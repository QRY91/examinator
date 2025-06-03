# 🚀 Examinator Setup Guide

## Quick Start (Recommended)

```bash
# Clone and setup
git clone <your-repo>
cd examinator

# Install dependencies  
pip install -r requirements.txt

# Generate flashcards from existing summaries
python3 convert_qa_to_flashcards.py

# Start studying!
python3 flashcards.py
```

## Directory Structure

```
examinator/
├── flashcards/          # 🃏 Clean flashcards for the app
├── summaries/           # 📚 Study summaries (markdown viewing)
├── output/              # 🔄 Generated questions/scenarios
├── input/               # 📄 Source materials (PDFs, etc)
└── demos/               # 🎯 Example files
```

## Encoding Issues? 

If you see weird characters or encoding errors:

### Option 1: Clean Install (Recommended)
```bash
pip install -r requirements.txt
python3 convert_qa_to_flashcards.py  # Regenerate with UTF-8
```

### Option 2: Docker (Nuclear Option)
```bash
# Coming soon if needed - probably overkill for this
```

### Option 3: Manual Fix
```bash
# Check your locale
locale

# Should show UTF-8. If not:
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

## Generate Spicy Questions

```bash
# Test LLM connection first
python3 generate-practice-questions.py --test

# Generate flashcards from specific topic
python3 generate-practice-questions.py --flashcards -f security-fundamentals-clean-demo.md

# Include spoiler format for sharing
python3 generate-practice-questions.py --flashcards --spoilers -f filename.md

# Generate multiple choice + scenarios
python3 generate-practice-questions.py -f filename.md -t multiple_choice scenarios
```

## Troubleshooting

**No cards loaded?**
- Check `flashcards/` directory has `.md` files
- Run `python3 convert_qa_to_flashcards.py` to regenerate

**LLM not working?**
- Install Ollama: https://ollama.ai
- Start service: `ollama serve`  
- Install model: `ollama pull mistral:latest`

**Encoding errors?**
- Use Python 3.8+ with UTF-8 support
- Install dependencies: `pip install -r requirements.txt`
- Regenerate flashcards with UTF-8: `python3 convert_qa_to_flashcards.py`

## Clean Workflow

1. **Study materials** → `summaries/` (manual Q&A format)
2. **Generate flashcards** → `flashcards/` (app-compatible) 
3. **Generate questions** → `output/` (practice scenarios)
4. **Use apps**: `python3 flashcards.py` for drilling

No cross-contamination between directories! 🧹 