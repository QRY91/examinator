#!/usr/bin/env python3
"""
Examinator Ecosystem Integration Example

This demonstrates how examinator can integrate with the QRY ecosystem database
to generate flashcards from uroboro captures and use wherewasi context for
enhanced study experiences.

Usage:
    python ecosystem_integration_example.py generate --project myproject
    python ecosystem_integration_example.py study --project myproject
    python ecosystem_integration_example.py sync
"""

import sqlite3
import json
import os
import sys
import argparse
import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

# Ecosystem constants
class ToolName(Enum):
    WHEREWASI = "wherewasi"
    UROBORO = "uroboro"
    EXAMINATOR = "examinator"
    QRYAI = "qryai"
    DOGGOWOOF = "doggowoof"
    QOMOBORO = "qomoboro"

class MessageType(Enum):
    CAPTURE = "capture"
    CONTEXT_UPDATE = "context_update"
    FLASHCARD_REQUEST = "flashcard_request"
    STUDY_SESSION = "study_session"
    PROJECT_ACTIVITY = "project_activity"
    INSIGHT = "insight"

# Data structures
@dataclass
class ContextSession:
    id: int
    project: str
    timestamp: datetime.datetime
    context_data: str
    session_info: str
    keywords: str
    git_branch: Optional[str] = None
    git_commit: Optional[str] = None

@dataclass
class Capture:
    id: int
    timestamp: datetime.datetime
    content: str
    project: Optional[str]
    tags: Optional[str]
    source_tool: str
    metadata: Optional[str] = None
    context_session_id: Optional[int] = None

@dataclass
class Flashcard:
    id: int
    question: str
    answer: str
    category: Optional[str]
    difficulty: int
    source_capture_id: Optional[int]
    context_session_id: Optional[int]
    project: Optional[str]
    created_at: datetime.datetime
    last_reviewed: Optional[datetime.datetime] = None
    next_review: Optional[datetime.datetime] = None
    ease_factor: float = 2.5
    review_count: int = 0
    correct_streak: int = 0

@dataclass
class StudySession:
    id: int
    project: Optional[str]
    flashcards_reviewed: int
    correct_answers: int
    duration_minutes: int
    context_session_id: Optional[int]
    created_at: datetime.datetime

@dataclass
class ToolMessage:
    id: int
    from_tool: str
    to_tool: str
    message_type: str
    data: str
    processed: bool
    created_at: datetime.datetime
    processed_at: Optional[datetime.datetime] = None

