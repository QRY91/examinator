#!/usr/bin/env python3
"""
Smart Flashcard TUI - ADHD-friendly spaced repetition
Focuses on hard cards, avoids easy-card traps
"""

import re
import json
import random
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, Label, ProgressBar, Header, Footer
from textual.binding import Binding

class FlashCard:
    def __init__(self, question: str, answer: str, term: str):
        self.question = question
        self.answer = answer
        self.term = term
        self.difficulty = 'new'  # new, easy, medium, hard
        self.last_seen = None
        self.times_correct = 0
        self.times_wrong = 0
        self.weight = 1.0  # Higher weight = more likely to appear

    def mark_correct(self):
        self.times_correct += 1
        self.last_seen = datetime.now()
        
        # ADHD-friendly: Quick promotion but slow demotion
        if self.times_correct >= 3 and self.times_wrong == 0:
            self.difficulty = 'easy'
            self.weight = 0.1  # Very low chance to appear
        elif self.times_correct >= 2:
            self.difficulty = 'medium'
            self.weight = 0.3
        else:
            self.weight = 0.5

    def mark_wrong(self):
        self.times_wrong += 1
        self.last_seen = datetime.now()
        self.difficulty = 'hard'
        self.weight = 2.0  # High chance to appear again
        # Reset correct counter to make it harder to become easy
        self.times_correct = max(0, self.times_correct - 1)

    def get_priority_score(self):
        """Higher score = should appear sooner"""
        base_score = self.weight
        
        # Boost cards not seen recently
        if self.last_seen:
            hours_since = (datetime.now() - self.last_seen).total_seconds() / 3600
            if hours_since > 1:  # Boost after 1 hour
                base_score *= (1 + hours_since / 24)
        else:
            base_score *= 2  # New cards get priority
            
        return base_score

class CardDisplay(Static):
    def __init__(self, card: FlashCard = None):
        super().__init__()
        self.card = card
        self.showing_answer = False

    def compose(self) -> ComposeResult:
        if not self.card:
            yield Label("Loading cards...", id="card-content")
            return
            
        if self.showing_answer:
            yield Label(f"Q: {self.card.question}", classes="question")
            yield Label(f"A: {self.card.answer}", classes="answer")
        else:
            yield Label(f"Q: {self.card.question}", classes="question")
            yield Label("Press SPACE to reveal answer", classes="hint")

    def show_answer(self):
        self.showing_answer = True
        self.remove_children()
        self.mount(Label(f"Q: {self.card.question}", classes="question"))
        self.mount(Label(f"A: {self.card.answer}", classes="answer"))

    def set_card(self, card: FlashCard):
        self.card = card
        self.showing_answer = False
        # Clear and rebuild the display
        self.remove_children()
        if self.card:
            self.mount(Label(f"Q: {self.card.question}", classes="question"))
            self.mount(Label("Press SPACE to reveal answer", classes="hint"))

class StatsDisplay(Static):
    def __init__(self):
        super().__init__()
        self.total_cards = 0
        self.hard_cards = 0
        self.easy_cards = 0
        self.session_correct = 0
        self.session_wrong = 0

    def compose(self) -> ComposeResult:
        yield Label(f"Total: {self.total_cards} | Hard: {self.hard_cards} | Easy: {self.easy_cards}")
        yield Label(f"Session: ✓{self.session_correct} ✗{self.session_wrong}")

    def update_stats(self, cards: List[FlashCard], session_correct: int, session_wrong: int):
        self.total_cards = len(cards)
        self.hard_cards = len([c for c in cards if c.difficulty == 'hard'])
        self.easy_cards = len([c for c in cards if c.difficulty == 'easy'])
        self.session_correct = session_correct
        self.session_wrong = session_wrong
        self.refresh()

