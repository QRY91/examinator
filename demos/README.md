# 🎬 Demo GIFs for Zoomers

Quick visual guides showing how to use the security exam prep toolkit.

## 📼 Generated Demos

### 🚀 Installation Demo
![Installation Demo](install.gif)

Shows the complete setup process - installing packages, making scripts executable, and verifying everything works.

### 📚 Basic Usage Demo  
![Basic Usage Demo](basic-usage.gif)

Demonstrates the full CLI pipeline: ingest → tidy → refine → generate-questions workflow.

### 🧠 Flashcard App Demo
![Flashcard App Demo](flashcards.gif)

Interactive study tool with ADHD-friendly features and navigation controls.

## 🚀 Generate Your Own GIFs

Install VHS (terminal recorder):
```bash
# On Linux/macOS
curl -fsSL https://github.com/charmbracelet/vhs/releases/latest/download/install.sh | bash

# Or with Go
go install github.com/charmbracelet/vhs@latest
```

Generate all demos:
```bash
cd demos/
vhs 01-installation.tape      # Creates install.gif
vhs 02-basic-usage.tape       # Creates basic-usage.gif  
vhs 03-flashcards.tape        # Creates flashcards.gif
```

## 📼 What Each Demo Shows

### `install.gif` - Installation Demo
- Installing Python packages with pip3
- Making scripts executable  
- Verifying installation worked

### `basic-usage.gif` - Basic CLI Workflow
- Processing study materials with the pipeline
- Running ingest → tidy → refine → generate-questions
- Checking generated output files

### `flashcards.gif` - Flashcard App Demo  
- Launching the interactive study tool
- Basic navigation and controls
- ADHD-friendly features (easy/hard marking)

## 💡 Usage Tips

- Share these GIFs in your class Discord/Slack
- Post on social media with exam prep hashtags
- Embed in course wikis or study group resources
- Send directly to classmates who need CLI help

Perfect for zoomers who prefer visual learning over reading docs! 📱✨ 