#!/usr/bin/env python3
"""
Convert Q/A formatted summaries to flashcard format
Extracts questions and answers from clean study guides
"""

import re
from pathlib import Path

def extract_qa_pairs(content: str):
    """Extract Q: A: pairs from markdown content"""
    qa_pairs = []
    
    # Pattern to match our Q: A: format
    pattern = r'\*\*Q:\s*(.*?)\*\*\s*\n\s*A:\s*(.*?)(?=\n\n|\n\*\*Q:|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for question, answer in matches:
        # Clean up whitespace and formatting
        question = re.sub(r'\s+', ' ', question.strip())
        answer = re.sub(r'\s+', ' ', answer.strip())
        
        if len(question) > 5 and len(answer) > 5:  # Skip very short ones
            qa_pairs.append((question, answer))
    
    return qa_pairs

def convert_to_flashcard_format(qa_pairs, source_file):
    """Convert Q/A pairs to the format expected by flashcards.py"""
    flashcard_content = []
    
    # Create header based on source file
    title = source_file.stem.replace('-', ' ').replace('_', ' ').title()
    flashcard_content.append(f"# {title} - Flashcards\n")
    
    # Convert each Q/A pair to bullet format
    for question, answer in qa_pairs:
        # Remove "What is" or similar prefixes if present for cleaner terms
        term = question
        if question.startswith("What is "):
            term = question[8:].rstrip("?")
        elif question.startswith("What are "):
            term = question[9:].rstrip("?")
        elif question.startswith("How "):
            term = f"How {question[4:].rstrip('?')}"
        
        flashcard_content.append(f"- **{term}**: {answer}")
    
    return '\n'.join(flashcard_content)

def main():
    """Convert all clean summaries to flashcard format"""
    summaries_dir = Path("summaries")
    output_dir = Path("output")
    
    if not summaries_dir.exists():
        print("❌ No summaries directory found!")
        return
    
    # Get all markdown files from summaries
    summary_files = list(summaries_dir.glob("*.md"))
    
    if not summary_files:
        print("❌ No summary files found!")
        return
    
    total_cards = 0
    
    print("🔄 Converting Q/A summaries to flashcard format...")
    print("=" * 50)
    
    for file_path in summary_files:
        print(f"📝 Processing: {file_path.name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract Q/A pairs
            qa_pairs = extract_qa_pairs(content)
            
            if not qa_pairs:
                print(f"⚠️  No Q/A pairs found in {file_path.name}")
                continue
            
            # Convert to flashcard format
            flashcard_content = convert_to_flashcard_format(qa_pairs, file_path)
            
            # Write to output directory with -flashcards suffix
            output_file = output_dir / f"{file_path.stem}-flashcards.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(flashcard_content)
            
            print(f"✅ Created: {output_file.name} ({len(qa_pairs)} cards)")
            total_cards += len(qa_pairs)
            
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
    
    print("\n" + "=" * 50)
    print(f"🎯 Conversion complete! Created {total_cards} flashcards total")
    print(f"📁 Flashcards saved to: {output_dir}")
    print("🚀 Ready to use with: python flashcards.py")

if __name__ == "__main__":
    main() 