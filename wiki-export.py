#!/usr/bin/env python3
"""
Wiki Export - Convert Q&A summaries to GitHub wiki format
Creates wiki-ready copies while preserving original files
"""

import re
from pathlib import Path
from typing import Dict, List

def sanitize_wiki_title(title: str) -> str:
    """Convert title to wiki-friendly format"""
    # Remove special characters, keep spaces
    clean = re.sub(r'[^\w\s-]', '', title)
    # Replace multiple spaces with single space
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip()

def convert_to_wiki_format(content: str, title: str) -> str:
    """Convert Q&A summary to GitHub wiki format"""
    
    # Extract Q&A pairs
    qa_pairs = []
    lines = content.split('\n')
    current_q = None
    current_a = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and original headers
        if not line or line.startswith('# 🎯') or line.startswith('*Generated from:'):
            continue
            
        # Detect questions
        if line.startswith('**Q:') and line.endswith('**'):
            # Save previous Q&A if exists
            if current_q:
                qa_pairs.append((current_q, '\n'.join(current_a).strip()))
            
            # Start new question
            current_q = line[4:-2].strip()  # Remove **Q: and **
            current_a = []
            
        # Detect answers
        elif line.startswith('A:'):
            current_a.append(line[2:].strip())  # Remove A: prefix
            
        # Continue multi-line answers
        elif current_q and line and not line.startswith('**'):
            current_a.append(line)
    
    # Don't forget the last Q&A pair
    if current_q:
        qa_pairs.append((current_q, '\n'.join(current_a).strip()))
    
    # Build wiki content
    wiki_content = []
    wiki_content.append(f"# {title}")
    wiki_content.append("")
    wiki_content.append("## 📚 Study Questions & Answers")
    wiki_content.append("")
    
    for i, (question, answer) in enumerate(qa_pairs, 1):
        # Use collapsible sections for each Q&A
        wiki_content.append(f"### {i}. {question}")
        wiki_content.append("")
        wiki_content.append("<details>")
        wiki_content.append("<summary>🤔 Click to reveal answer</summary>")
        wiki_content.append("")
        wiki_content.append(answer)
        wiki_content.append("")
        wiki_content.append("</details>")
        wiki_content.append("")
    
    # Add navigation footer
    wiki_content.append("---")
    wiki_content.append("")
    wiki_content.append("📖 **[Return to Wiki Home](Home)**")
    wiki_content.append("")
    wiki_content.append("🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**")
    
    return '\n'.join(wiki_content)

def categorize_summaries() -> Dict[str, List[Path]]:
    """Organize summaries by topic category"""
    
    categories = {
        "Security Fundamentals": [],
        "Cryptography": [],
        "Data Protection": [],
        "Threats & Defense": [],
        "Privacy & Compliance": [],
        "Exam Preparation": []
    }
    
    summaries_dir = Path("summaries")
    
    for summary_file in summaries_dir.glob("*.md"):
        filename = summary_file.name.lower()
        
        # Categorize based on filename patterns
        if any(pattern in filename for pattern in ['ps-1-security', 'ps-2-cia', 'ps-2-security']):
            categories["Security Fundamentals"].append(summary_file)
        elif 'ps-3-' in filename:
            categories["Cryptography"].append(summary_file)
        elif any(pattern in filename for pattern in ['ps-4-', 'ps-5-']):
            categories["Data Protection"].append(summary_file)
        elif any(pattern in filename for pattern in ['ps-6-', 'ps-7-', 'ps-8-']):
            categories["Threats & Defense"].append(summary_file)
        elif 'ps-9-' in filename:
            categories["Privacy & Compliance"].append(summary_file)
        elif any(pattern in filename for pattern in ['exam', 'practice']):
            categories["Exam Preparation"].append(summary_file)
        else:
            # Default category for uncategorized files
            categories["Security Fundamentals"].append(summary_file)
    
    return categories

