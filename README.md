# 🎯 Examinator - Offline Study Companion

**3 commands. No internet. Maximum drilling.**  
*Study security concepts with ADHD-friendly spaced repetition*

## 🤖 AI Collaboration Transparency

This project documentation and development has been enhanced through systematic AI collaboration following QRY Labs methodology:

- **Human-Centered Development**: All core functionality, architecture decisions, and strategic direction remain human-controlled
- **AI-Enhanced Documentation**: AI assistants help improve documentation quality and systematic presentation
- **Transparent Attribution**: AI collaboration is acknowledged openly as part of QRY's commitment to ethical technology use
- **Local AI Integration**: Examinator uses local AI (Ollama) for flashcard generation while maintaining complete privacy
- **Systematic Methodology**: AI collaboration follows structured procedures documented in `/ai/` directory

**Core Principle**: AI enhances human capability rather than replacing human judgment. Examinator exemplifies this by using local AI to generate study content while keeping all learning and knowledge assessment under human control.

## 🔗 QRY Ecosystem Integration (Experimental)

**examinator** now supports experimental integration with the QRY ecosystem database, enabling automatic flashcard generation from development work while maintaining complete independence.

**Ecosystem Features:**
- **Automatic Discovery**: Detects shared QRY ecosystem database (`~/.local/share/qry/ecosystem.sqlite`)
- **Smart Flashcard Generation**: Creates study materials from uroboro captures automatically
- **Context-Aware Learning**: Uses wherewasi context to improve flashcard categorization
- **Cross-Tool Intelligence**: Receives notifications when new content is captured
- **Graceful Fallback**: Works normally with local database when ecosystem unavailable

**Status Indicators:**
```bash
python3 ecosystem_integration_example.py status
# Ecosystem mode: "Ecosystem mode: ENABLED"
# Local mode:     "Ecosystem mode: DISABLED"
```

**Ecosystem Commands:**
```bash
python3 ecosystem_integration_example.py sync            # Process captures from uroboro
python3 ecosystem_integration_example.py generate --project myproject  # Generate from captures
python3 ecosystem_integration_example.py study --project myproject     # Study with context
python3 ecosystem_integration_example.py --local        # Force local database mode
```

**Integration Status**: Experimental implementation - automatically generates study materials from development activity when ecosystem tools work together, functions independently when not.

## 📱 Quick Guide (Mobile-Optimized Text)

*Cramped bus seat? Phone screen? These instructions are your lifeline.*

### 🚀 Installation
```bash
# 1. Clone the repo
git clone https://github.com/QRY91/examinator.git
cd examinator

# 2. Install dependencies (once)
pip install -r requirements.txt

# 3. Generate initial flashcards
python3 convert.py
```

### 🎮 3-Command Workflow  
```bash
# 1. STUDY (main command - 186 cards ready)
python3 flashcards.py

# 2. GENERATE (create new cards with local LLM)
python3 generate.py --flashcards -f your-notes.md

# 3. CONVERT (turn Q&A notes into flashcards)
python3 convert.py
```

### 🧠 Smart Flashcard App Controls
- **SPACE**: Show answer
- **G**: Got it (mark correct)
- **N**: Need practice (mark wrong)
- **S**: Skip card
- **Q**: Quit & save progress

*Optimized for mobile viewing - bigger fonts in app, clear instructions in docs*

---

## 📚 For Classmates: Just Read (No Install Required)

**Don't want to fiddle with the app?** Just browse these GitHub pages with **spoiler-enabled study materials**:

### 🔥 Ready-to-Study Materials
- **[Security Fundamentals](summaries/security-fundamentals-clean-demo.md)** - CIA triad, crypto basics, authentication
- **[Web Security & XSS](summaries/web-security-xss-exam-guide.md)** - XSS types, SQL injection, CSP  
- **[Privacy & Anonymization](summaries/privacy-anonymization-exam-guide.md)** - K-anonymity, differential privacy
- **[Incident Response](summaries/incident-response-social-engineering-exam-guide.md)** - IR phases, social engineering
- **[Malware & Deception](summaries/ps_6_malware_and_deception-summary.md)** - Attack vectors, defense strategies
- **[Advanced Attacks](summaries/ps_7_attacks-(2)-summary.md)** - Advanced persistent threats, analysis
- **[Privacy Deep Dive](summaries/ps_9_privacy_-summary.md)** - GDPR, privacy-preserving techniques

**Click the spoiler arrows (▶️) to reveal answers.** Perfect for group study sessions!

---

## 🚀 Panic Mode Quick Start

```bash
# 1. STUDY - Start drilling immediately with existing cards
python3 flashcards.py

# 2. GENERATE - Create more flashcards from study materials  
python3 generate.py --flashcards -f filename.md

# 3. CONVERT - Turn summaries into flashcards
python3 convert.py
```

**That's it.** No wifi dongle, no 5G, no GPT needed.

---

## 🎮 The 3-Command Philosophy

