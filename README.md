# 🎯 Examinator - Offline Study Companion

**3 commands. No internet. Maximum drilling.**  
*Study security concepts with ADHD-friendly spaced repetition*

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

Like [uroboro](https://urobo.eu/) - **simplicity over complexity**. Stressed students on buses need tools that **just work**.

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