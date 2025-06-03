#!/usr/bin/env python3
"""
Smart PDF Ingestion - Extract and process study materials
Uses PyMuPDF for extraction + optional local LLM for Q&A generation
"""

import sys
import re
import subprocess
from pathlib import Path
from typing import Optional, List

try:
    import fitz  # PyMuPDF
except ImportError:
    print("📦 Installing PyMuPDF...")
    subprocess.run([sys.executable, "-m", "pip", "install", "PyMuPDF", "--user", "--break-system-packages"])
    import fitz

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to kebab-case"""
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    
    # Convert to lowercase and clean
    clean = stem.lower()
    clean = re.sub(r'[_\s]+', '-', clean)
    clean = re.sub(r'[()[\]{}]', '', clean)
    clean = re.sub(r'[^\w\-]', '-', clean)
    clean = re.sub(r'-+', '-', clean)
    clean = clean.strip('-')
    
    return f"{clean}{suffix}"

def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract clean text from PDF"""
    try:
        doc = fitz.open(pdf_path)
        all_text = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            
            if text.strip():
                # Clean the text
                text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)  # Remove excessive newlines
                text = re.sub(r' +', ' ', text)  # Remove excessive spaces
                text = re.sub(r'\n +', '\n', text)  # Remove leading spaces on lines
                all_text.append(text.strip())
        
        doc.close()
        return '\n\n'.join(all_text)
        
    except Exception as e:
        print(f"❌ Error extracting from {pdf_path}: {e}")
        return ""

def test_ollama_connection() -> bool:
    """Test if Ollama is available"""
    try:
        result = subprocess.run([
            "ollama", "run", "mistral:latest"
        ], input="Hello", capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except:
        return False

def generate_qa_summary(content: str, topic_name: str) -> str:
    """Generate Q&A summary using local LLM"""
    
    prompt = f"""You are an expert educator creating study materials from cybersecurity content.

Based on this material about "{topic_name}", create a comprehensive Q&A study guide.

CONTENT:
{content[:4000]}  # Limit content to avoid token limits

REQUIREMENTS:
1. Extract the most important concepts, terms, and procedures
2. Create clear, specific questions that test understanding
3. Provide complete, accurate answers
4. Focus on exam-relevant material
5. Include both conceptual and practical questions

FORMAT each Q&A as:
**Q: [Clear, specific question]**
A: [Complete answer with key details]

Generate 15-20 high-quality Q&A pairs covering the main topics in this material."""

    try:
        print("🧠 Generating Q&A summary with local LLM...")
        result = subprocess.run([
            "ollama", "run", "mistral:latest"
        ], input=prompt, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"❌ LLM error: {result.stderr}")
            return ""
            
    except subprocess.TimeoutExpired:
        print("⏰ LLM timeout - content too long")
        return ""
    except Exception as e:
        print(f"💥 LLM error: {e}")
        return ""

def create_basic_summary(content: str, topic_name: str) -> str:
    """Create basic markdown summary without LLM"""
    
    # Try to extract key sections
    lines = content.split('\n')
    sections = []
    current_section = []
    
    for line in lines:
        line = line.strip()
        
        # Detect potential headers
        if (len(line) < 100 and 
            (line.isupper() or 
             any(keyword in line.lower() for keyword in ['chapter', 'section', 'introduction', 'overview']))):
            if current_section:
                sections.append('\n'.join(current_section))
                current_section = []
            sections.append(f"## {line}")
        else:
            if line:
                current_section.append(line)
    
    if current_section:
        sections.append('\n'.join(current_section))
    
    return '\n\n'.join(sections)

def process_pdf(pdf_path: Path, use_llm: bool = False) -> bool:
    """Process a single PDF file"""
    
    print(f"\n📄 Processing: {pdf_path.name}")
    
    # Extract text
    content = extract_text_from_pdf(pdf_path)
    if not content:
        print("❌ No text extracted")
        return False
    
    print(f"📝 Extracted {len(content)} characters")
    
    # Create sanitized filename
    sanitized_name = sanitize_filename(pdf_path.name)
    output_path = Path("summaries") / sanitized_name.replace('.pdf', '-summary.md')
    
    # Ensure summaries directory exists
    Path("summaries").mkdir(exist_ok=True)
    
    # Generate summary
    topic_name = pdf_path.stem.replace('_', ' ').replace('-', ' ')
    
    if use_llm and test_ollama_connection():
        print("🤖 Using local LLM for Q&A generation...")
        summary_content = generate_qa_summary(content, topic_name)
        
        if summary_content:
            final_content = f"# 🎯 {topic_name.title()} - Study Guide\n*Generated from: {pdf_path.name}*\n\n{summary_content}"
        else:
            print("⚠️ LLM failed, falling back to basic extraction...")
            basic_summary = create_basic_summary(content, topic_name)
            final_content = f"# 📄 {topic_name.title()} - Basic Summary\n*Extracted from: {pdf_path.name}*\n\n{basic_summary}"
    else:
        if use_llm:
            print("⚠️ LLM not available, using basic extraction...")
        print("📝 Creating basic summary...")
        basic_summary = create_basic_summary(content, topic_name)
        final_content = f"# 📄 {topic_name.title()} - Basic Summary\n*Extracted from: {pdf_path.name}*\n\n{basic_summary}"
    
    # Save summary
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"✅ Saved: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error saving summary: {e}")
        return False

