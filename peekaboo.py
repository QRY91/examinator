#!/usr/bin/env python3
"""
Peekaboo - Convert Q&A summaries to GitHub spoiler format
Creates collapsible sections perfect for sharing study materials
"""

import re
from pathlib import Path

def convert_qa_to_spoilers(content: str) -> str:
    """Convert Q&A format to GitHub spoiler format"""
    spoiler_lines = []
    
    # Split content into lines
    lines = content.split('\n')
    current_question = None
    current_answer = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('#'):
            if line.startswith('#'):
                spoiler_lines.append(line)
            continue
            
        # Detect Q: pattern
        if line.startswith('**Q:') and line.endswith('**'):
            # Save previous Q&A if exists
            if current_question and current_answer:
                answer_text = ' '.join(current_answer).strip()
                spoiler_block = f"""**{current_question}**
<details>
<summary>🤔 Click to reveal answer</summary>

{answer_text}

</details>
"""
                spoiler_lines.append(spoiler_block)
            
            # Start new question
            current_question = line[4:-2]  # Remove **Q: and **
            current_answer = []
            
        # Detect A: pattern  
        elif line.startswith('A:'):
            current_answer.append(line[2:].strip())
            
        # Continue answer on next line
        elif current_answer and line and not line.startswith('**Q:'):
            current_answer.append(line)
            
        # Other content (non Q&A)
        else:
            if not current_question:
                spoiler_lines.append(line)
    
    # Handle last Q&A
    if current_question and current_answer:
        answer_text = ' '.join(current_answer).strip()
        spoiler_block = f"""**{current_question}**
<details>
<summary>🤔 Click to reveal answer</summary>

{answer_text}

</details>
"""
        spoiler_lines.append(spoiler_block)
    
    return '\n'.join(spoiler_lines)

def main():
    """Convert all summaries to peekaboo format"""
    summaries_dir = Path("summaries")
    peekaboo_dir = Path("peekaboo")
    
    # Create peekaboo directory
    peekaboo_dir.mkdir(exist_ok=True)
    
    # Process all summary files
    summary_files = list(summaries_dir.glob("*.md"))
    
    if not summary_files:
        print("❌ No summary files found in summaries/ directory!")
        return
    
    print(f"🫣 Converting {len(summary_files)} summaries to peekaboo format...")
    
    converted = 0
    for file_path in summary_files:
        try:
            print(f"📄 Processing: {file_path.name}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert to spoiler format
            spoiler_content = convert_qa_to_spoilers(content)
            
            # Save to peekaboo directory
            output_file = peekaboo_dir / f"{file_path.stem}-peekaboo.md"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# 🫣 {file_path.stem.replace('-', ' ').title()} - Peekaboo Study Guide\n")
                f.write(f"*Generated from: {file_path.name}*\n\n")
                f.write("**Click the details to reveal answers! Perfect for GitHub study sessions.**\n\n")
                f.write("---\n\n")
                f.write(spoiler_content)
            
            print(f"✅ Saved: {output_file}")
            converted += 1
            
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
    
    print(f"\n🎉 Conversion complete!")
    print(f"✅ Converted: {converted} files")
    print(f"📁 Peekaboo files saved to: {peekaboo_dir}")
    print(f"🫣 Perfect for sharing on GitHub - answers hidden until clicked!")

if __name__ == "__main__":
    main() 