class FlashcardApp(App):
    # Zenburn theme - easy on the eyes for long study sessions
    CSS = """
    Screen {
        background: #3f3f3f;
        color: #dcdcdc;
    }
    
    Header {
        background: #2b2b2b;
        color: #f0dfaf;
    }
    
    Footer {
        background: #2b2b2b; 
        color: #8cd0d3;
    }
    
    .question {
        text-style: bold;
        color: #8cd0d3;
        padding: 1;
        background: #4f4f4f;
    }
    .answer {
        color: #9fdf9f;
        padding: 1;
        background: #4f4f4f;
    }
    .hint {
        color: #f0dfaf;
        text-style: italic;
        padding: 1;
    }
    #card-area {
        height: 12;
        border: solid #6f6f6f;
        padding: 1;
        background: #4f4f4f;
    }
    #controls {
        height: 3;
        align: center middle;
        background: #3f3f3f;
    }
    #stats {
        height: 3;
        border: solid #6f6f6f;
        background: #4f4f4f;
        color: #dfaf8f;
    }
    
    Button {
        background: #5f5f5f;
        color: #dcdcdc;
        border: solid #6f6f6f;
    }
    
    Button.-success {
        background: #60b48a;
        color: #2b2b2b;
    }
    
    Button.-error {
        background: #cc9393;
        color: #2b2b2b;
    }
    
    Button:hover {
        background: #7f7f7f;
    }
    """

    BINDINGS = [
        Binding("space", "show_answer", "Show Answer"),
        Binding("g", "mark_correct", "Got it (G)"),
        Binding("n", "mark_wrong", "Need practice (N)"),
        Binding("s", "skip", "Skip (S)"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.cards: List[FlashCard] = []
        self.current_card = None
        self.session_correct = 0
        self.session_wrong = 0
        self.card_display = None
        self.stats_display = None

    def compose(self) -> ComposeResult:
        yield Header()
        
        with Vertical():
            self.stats_display = StatsDisplay()
            yield self.stats_display
            
            with Container(id="card-area"):
                self.card_display = CardDisplay()
                yield self.card_display
            
            with Horizontal(id="controls"):
                yield Button("Got it (G)", id="correct", variant="success")
                yield Button("Need practice (N)", id="wrong", variant="error")
                yield Button("Skip (S)", id="skip", variant="default")
        
        yield Footer()

    def on_mount(self):
        self.load_cards()
        # Add a small delay to ensure widgets are properly initialized
        self.call_later(self.next_card)

    def load_cards(self):
        """Load cards from markdown summaries"""
        summary_files = list(Path("output").glob("*-summary.md"))
        
        if not summary_files:
            self.notify("No summary files found in output/ directory!")
            return
            
        cards_loaded = 0
        for file_path in summary_files:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Extract flashcards from markdown
                pattern = r'- \*\*(.*?)\*\*:\s*(.*?)(?=\n-|\n#|\Z)'
                matches = re.findall(pattern, content, re.DOTALL)
                
                for term, definition in matches:
                    definition = re.sub(r'\s+', ' ', definition.strip())
                    card = FlashCard(
                        question=f"What is {term}?",
                        answer=definition,
                        term=term
                    )
                    self.cards.append(card)
                    cards_loaded += 1
                    
                self.notify(f"Loaded {len(matches)} cards from {file_path.name}")
                    
            except Exception as e:
                self.notify(f"Error loading {file_path.name}: {e}")
        
        if self.cards:
            self.title = f"Smart Flashcards ({len(self.cards)} cards)"
            self.notify(f"Ready to study! Loaded {cards_loaded} total cards.")
        else:
            self.title = "Smart Flashcards (No cards loaded)"
            self.notify("No cards found! Check your summary files.")

    def get_next_card(self) -> FlashCard:
        """Smart card selection - weighted by difficulty and recency"""
        if not self.cards:
            self.notify("No cards available for selection!")
            return None
            
        # Calculate weights for all cards
        weights = [card.get_priority_score() for card in self.cards]
        
        # Weighted random selection
        selected = random.choices(self.cards, weights=weights, k=1)[0]
        self.notify(f"Selected card: {selected.term}")
        return selected

    def next_card(self):
        self.current_card = self.get_next_card()
        if self.current_card:
            if self.card_display:
                self.card_display.set_card(self.current_card)
                self.notify(f"Displaying: {self.current_card.term}")
            else:
                self.notify("Card display not ready!")
        else:
            self.notify("No current card available!")
        self.update_stats()

    def update_stats(self):
        if self.stats_display:
            self.stats_display.update_stats(
                self.cards, self.session_correct, self.session_wrong
            )

    def action_show_answer(self):
        if self.card_display and self.current_card:
            self.card_display.show_answer()

    def action_mark_correct(self):
        if self.current_card:
            self.current_card.mark_correct()
            self.session_correct += 1
            self.next_card()

    def action_mark_wrong(self):
        if self.current_card:
            self.current_card.mark_wrong()
            self.session_wrong += 1
            self.next_card()

    def action_skip(self):
        self.next_card()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "correct":
            self.action_mark_correct()
        elif event.button.id == "wrong":
            self.action_mark_wrong()
        elif event.button.id == "skip":
            self.action_skip()

if __name__ == "__main__":
    app = FlashcardApp()
    app.run() 