class EcosystemDatabase:
    """QRY Ecosystem Database Integration for Examinator"""
    
    def __init__(self, force_local: bool = False):
        self.db_path = self._discover_database(force_local)
        self.is_shared = self._is_ecosystem_database()
        self.connection = None
        self._connect()
        self._ensure_examinator_tables()
    
    def _discover_database(self, force_local: bool) -> str:
        """Discover ecosystem database or fall back to local"""
        if not force_local:
            # Try shared ecosystem database
            home_dir = Path.home()
            shared_path = home_dir / ".local" / "share" / "qry" / "ecosystem.sqlite"
            
            if shared_path.parent.exists() or not shared_path.exists():
                shared_path.parent.mkdir(parents=True, exist_ok=True)
                return str(shared_path)
        
        # Fall back to local examinator database
        data_dir = Path.home() / ".local" / "share" / "examinator"
        data_dir.mkdir(parents=True, exist_ok=True)
        return str(data_dir / "examinator.sqlite")
    
    def _is_ecosystem_database(self) -> bool:
        """Check if this is a shared ecosystem database"""
        return "ecosystem.sqlite" in self.db_path
    
    def _connect(self):
        """Establish database connection"""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        # Enable foreign keys
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.execute("PRAGMA journal_mode = WAL")
    
    def _ensure_examinator_tables(self):
        """Create examinator-specific tables if they don't exist"""
        schema = """
        -- Flashcards for spaced repetition
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT,
            difficulty INTEGER DEFAULT 1,
            source_capture_id INTEGER,
            context_session_id INTEGER,
            project TEXT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_reviewed DATETIME,
            next_review DATETIME,
            ease_factor REAL DEFAULT 2.5,
            review_count INTEGER DEFAULT 0,
            correct_streak INTEGER DEFAULT 0,
            FOREIGN KEY (source_capture_id) REFERENCES captures(id),
            FOREIGN KEY (context_session_id) REFERENCES context_sessions(id)
        );
        
        -- Study sessions
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT,
            flashcards_reviewed INTEGER DEFAULT 0,
            correct_answers INTEGER DEFAULT 0,
            duration_minutes INTEGER,
            context_session_id INTEGER,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (context_session_id) REFERENCES context_sessions(id)
        );
        
        -- Flashcard reviews (detailed tracking)
        CREATE TABLE IF NOT EXISTS flashcard_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flashcard_id INTEGER NOT NULL,
            study_session_id INTEGER,
            response_quality INTEGER, -- 0-5 scale
            response_time_ms INTEGER,
            was_correct BOOLEAN,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (flashcard_id) REFERENCES flashcards(id),
            FOREIGN KEY (study_session_id) REFERENCES study_sessions(id)
        );
        
        -- Indexes
        CREATE INDEX IF NOT EXISTS idx_flashcards_project ON flashcards(project);
        CREATE INDEX IF NOT EXISTS idx_flashcards_next_review ON flashcards(next_review);
        CREATE INDEX IF NOT EXISTS idx_flashcards_source_capture ON flashcards(source_capture_id);
        CREATE INDEX IF NOT EXISTS idx_study_sessions_project ON study_sessions(project);
        CREATE INDEX IF NOT EXISTS idx_flashcard_reviews_flashcard ON flashcard_reviews(flashcard_id);
        """
        
        self.connection.executescript(schema)
        self.connection.commit()
    
    def get_unprocessed_messages(self, tool_name: str) -> List[ToolMessage]:
        """Get unprocessed messages for a specific tool"""
        if not self.is_shared:
            return []
        
        cursor = self.connection.execute("""
            SELECT id, from_tool, to_tool, message_type, data, processed, created_at, processed_at
            FROM tool_messages 
            WHERE to_tool = ? AND processed = FALSE
            ORDER BY created_at ASC
        """, (tool_name,))
        
        messages = []
        for row in cursor.fetchall():
            msg = ToolMessage(
                id=row['id'],
                from_tool=row['from_tool'],
                to_tool=row['to_tool'],
                message_type=row['message_type'],
                data=row['data'],
                processed=bool(row['processed']),
                created_at=datetime.datetime.fromisoformat(row['created_at']),
                processed_at=datetime.datetime.fromisoformat(row['processed_at']) if row['processed_at'] else None
            )
            messages.append(msg)
        
        return messages
    
    def mark_message_processed(self, message_id: int):
        """Mark a tool message as processed"""
        self.connection.execute("""
            UPDATE tool_messages 
            SET processed = TRUE, processed_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (message_id,))
        self.connection.commit()
    
    def get_recent_captures(self, project: str, limit: int = 10) -> List[Capture]:
        """Get recent captures for flashcard generation"""
        if not self.is_shared:
            return []
        
        cursor = self.connection.execute("""
            SELECT id, timestamp, content, project, tags, source_tool, metadata, context_session_id, created_at, updated_at
            FROM captures 
            WHERE project = ?
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (project, limit))
        
        captures = []
        for row in cursor.fetchall():
            capture = Capture(
                id=row['id'],
                timestamp=datetime.datetime.fromisoformat(row['timestamp']),
                content=row['content'],
                project=row['project'],
                tags=row['tags'],
                source_tool=row['source_tool'],
                metadata=row['metadata'],
                context_session_id=row['context_session_id']
            )
            captures.append(capture)
        
        return captures
    
    def get_recent_context(self, project: str, limit: int = 1) -> List[ContextSession]:
        """Get recent context sessions for a project"""
        if not self.is_shared:
            return []
        
        cursor = self.connection.execute("""
            SELECT id, project, timestamp, context_data, session_info, keywords, git_branch, git_commit, created_at
            FROM context_sessions 
            WHERE project = ?
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (project, limit))
        
        sessions = []
        for row in cursor.fetchall():
            session = ContextSession(
                id=row['id'],
                project=row['project'],
                timestamp=datetime.datetime.fromisoformat(row['timestamp']),
                context_data=row['context_data'],
                session_info=row['session_info'],
                keywords=row['keywords'],
                git_branch=row['git_branch'],
                git_commit=row['git_commit']
            )
            sessions.append(session)
        
        return sessions
    
    def create_flashcard(self, question: str, answer: str, category: str = None, 
                        difficulty: int = 1, source_capture_id: int = None, 
                        context_session_id: int = None, project: str = None) -> Flashcard:
        """Create a new flashcard"""
        cursor = self.connection.execute("""
            INSERT INTO flashcards (question, answer, category, difficulty, source_capture_id, context_session_id, project)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, answer, category, difficulty, source_capture_id, context_session_id, project))
        
        flashcard_id = cursor.lastrowid
        self.connection.commit()
        
        return Flashcard(
            id=flashcard_id,
            question=question,
            answer=answer,
            category=category,
            difficulty=difficulty,
            source_capture_id=source_capture_id,
            context_session_id=context_session_id,
            project=project,
            created_at=datetime.datetime.now()
        )
    
    def get_flashcards_for_review(self, project: str = None, limit: int = 10) -> List[Flashcard]:
        """Get flashcards that are due for review"""
        query = """
            SELECT id, question, answer, category, difficulty, source_capture_id, 
                   context_session_id, project, created_at, last_reviewed, next_review,
                   ease_factor, review_count, correct_streak
            FROM flashcards 
            WHERE (next_review IS NULL OR next_review <= CURRENT_TIMESTAMP)
        """
        params = []
        
        if project:
            query += " AND project = ?"
            params.append(project)
        
        query += " ORDER BY created_at ASC LIMIT ?"
        params.append(limit)
        
        cursor = self.connection.execute(query, params)
        
        flashcards = []
        for row in cursor.fetchall():
            flashcard = Flashcard(
                id=row['id'],
                question=row['question'],
                answer=row['answer'],
                category=row['category'],
                difficulty=row['difficulty'],
                source_capture_id=row['source_capture_id'],
                context_session_id=row['context_session_id'],
                project=row['project'],
                created_at=datetime.datetime.fromisoformat(row['created_at']),
                last_reviewed=datetime.datetime.fromisoformat(row['last_reviewed']) if row['last_reviewed'] else None,
                next_review=datetime.datetime.fromisoformat(row['next_review']) if row['next_review'] else None,
                ease_factor=row['ease_factor'],
                review_count=row['review_count'],
                correct_streak=row['correct_streak']
            )
            flashcards.append(flashcard)
        
        return flashcards
    
    def record_flashcard_review(self, flashcard_id: int, was_correct: bool, response_quality: int):
        """Record a flashcard review and update spaced repetition algorithm"""
        # Get current flashcard
        cursor = self.connection.execute("""
            SELECT ease_factor, review_count, correct_streak
            FROM flashcards WHERE id = ?
        """, (flashcard_id,))
        
        row = cursor.fetchone()
        if not row:
            return
        
        ease_factor = row['ease_factor']
        review_count = row['review_count']
        correct_streak = row['correct_streak']
        
        # Update based on spaced repetition algorithm
        if was_correct:
            correct_streak += 1
            ease_factor = max(1.3, ease_factor + (0.1 - (5 - response_quality) * (0.08 + (5 - response_quality) * 0.02)))
            
            # Calculate next review interval
            if review_count == 0:
                interval_days = 1
            elif review_count == 1:
                interval_days = 6
            else:
                interval_days = int(6 * (ease_factor ** (review_count - 1)))
        else:
            correct_streak = 0
            ease_factor = max(1.3, ease_factor - 0.2)
            interval_days = 1
        
        next_review = datetime.datetime.now() + datetime.timedelta(days=interval_days)
        
        # Update flashcard
        self.connection.execute("""
            UPDATE flashcards 
            SET last_reviewed = CURRENT_TIMESTAMP,
                next_review = ?,
                ease_factor = ?,
                review_count = review_count + 1,
                correct_streak = ?
            WHERE id = ?
        """, (next_review.isoformat(), ease_factor, correct_streak, flashcard_id))
        
        self.connection.commit()
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