Like [uroboro](https://uroboro.dev/) - **simplicity over complexity**. Stressed students on buses need tools that **just work**.

### 📱 Command 1: `flashcards.py`
**Your main study app**
- 186 ready-to-go security flashcards
- Smart spaced repetition (focuses on hard cards)
- ADHD-friendly (no easy-card traps)
- Works 100% offline

```bash
python3 flashcards.py
# Loads cards from flashcards/ and summaries/
# Press G (got it), N (need practice), S (skip)
# Zenburn theme - easy on tired eyes
```

### ⚡ Command 2: `generate.py`
**Create new flashcards with local LLM**
- Uses Ollama + Mistral (free, private, offline)
- Generates multiple choice, scenarios, flashcards
- Spoiler format for sharing with classmates

```bash
# Quick flashcard generation
python3 generate.py --flashcards -f security-file.md

# With spoiler format (shareable)
python3 generate.py --flashcards --spoilers -f filename.md

# Full question suite
python3 generate.py -f filename.md
```

### 🔄 Command 3: `convert.py`
**Turn your study notes into drilling cards**
- Converts Q&A summaries → flashcard format
- UTF-8 safe (fixes encoding issues)
- Batch processes all summaries

```bash
python3 convert.py
# Converts everything in summaries/ → flashcards/
```

---

## 📁 Simple Directory Structure

```
examinator/
├── flashcards/     # 🃏 Clean cards (app reads here)
├── summaries/      # 📚 Your Q&A study notes  
├── output/         # 🔄 Generated practice questions
└── input/          # 📄 Source PDFs/materials
```

**No cross-contamination.** Each directory has one purpose.

---

## 🛠️ One-Time Setup

```bash
# Get the code
git clone https://github.com/QRY91/examinator.git
cd examinator

# Install once
pip install -r requirements.txt

# Generate initial flashcards
python3 convert.py

# Start studying
python3 flashcards.py
```

**For LLM questions** (optional):
```bash
# Install Ollama once
curl -fsSL https://ollama.ai/install.sh | sh

# Pull model once  
ollama pull mistral:latest

# Test connection
python3 generate.py --test
```

---

## 🚨 Panic Mode Troubleshooting

**Nothing works?**
```bash
pip install -r requirements.txt
python3 convert.py
```

**No cards found?**
- Check `flashcards/` directory exists
- Run `python3 convert.py`

**Encoding errors?**
- Files are now UTF-8 safe
- Run converter to fix: `python3 convert.py`

**LLM not working?**
- App works without LLM
- Just use `python3 flashcards.py` with existing 186 cards

---

## 🎯 What You Get

- **186 clean security flashcards** (CIA triad, crypto, attacks, privacy, etc.)
- **Smart spaced repetition** (avoids easy-card traps)
- **Local LLM generation** (free, private, no API costs)
- **Offline first** (works on buses, planes, cafes with broken wifi)
- **ADHD-friendly** (focuses on hard concepts, not busy work)

---

## 🧠 Study Methods

1. **Daily drilling**: `python3 flashcards.py` (15-30 min sessions)
2. **Topic deep-dive**: Generate targeted cards for weak areas
3. **Group study**: Share spoiler-format cards with classmates
4. **Exam prep**: Use multiple choice + scenario questions

---

## 🌟 Design Principles

**Inspired by uroboro's simplicity:**

- **3 commands maximum** - No complex workflows
- **Offline first** - Works without internet
- **Panic-proof** - Clear errors, simple fixes
- **Student-focused** - Built for stressed learners
- **No BS** - Does one thing well

**Just works.** Even at 3am before an exam. Even on a bus with no wifi. Even when you're stressed and can't think straight.

Start drilling: `python3 flashcards.py` 🎯

---

## 🛣️ Roadmap (Future Ideas)

- **SQLite Integration**: Enhance flashcard study with persistent progress tracking (review dates, intervals, ease factors) for an even smarter, more resilient spaced repetition system. Could also log generation/conversion history.
- **Advanced Content Parsing**: More robust extraction from diverse PDF layouts or other document types.
- **Community Flashcard Decks**: A way to share and import pre-made flashcard decks on specific security topics. 

---

## 🌐 Wiki Deployment (Collaborative Study)

**Turn your study materials into a collaborative knowledge base!**

### 📤 5-Command Workflow

```bash
# 1. STUDY - Interactive flashcards
python3 flashcards.py

# 2. GENERATE - LLM question creation  
python3 generate.py --flashcards -f filename.md

# 3. CONVERT - Notes → flashcards
python3 convert.py

# 4. INGEST - PDFs → Q&A summaries
python3 ingest.py -f filename.pdf --llm

# 5. WIKI - Summaries → collaborative format
python3 wiki-export.py
```

### 🚀 Wiki Setup & Deployment

**1. Generate Wiki Content**
```bash
# Convert all summaries to wiki format
python3 wiki-export.py
# Creates 20+ organized wiki pages in wiki/ directory
```

**2. Enable GitHub Wiki**
- Go to your repo **Settings** → **Features**  
- Check ✅ **Wikis**

**3. Deploy to GitHub**
```bash
# Clone the wiki repository
git clone https://github.com/YOUR_USERNAME/examinator.wiki.git

# Copy generated content
cp wiki/* examinator.wiki/

# Deploy
cd examinator.wiki
git add .
git commit -m "📚 Deploy comprehensive study wiki"
git push origin master
```

**4. Share with Classmates**
- Wiki URL: `https://github.com/YOUR_USERNAME/examinator/wiki`
- **Organized by topic** - 6 study categories
- **Collapsible Q&A** - Click 🤔 to reveal answers
- **Collaborative editing** - Everyone can contribute

### 📊 What You Get

**Wiki Features:**
- **20+ topic pages** with comprehensive Q&A
- **6 organized categories** (Security Fundamentals, Cryptography, etc.)
- **Collapsible spoilers** for progressive revelation  
- **Mobile-friendly** for study-on-the-go
- **Collaborative editing** for group knowledge building

**Local Tools Remain:**
- **Original summaries** preserved in `summaries/`
- **Flashcard app** works offline with `flashcards.py`
- **LLM generation** continues with `generate.py`

This creates a **dual-mode study system**: 
- **Individual**: Offline flashcard drilling  
- **Collaborative**: Online wiki knowledge sharing

--- 