def main():
    """Main ingestion function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🔄 Ingest PDFs and create study summaries")
    parser.add_argument("--file", "-f", help="Process specific PDF file")
    parser.add_argument("--all", action="store_true", help="Process all PDFs in input/ directory")
    parser.add_argument("--llm", action="store_true", help="Use local LLM for Q&A generation")
    parser.add_argument("--list", action="store_true", help="List available PDF files")
    
    args = parser.parse_args()
    
    input_dir = Path("input")
    
    if args.list:
        pdf_files = list(input_dir.glob("*.pdf"))
        print(f"📁 Found {len(pdf_files)} PDF files in input/:")
        for pdf in pdf_files:
            print(f"  📄 {pdf.name}")
        return
    
    if args.file:
        # Process specific file
        pdf_path = Path(args.file)
        if not pdf_path.exists():
            pdf_path = input_dir / args.file
        
        if not pdf_path.exists():
            print(f"❌ File not found: {args.file}")
            return
        
        if not pdf_path.suffix.lower() == '.pdf':
            print(f"❌ Not a PDF file: {args.file}")
            return
        
        print("🔄 SMART PDF INGESTION")
        print("=" * 40)
        
        success = process_pdf(pdf_path, args.llm)
        if success:
            print("\n🎉 Ingestion complete!")
            if not args.llm:
                print("💡 Tip: Use --llm for Q&A generation with local AI")
        
    elif args.all:
        # Process all PDFs
        pdf_files = list(input_dir.glob("*.pdf"))
        
        if not pdf_files:
            print("❌ No PDF files found in input/ directory")
            return
        
        print("🔄 BATCH PDF INGESTION")
        print("=" * 40)
        print(f"📁 Found {len(pdf_files)} PDF files")
        
        if args.llm:
            if test_ollama_connection():
                print("🤖 Using local LLM for Q&A generation")
            else:
                print("⚠️ LLM not available, using basic extraction")
        
        successful = 0
        for pdf_path in pdf_files:
            if process_pdf(pdf_path, args.llm):
                successful += 1
        
        print(f"\n🎉 Batch ingestion complete!")
        print(f"✅ Processed: {successful}/{len(pdf_files)} files")
        print(f"📁 Summaries saved to: summaries/")
        
    else:
        print("Usage:")
        print("  python3 ingest.py --list                    # List available PDFs")
        print("  python3 ingest.py -f filename.pdf          # Process single PDF")
        print("  python3 ingest.py -f filename.pdf --llm    # Process with Q&A generation")
        print("  python3 ingest.py --all                    # Process all PDFs")
        print("  python3 ingest.py --all --llm              # Process all with Q&A generation")

if __name__ == "__main__":
    main() 