class FlashcardGenerator:
    """Generate flashcards from uroboro captures using AI-like text processing"""
    
    @staticmethod
    def generate_from_capture(capture: Capture, context: ContextSession = None) -> List[Tuple[str, str, str]]:
        """Generate question-answer pairs from capture content"""
        content = capture.content.strip()
        
        # Simple heuristic-based flashcard generation
        flashcards = []
        
        # If content contains "Fixed" or "Implemented" - create Q&A about the solution
        if any(word in content.lower() for word in ['fixed', 'implemented', 'added', 'created']):
            question = f"What was accomplished in {capture.project or 'the project'}?"
            answer = content
            category = "accomplishments"
            flashcards.append((question, answer, category))
        
        # If content contains technical terms - create definition flashcards
        technical_terms = FlashcardGenerator._extract_technical_terms(content)
        for term in technical_terms:
            question = f"What is {term} in the context of {capture.project or 'this project'}?"
            answer = f"Based on capture: {content}"
            category = "technical_concepts"
            flashcards.append((question, answer, category))
        
        # If content mentions a problem/bug - create troubleshooting flashcard
        if any(word in content.lower() for word in ['bug', 'error', 'issue', 'problem']):
            question = f"How was this issue resolved: {content[:50]}...?"
            answer = content
            category = "troubleshooting"
            flashcards.append((question, answer, category))
        
        # Use context keywords for enhanced categorization
        if context and context.keywords:
            category = f"context_{context.keywords.replace(' ', '_')}"
            question = f"What was learned about {context.keywords}?"
            answer = content
            flashcards.append((question, answer, category))
        
        return flashcards[:3]  # Limit to 3 flashcards per capture
    
    @staticmethod
    def _extract_technical_terms(content: str) -> List[str]:
        """Extract potential technical terms from content"""
        # Simple keyword extraction
        tech_indicators = ['API', 'database', 'function', 'class', 'method', 'algorithm', 'framework']
        terms = []
        
        words = content.split()
        for word in words:
            word_clean = word.strip('.,!?();:')
            if (word_clean.isupper() and len(word_clean) > 2) or word_clean in tech_indicators:
                terms.append(word_clean)
        
        return list(set(terms))[:2]  # Return max 2 terms