def create_wiki_home(categories: Dict[str, List[Path]]) -> str:
    """Create wiki home page with navigation"""
    
    home_content = []
    home_content.append("# 🎯 Examinator Wiki - Cybersecurity Study Guide")
    home_content.append("")
    home_content.append("Welcome to the collaborative cybersecurity knowledge base! This wiki contains comprehensive Q&A study materials covering all major security topics.")
    home_content.append("")
    home_content.append("## 📚 Study Topics")
    home_content.append("")
    
    for category, files in categories.items():
        if files:  # Only show categories that have content
            home_content.append(f"### {category}")
            home_content.append("")
            
            for file_path in sorted(files):
                # Create wiki page title from filename
                title = file_path.stem.replace('-', ' ').title()
                title = re.sub(r'\bPs\b', 'PS', title)  # Fix PS capitalization
                
                # Create wiki link
                wiki_link = file_path.stem.replace('-', '-')
                home_content.append(f"- [[{title}|{wiki_link}]]")
            
            home_content.append("")
    
    home_content.append("## 🚀 How to Use This Wiki")
    home_content.append("")
    home_content.append("1. **Browse by topic** - Use the categories above to find relevant material")
    home_content.append("2. **Click question headings** - Each page has numbered questions")
    home_content.append("3. **Reveal answers** - Click the 🤔 spoiler sections to see answers")
    home_content.append("4. **Contribute** - Edit pages to add your own insights and questions")
    home_content.append("")
    home_content.append("## 🛠️ Local Study Tools")
    home_content.append("")
    home_content.append("Want to study offline? Check out the [Examinator repository](https://github.com/QRY91/examinator) for:")
    home_content.append("")
    home_content.append("- 🃏 **Interactive flashcard app** with spaced repetition")
    home_content.append("- 🤖 **Local AI question generation** (completely offline)")
    home_content.append("- 📱 **Mobile-friendly** study tools")
    home_content.append("")
    home_content.append("---")
    home_content.append("")
    home_content.append("*This wiki is automatically generated from the Examinator study materials. Last updated: Generated from comprehensive PDF curriculum.*")
    
    return '\n'.join(home_content)

def main():
    """Main wiki export function"""
    
    print("🌐 WIKI EXPORT")
    print("=" * 40)
    
    # Create wiki directory
    wiki_dir = Path("wiki")
    wiki_dir.mkdir(exist_ok=True)
    
    # Categorize summaries
    categories = categorize_summaries()
    
    print(f"📁 Found summaries in {len(categories)} categories")
    
    # Convert each summary to wiki format
    total_pages = 0
    for category, files in categories.items():
        if files:
            print(f"\n📚 {category}: {len(files)} pages")
            
            for file_path in files:
                try:
                    # Read original summary
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Create wiki title
                    title = file_path.stem.replace('-', ' ').title()
                    title = re.sub(r'\bPs\b', 'PS', title)
                    
                    # Convert to wiki format
                    wiki_content = convert_to_wiki_format(content, title)
                    
                    # Save wiki page
                    wiki_filename = f"{file_path.stem}.md"
                    wiki_path = wiki_dir / wiki_filename
                    
                    with open(wiki_path, 'w', encoding='utf-8') as f:
                        f.write(wiki_content)
                    
                    print(f"  ✅ {title}")
                    total_pages += 1
                    
                except Exception as e:
                    print(f"  ❌ Error processing {file_path.name}: {e}")
    
    # Create home page
    home_content = create_wiki_home(categories)
    home_path = wiki_dir / "Home.md"
    
    with open(home_path, 'w', encoding='utf-8') as f:
        f.write(home_content)
    
    print(f"\n🏠 Created wiki home page")
    
    print(f"\n🎉 Wiki export complete!")
    print(f"✅ Generated: {total_pages} topic pages + 1 home page")
    print(f"📁 Location: wiki/ directory")
    print(f"🌐 Ready for GitHub wiki upload!")
    
    print(f"\n📋 Next steps:")
    print(f"1. Enable wiki in GitHub repo settings")
    print(f"2. Clone wiki: git clone https://github.com/QRY91/examinator.wiki.git")
    print(f"3. Copy files from wiki/ directory to cloned wiki repo")
    print(f"4. Git add, commit, push to publish")

if __name__ == "__main__":
    main() 