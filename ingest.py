#!/usr/bin/env python3
"""
Automated Security Exam Ingest Pipeline
Converts PDFs → Markdown → Bullet Summaries → Flashcards

Usage: python ingest.py
"""

import re
import subprocess
import sys
from pathlib import Path
from typing import List, Dict

def run_pdf_converter(pdf_path: Path, output_path: Path):
    """Convert PDF to markdown using our pdf-to-md.py script"""
    try:
        result = subprocess.run([
            sys.executable, "pdf-to-md.py", 
            str(pdf_path), str(output_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Converted: {pdf_path.name} → {output_path.name}")
            return True
        else:
            print(f"❌ Failed to convert {pdf_path.name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error converting {pdf_path.name}: {e}")
        return False

def extract_key_concepts(content: str) -> List[str]:
    """Extract key concepts and definitions from markdown content"""
    concepts = []
    
    # Look for bullet points with definitions
    bullet_pattern = r'[-•]\s*\*\*(.*?)\*\*[:\s]+(.*?)(?=\n[-•]|\n#|\n\n|\Z)'
    matches = re.findall(bullet_pattern, content, re.DOTALL)
    
    for term, definition in matches:
        clean_def = re.sub(r'\s+', ' ', definition.strip())
        if len(clean_def) > 10:  # Skip very short definitions
            concepts.append(f"- **{term}**: {clean_def}")
    
    # Look for numbered definitions
    numbered_pattern = r'\d+\.\s*\*\*(.*?)\*\*[:\s]+(.*?)(?=\n\d+\.|\n#|\n\n|\Z)'
    matches = re.findall(numbered_pattern, content, re.DOTALL)
    
    for term, definition in matches:
        clean_def = re.sub(r'\s+', ' ', definition.strip())
        if len(clean_def) > 10:
            concepts.append(f"- **{term.strip()}**: {clean_def}")
    
    # Look for headers followed by content
    header_pattern = r'#{2,4}\s+(.*?)\n(.*?)(?=\n#{2,4}|\Z)'
    matches = re.findall(header_pattern, content, re.DOTALL)
    
    for header, content_block in matches:
        # Extract first meaningful sentence
        sentences = re.split(r'[.!?]\s+', content_block.strip())
        if sentences and len(sentences[0]) > 20:
            clean_sentence = re.sub(r'\s+', ' ', sentences[0])
            concepts.append(f"- **{header.strip()}**: {clean_sentence}")
    
    return concepts

def create_summary(file_path: Path, concepts: List[str]) -> str:
    """Create a structured summary from extracted concepts"""
    
    # Categorize concepts by keywords
    categories = {
        'Encryption & Cryptography': ['encrypt', 'crypto', 'cipher', 'key', 'hash', 'rsa', 'aes'],
        'Attacks & Threats': ['attack', 'threat', 'malware', 'virus', 'phishing', 'exploit'],
        'Security Controls': ['control', 'defense', 'protect', 'secure', 'authentication', 'authorization'],
        'Awareness & Training': ['awareness', 'training', 'user', 'social', 'human', 'education'],
        'Network Security': ['network', 'firewall', 'router', 'protocol', 'traffic'],
        'General Concepts': []  # Catch-all
    }
    
    categorized = {cat: [] for cat in categories}
    
    for concept in concepts:
        concept_lower = concept.lower()
        assigned = False
        
        for category, keywords in categories.items():
            if category == 'General Concepts':
                continue
            if any(keyword in concept_lower for keyword in keywords):
                categorized[category].append(concept)
                assigned = True
                break
        
        if not assigned:
            categorized['General Concepts'].append(concept)
    
    # Build summary
    title = file_path.stem.replace('_', ' ').replace('-', ' ').title()
    summary = [f"# {title} - Quick Summary\n"]
    
    for category, items in categorized.items():
        if items:
            summary.append(f"## {category}")
            summary.extend(items)
            summary.append("")
    
    return '\n'.join(summary)

def process_file(input_path: Path, temp_dir: Path, output_dir: Path):
    """Process a single file (PDF or MD) into a summary"""
    
    if input_path.suffix.lower() == '.pdf':
        # Convert PDF to markdown first
        temp_md = temp_dir / f"{input_path.stem}.md"
        if not run_pdf_converter(input_path, temp_md):
            return
        content_path = temp_md
    else:
        content_path = input_path
    
    # Read the markdown content
    try:
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {content_path}: {e}")
        return
    
    # Extract concepts and create summary
    concepts = extract_key_concepts(content)
    
    if not concepts:
        print(f"⚠️  No concepts extracted from {input_path.name}")
        return
    
    summary = create_summary(input_path, concepts)
    
    # Write summary to output
    output_file = output_dir / f"{input_path.stem.lower().replace(' ', '-')}-summary.md"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"📝 Created summary: {output_file.name} ({len(concepts)} concepts)")
    except Exception as e:
        print(f"❌ Error writing {output_file}: {e}")

def main():
    input_dir = Path("input")
    output_dir = Path("output")
    temp_dir = Path("temp")
    
    # Create directories
    output_dir.mkdir(exist_ok=True)
    temp_dir.mkdir(exist_ok=True)
    
    print("🚀 Starting Security Exam Ingest Pipeline")
    print("=" * 50)
    
    # Get all relevant files
    pdf_files = list(input_dir.glob("*.pdf"))
    md_files = list(input_dir.glob("*.md"))
    
    print(f"📄 Found {len(pdf_files)} PDFs and {len(md_files)} markdown files")
    
    total_processed = 0
    
    # Process all files
    for file_path in pdf_files + md_files:
        print(f"\n🔄 Processing: {file_path.name}")
        process_file(file_path, temp_dir, output_dir)
        total_processed += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Pipeline complete! Processed {total_processed} files")
    print(f"📁 Summaries saved to: {output_dir}")
    print(f"🎯 Ready for flashcard app!")
    
    # Clean up temp directory
    import shutil
    if temp_dir.exists():
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main() 