class StudySessionManager:
    """Manage study sessions with ecosystem integration"""
    
    def __init__(self, db: EcosystemDatabase):
        self.db = db
    
    def start_study_session(self, project: str = None) -> int:
        """Start a new study session"""
        # Get recent context if available
        context_session_id = None
        if project and self.db.is_shared:
            contexts = self.db.get_recent_context(project, 1)
            if contexts:
                context_session_id = contexts[0].id
                print(f"🔗 Study session linked to context: {contexts[0].session_info}")
        
        # Get flashcards for review
        flashcards = self.db.get_flashcards_for_review(project, 10)
        
        if not flashcards:
            print("📚 No flashcards due for review!")
            return 0
        
        print(f"📚 Starting study session with {len(flashcards)} flashcards")
        
        correct_answers = 0
        start_time = datetime.datetime.now()
        
        for i, flashcard in enumerate(flashcards, 1):
            print(f"\n--- Flashcard {i}/{len(flashcards)} ---")
            print(f"Category: {flashcard.category or 'General'}")
            print(f"Question: {flashcard.question}")
            
            input("Press Enter to see answer...")
            print(f"Answer: {flashcard.answer}")
            
            # Get user response
            while True:
                response = input("\nWas this correct? (y/n): ").lower().strip()
                if response in ['y', 'yes']:
                    correct_answers += 1
                    quality = int(input("Quality (1-5, 5=perfect): ") or "3")
                    self.db.record_flashcard_review(flashcard.id, True, quality)
                    break
                elif response in ['n', 'no']:
                    quality = int(input("Quality (1-5, 1=completely wrong): ") or "1")
                    self.db.record_flashcard_review(flashcard.id, False, quality)
                    break
                else:
                    print("Please enter 'y' or 'n'")
        
        duration_minutes = int((datetime.datetime.now() - start_time).total_seconds() / 60)
        
        # Record study session
        cursor = self.db.connection.execute("""
            INSERT INTO study_sessions (project, flashcards_reviewed, correct_answers, duration_minutes, context_session_id)
            VALUES (?, ?, ?, ?, ?)
        """, (project, len(flashcards), correct_answers, duration_minutes, context_session_id))
        
        session_id = cursor.lastrowid
        self.db.connection.commit()
        
        # Show results
        accuracy = (correct_answers / len(flashcards)) * 100 if flashcards else 0
        print(f"\n✅ Study session complete!")
        print(f"📊 Accuracy: {accuracy:.1f}% ({correct_answers}/{len(flashcards)})")
        print(f"⏱️  Duration: {duration_minutes} minutes")
        
        return session_id

