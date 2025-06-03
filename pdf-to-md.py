#!/usr/bin/env python3
"""
Quick PDF to Markdown converter
Usage: python pdf-to-md.py <input.pdf> [output.md]
"""

import sys
import re
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Installing PyMuPDF...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "PyMuPDF", "--user", "--break-system-packages"])
    import fitz

def clean_text(text):
    """Clean and format extracted text"""
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    
    # Try to detect headers (lines that are short and followed by content)
    lines = text.split('\n')
    cleaned_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            cleaned_lines.append('')
            continue
            
        # Detect potential headers (short lines, often capitalized)
        if (len(line) < 80 and 
            line.isupper() or 
            (len(line.split()) <= 6 and any(c.isupper() for c in line))):
            cleaned_lines.append(f'## {line}')
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def pdf_to_markdown(pdf_path, output_path=None):
    """Convert PDF to Markdown"""
    pdf_path = Path(pdf_path)
    
    if not output_path:
        output_path = pdf_path.with_suffix('.md')
    
    try:
        # Open PDF
        doc = fitz.open(pdf_path)
        
        markdown_content = [f"# {pdf_path.stem}\n"]
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Extract text
            text = page.get_text()
            
            if text.strip():
                markdown_content.append(f"\n## Page {page_num + 1}\n")
                cleaned_text = clean_text(text)
                markdown_content.append(cleaned_text)
        
        doc.close()
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        
        print(f"✅ Converted: {pdf_path} → {output_path}")
        print(f"📄 {len(doc)} pages processed")
        
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf-to-md.py <input.pdf> [output.md]")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(pdf_file).exists():
        print(f"❌ File not found: {pdf_file}")
        sys.exit(1)
    
    pdf_to_markdown(pdf_file, output_file)

if __name__ == "__main__":
    main() 