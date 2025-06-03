#!/usr/bin/env python3
"""
Security Summary Tidy Tool
Cleans up malformed summaries, removes duplicates, fixes formatting
For high-quality exam prep materials

Usage: python tidy.py [--all | specific-summary.md]
"""

import re
import sys
from pathlib import Path
from typing import List, Set, Dict
from collections import defaultdict

def clean_text(text: str) -> str:
    """Clean up malformed text"""
    # Remove excessive symbols and markdown artifacts
    text = re.sub(r'[●○■]+\s*', '- ', text)
    text = re.sub(r'#{2,}\s*(Chapter \d+[:\s]*["\']?Attacks["\']?)\s*#{0,}', '', text)
    text = re.sub(r'##\s*Page \d+', '', text)
    text = re.sub(r'##\s*Source:\s*https?://[^\s]+', '', text)
    
    # Fix broken sentences
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'([a-z])\.\s+([A-Z])', r'\1. \2', text)
    
    # Remove incomplete thoughts
    text = re.sub(r'[:\s]*[a-z]+\s*$', '', text)
    
    return text.strip()

def is_valid_concept(concept: str, min_length: int = 30) -> bool:
    """Check if a concept is worth keeping"""
    # Remove markdown formatting for length check
    clean_concept = re.sub(r'\*\*.*?\*\*:\s*', '', concept)
    clean_concept = re.sub(r'[-•]\s*', '', clean_concept)
    
    # Skip if too short
    if len(clean_concept) < min_length:
        return False
    
    # Skip if mostly symbols or repeated characters
    if re.match(r'^[^a-zA-Z]*$', clean_concept):
        return False
    
    # Skip if looks like broken markdown
    if '##' in clean_concept or concept.count('●') > 3:
        return False
    
    # Skip if no actual content after the term
    if re.match(r'- \*\*.*?\*\*:\s*$', concept):
        return False
        
    return True

def extract_term_and_definition(concept: str) -> tuple:
    """Extract clean term and definition from concept"""
    match = re.match(r'- \*\*(.*?)\*\*:\s*(.*)', concept)
    if not match:
        return None, None
    
    term = clean_text(match.group(1)).strip()
    definition = clean_text(match.group(2)).strip()
    
    # Skip malformed terms
    if len(term) < 2 or len(definition) < 10:
        return None, None
    
    return term, definition

def deduplicate_concepts(concepts: List[str]) -> List[str]:
    """Remove duplicate and similar concepts"""
    seen_terms = set()
    seen_definitions = set()
    clean_concepts = []
    
    for concept in concepts:
        term, definition = extract_term_and_definition(concept)
        if not term or not definition:
            continue
            
        # Normalize for comparison
        norm_term = term.lower().strip()
        norm_def = re.sub(r'\s+', ' ', definition.lower().strip())
        
        # Skip exact duplicates
        if norm_term in seen_terms or norm_def in seen_definitions:
            continue
            
        # Skip very similar definitions (first 50 chars)
        def_prefix = norm_def[:50]
        if any(def_prefix in existing for existing in seen_definitions):
            continue
            
        seen_terms.add(norm_term)
        seen_definitions.add(norm_def)
        clean_concepts.append(f"- **{term}**: {definition}")
    
    return clean_concepts

def categorize_concepts(concepts: List[str]) -> Dict[str, List[str]]:
    """Categorize concepts with better logic"""
    categories = {
        'Cryptography & Encryption': [
            'encrypt', 'crypto', 'cipher', 'key', 'hash', 'rsa', 'aes', 'des', 
            'tls', 'ssl', 'certificate', 'digital signature', 'pki'
        ],
        'Network Attacks': [
            'ddos', 'dos', 'sniffing', 'spoofing', 'man-in-the-middle', 'mitm',
            'arp', 'dns', 'replay', 'wireless', 'wifi', 'wep', 'wpa'
        ],
        'Web Application Attacks': [
            'xss', 'sql injection', 'csrf', 'directory traversal', 'code injection',
            'cross-site', 'owasp', 'web', 'http', 'session'
        ],
        'Malware & Threats': [
            'malware', 'virus', 'trojan', 'worm', 'ransomware', 'keylogger',
            'botnet', 'zero-day', 'exploit', 'vulnerability'
        ],
        'Security Controls': [
            'authentication', 'authorization', 'access control', 'firewall',
            'defense', 'protection', 'security policy', 'hardening'
        ],
        'Security Awareness': [
            'phishing', 'social engineering', 'training', 'awareness',
            'user education', 'incident', 'reporting'
        ]
    }
    
    categorized = defaultdict(list)
    
    for concept in concepts:
        concept_lower = concept.lower()
        assigned = False
        
        for category, keywords in categories.items():
            if any(keyword in concept_lower for keyword in keywords):
                categorized[category].append(concept)
                assigned = True
                break
        
        if not assigned:
            categorized['General Security'].append(concept)
    
    return dict(categorized)

def tidy_summary_file(file_path: Path) -> bool:
    """Clean up a single summary file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False
    
    # Extract concepts
    concept_pattern = r'- \*\*.*?\*\*:.*?(?=\n-|\n#|\n\n|\Z)'
    concepts = re.findall(concept_pattern, content, re.DOTALL)
    
    print(f"📄 {file_path.name}: Found {len(concepts)} raw concepts")
    
    # Clean and validate concepts
    valid_concepts = []
    for concept in concepts:
        clean_concept = clean_text(concept)
        if is_valid_concept(clean_concept):
            valid_concepts.append(clean_concept)
    
    print(f"✅ {len(valid_concepts)} valid concepts after cleaning")
    
    # Remove duplicates
    unique_concepts = deduplicate_concepts(valid_concepts)
    print(f"🔧 {len(unique_concepts)} unique concepts after deduplication")
    
    if len(unique_concepts) < 3:
        print(f"⚠️  Too few concepts remaining, skipping {file_path.name}")
        return False
    
    # Categorize and rebuild
    categorized = categorize_concepts(unique_concepts)
    
    # Build clean summary
    title = file_path.stem.replace('-summary', '').replace('_', ' ').replace('-', ' ').title()
    clean_content = [f"# {title} - Study Guide\n"]
    
    for category, items in categorized.items():
        if items:
            clean_content.append(f"## {category}")
            clean_content.extend(items)
            clean_content.append("")
    
    # Write cleaned file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(clean_content))
        print(f"✨ Tidied: {file_path.name} ({len(unique_concepts)} clean concepts)")
        return True
    except Exception as e:
        print(f"❌ Error writing {file_path}: {e}")
        return False

def main():
    output_dir = Path("output")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        # Tidy all summary files
        summary_files = list(output_dir.glob("*-summary.md"))
    elif len(sys.argv) > 1:
        # Tidy specific file
        target_file = Path(sys.argv[1])
        if not target_file.exists():
            target_file = output_dir / sys.argv[1]
        summary_files = [target_file] if target_file.exists() else []
    else:
        print("Usage: python tidy.py [--all | specific-summary.md]")
        return
    
    if not summary_files:
        print("❌ No summary files found")
        return
    
    print("🧹 Starting Summary Tidy Process")
    print("=" * 50)
    
    tidied_count = 0
    for file_path in summary_files:
        print(f"\n🔄 Processing: {file_path.name}")
        if tidy_summary_file(file_path):
            tidied_count += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Tidied {tidied_count}/{len(summary_files)} summary files")
    print(f"🎯 Ready for high-quality study sessions!")

if __name__ == "__main__":
    main() 