def process_ecosystem_messages(db: EcosystemDatabase):
    """Process messages from other ecosystem tools"""
    if not db.is_shared:
        print("📁 Local database mode - no ecosystem messages to process")
        return
    
    messages = db.get_unprocessed_messages(ToolName.EXAMINATOR.value)
    processed_count = 0
    
    generator = FlashcardGenerator()
    
    for msg in messages:
        try:
            if msg.message_type == MessageType.CAPTURE.value:
                # Process capture message from uroboro
                data = json.loads(msg.data)
                content = data.get('content', '')
                project = data.get('project', '')
                
                if content and project:
                    # Create mock capture object
                    capture = Capture(
                        id=0,  # We don't have the actual ID
                        timestamp=datetime.datetime.now(),
                        content=content,
                        project=project,
                        tags=data.get('tags', ''),
                        source_tool='uroboro'
                    )
                    
                    # Get recent context for this project
                    context = None
                    contexts = db.get_recent_context(project, 1)
                    if contexts:
                        context = contexts[0]
                    
                    # Generate flashcards
                    flashcard_data = generator.generate_from_capture(capture, context)
                    
                    for question, answer, category in flashcard_data:
                        db.create_flashcard(
                            question=question,
                            answer=answer,
                            category=category,
                            project=project,
                            context_session_id=context.id if context else None
                        )
                    
                    print(f"📝 Generated {len(flashcard_data)} flashcards from uroboro capture")
                    processed_count += 1
                
            db.mark_message_processed(msg.id)
            
        except Exception as e:
            print(f"⚠️  Failed to process message {msg.id}: {e}")
    
    if processed_count > 0:
        print(f"✅ Processed {processed_count} ecosystem messages")
    else:
        print("📝 No new ecosystem messages to process")

def generate_flashcards_from_captures(db: EcosystemDatabase, project: str):
    """Generate flashcards from recent uroboro captures"""
    if not db.is_shared:
        print("📁 Local database mode - use 'sync' command to process ecosystem messages")
        return
    
    captures = db.get_recent_captures(project, 10)
    if not captures:
        print(f"📝 No recent captures found for project '{project}'")
        return
    
    print(f"📚 Found {len(captures)} recent captures for '{project}'")
    
    # Get recent context
    context = None
    contexts = db.get_recent_context(project, 1)
    if contexts:
        context = contexts[0]
        print(f"🔗 Using context: {context.session_info}")
    
    generator = FlashcardGenerator()
    total_flashcards = 0
    
    for capture in captures:
        flashcard_data = generator.generate_from_capture(capture, context)
        
        for question, answer, category in flashcard_data:
            db.create_flashcard(
                question=question,
                answer=answer,
                category=category,
                project=project,
                source_capture_id=capture.id,
                context_session_id=context.id if context else None
            )
            total_flashcards += 1
    
    print(f"✅ Generated {total_flashcards} flashcards from recent captures")

def main():
    parser = argparse.ArgumentParser(description="Examinator - QRY Ecosystem Flashcard System")
    parser.add_argument("--local", action="store_true", help="Force local database mode")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate flashcards from captures")
    generate_parser.add_argument("--project", required=True, help="Project name")
    
    # Study command
    study_parser = subparsers.add_parser("study", help="Start study session")
    study_parser.add_argument("--project", help="Project name (optional)")
    
    # Sync command
    sync_parser = subparsers.add_parser("sync", help="Process ecosystem messages")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show system status")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize database
    db = EcosystemDatabase(force_local=args.local)
    
    try:
        if db.is_shared:
            print(f"🔗 Connected to QRY ecosystem database")
        else:
            print(f"📁 Using local examinator database")
        print(f"    Database: {db.db_path}")
        print()
        
        if args.command == "generate":
            generate_flashcards_from_captures(db, args.project)
        
        elif args.command == "study":
            session_manager = StudySessionManager(db)
            session_manager.start_study_session(args.project)
        
        elif args.command == "sync":
            process_ecosystem_messages(db)
        
        elif args.command == "status":
            print(f"📊 Examinator Status")
            print(f"Database: {db.db_path}")
            print(f"Ecosystem mode: {'ENABLED' if db.is_shared else 'DISABLED'}")
            
            # Show flashcard counts
            cursor = db.connection.execute("SELECT COUNT(*) FROM flashcards")
            total_flashcards = cursor.fetchone()[0]
            
            cursor = db.connection.execute("SELECT COUNT(*) FROM flashcards WHERE next_review <= CURRENT_TIMESTAMP OR next_review IS NULL")
            due_flashcards = cursor.fetchone()[0]
            
            print(f"Total flashcards: {total_flashcards}")
            print(f"Due for review: {due_flashcards}")
    
    finally:
        db.close()

if __name__ == "__main__":
    main()