#!/usr/bin/env python3
"""
Quick flashcard generator for security exam prep
Usage: python flashcard-generator.py <summary-file.md>
"""

import re
import json
import random
import sys
from pathlib import Path

def parse_summary_to_flashcards(file_path):
    """Convert markdown bullet points to Q&A flashcards"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    flashcards = []
    
    # Find all bullet points with definitions
    pattern = r'- \*\*(.*?)\*\*:\s*(.*?)(?=\n-|\n#|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for term, definition in matches:
        # Clean up definition
        definition = re.sub(r'\s+', ' ', definition.strip())
        flashcards.append({
            'question': f"What is {term}?",
            'answer': definition,
            'term': term,
            'difficulty': 'new'
        })
    
    return flashcards

def study_session(flashcards):
    """Interactive study session"""
    random.shuffle(flashcards)
    correct = 0
    total = len(flashcards)
    
    print(f"\n🚀 Study Session Started! ({total} cards)")
    print("Commands: 'y' = got it right, 'n' = need more practice, 'q' = quit\n")
    
    for i, card in enumerate(flashcards, 1):
        print(f"Card {i}/{total}")
        print(f"Q: {card['question']}")
        input("Press Enter to see answer...")
        print(f"A: {card['answer']}")
        
        while True:
            response = input("Did you get it right? (y/n/q): ").lower()
            if response == 'y':
                card['difficulty'] = 'easy' if card['difficulty'] == 'new' else card['difficulty']
                correct += 1
                break
            elif response == 'n':
                card['difficulty'] = 'hard'
                break
            elif response == 'q':
                return correct, i
            else:
                print("Please enter 'y', 'n', or 'q'")
        
        print("-" * 50)
    
    return correct, total

def main():
    if len(sys.argv) != 2:
        print("Usage: python flashcard-generator.py <summary-file.md>")
        return
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File {file_path} not found!")
        return
    
    # Generate flashcards
    flashcards = parse_summary_to_flashcards(file_path)
    
    if not flashcards:
        print("No flashcards found in file!")
        return
    
    print(f"Generated {len(flashcards)} flashcards from {file_path.name}")
    
    while True:
        print("\nOptions:")
        print("1. Start study session")
        print("2. Show all cards")
        print("3. Filter by difficulty")
        print("4. Quit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == '1':
            correct, attempted = study_session(flashcards.copy())
            print(f"\nSession complete! Score: {correct}/{attempted} ({correct/attempted*100:.1f}%)")
            
        elif choice == '2':
            for card in flashcards:
                print(f"Q: {card['question']}")
                print(f"A: {card['answer']}")
                print(f"Difficulty: {card['difficulty']}\n")
                
        elif choice == '3':
            difficulty = input("Filter by difficulty (new/easy/hard): ").lower()
            filtered = [c for c in flashcards if c['difficulty'] == difficulty]
            print(f"\nFound {len(filtered)} {difficulty} cards:")
            for card in filtered:
                print(f"- {card['term']}")
                
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main() 