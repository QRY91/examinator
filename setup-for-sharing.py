#!/usr/bin/env python3
"""
Setup script for sharing the Security Exam Prep Toolkit
Initializes git repository and prepares for distribution

Usage: python3 setup-for-sharing.py
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=cwd)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def create_gitignore():
    """Create a .gitignore file for the repository"""
    gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
venv/
env/

# Temporary files
temp/
tmp/
*.tmp
.DS_Store
Thumbs.db

# Personal study materials (keep these local)
personal-notes/
my-additions/

# Large files that should be regenerated
output/temp/

# IDE files
.vscode/
.idea/
*.swp
*.swo

# System files
.DS_Store
*.log
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created .gitignore")

def create_license():
    """Create an MIT license file"""
    license_content = """MIT License

Copyright (c) 2025 Security Exam Prep Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    with open('LICENSE', 'w') as f:
        f.write(license_content)
    
    print("✅ Created LICENSE file")

def create_requirements():
    """Create a requirements.txt file"""
    requirements_content = """# Core dependencies for the Security Exam Prep Toolkit
textual>=0.40.0
PyMuPDF>=1.23.0

# Optional dependencies for enhanced functionality
rich>=13.0.0
pathlib2>=2.3.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    
    print("✅ Created requirements.txt")

def create_install_script():
    """Create an easy installation script"""
    install_script = """#!/bin/bash
# Easy installation script for Security Exam Prep Toolkit

echo "🎯 Setting up Security Exam Prep Toolkit..."
echo "============================================"

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oP '\\d+\\.\\d+')
echo "📍 Python version: $python_version"

# Install core dependencies
echo "📦 Installing core dependencies..."
pip3 install textual --user --break-system-packages

# Install optional PDF support
echo "📄 Installing PDF support..."
pip3 install PyMuPDF --user --break-system-packages

# Create input directory if it doesn't exist
mkdir -p input
echo "📁 Created input directory"

# Make scripts executable
chmod +x *.py
echo "🔧 Made scripts executable"

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Quick Start:"
echo "1. Add your course materials to the input/ directory"
echo "2. Run: python3 ingest.py"
echo "3. Run: python3 tidy.py --all"
echo "4. Run: python3 refine.py"
echo "5. Run: python3 flashcards.py"
echo ""
echo "📖 See README.md for detailed instructions"
echo "🎉 Good luck with your exam!"
"""
    
    with open('install.sh', 'w') as f:
        f.write(install_script)
    
    # Make the script executable
    success, _, _ = run_command("chmod +x install.sh")
    if success:
        print("✅ Created install.sh script")
    else:
        print("⚠️  Created install.sh (permissions may need manual adjustment)")

def setup_git_repository():
    """Initialize and configure git repository"""
    print("\n🔧 Setting up Git repository...")
    
    # Check if git is installed
    success, _, _ = run_command("git --version")
    if not success:
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    # Initialize repository if not already initialized
    if not Path('.git').exists():
        success, output, error = run_command("git init")
        if success:
            print("✅ Initialized git repository")
        else:
            print(f"❌ Failed to initialize git: {error}")
            return False
    else:
        print("✅ Git repository already exists")
    
    # Add all files
    success, _, error = run_command("git add .")
    if success:
        print("✅ Added files to git")
    else:
        print(f"⚠️  Warning adding files: {error}")
    
    # Initial commit
    commit_message = "Initial commit: Security Exam Prep Toolkit"
    success, _, error = run_command(f'git commit -m "{commit_message}"')
    if success:
        print("✅ Created initial commit")
    elif "nothing to commit" in error:
        print("✅ Repository is up to date")
    else:
        print(f"⚠️  Commit warning: {error}")
    
    return True

def create_sharing_instructions():
    """Create instructions for sharing with classmates"""
    instructions = """# 🤝 Sharing Instructions

## For the Original Creator

### Option 1: GitHub (Recommended)
1. Create a new repository on GitHub
2. Follow GitHub's instructions to add the remote:
   ```bash
   git remote add origin https://github.com/yourusername/security-exam-prep.git
   git branch -M main
   git push -u origin main
   ```

### Option 2: Zip File Distribution
```bash
# Create a zip file for sharing
zip -r security-exam-prep.zip . -x "*.git*" "temp/*" "__pycache__/*"
```

## For Classmates

### Getting Started (GitHub)
```bash
git clone https://github.com/username/security-exam-prep.git
cd security-exam-prep
./install.sh  # or bash install.sh
```

### Getting Started (Zip File)
1. Extract the zip file
2. Open terminal in the extracted directory
3. Run: `./install.sh` (or `bash install.sh`)

### Adding Your Materials
1. Place your PDFs and markdown files in `input/`
2. Run the processing pipeline:
   ```bash
   python3 ingest.py
   python3 tidy.py --all
   python3 refine.py
   ```

### Sharing Improvements
1. Make your changes
2. Commit them: `git commit -am "Description of changes"`
3. Push or share the updated files

## 🎯 What to Share
- ✅ All Python scripts and tools
- ✅ README.md and documentation
- ✅ Example output files (optional)
- ❌ Personal input materials (copyright)
- ❌ Personal notes or modifications

## 🔧 Troubleshooting for Classmates
Common issues and solutions are documented in README.md

## 🎉 Success!
Once set up, classmates can benefit from the same automated exam prep workflow you've built!
"""
    
    with open('SHARING.md', 'w') as f:
        f.write(instructions)
    
    print("✅ Created sharing instructions (SHARING.md)")

def main():
    print("🎯 Security Exam Prep Toolkit - Setup for Sharing")
    print("=" * 60)
    
    # Create necessary files
    create_gitignore()
    create_license() 
    create_requirements()
    create_install_script()
    
    # Setup git repository
    setup_git_repository()
    
    # Create sharing instructions
    create_sharing_instructions()
    
    print("\n" + "=" * 60)
    print("✅ Setup complete! Your toolkit is ready to share.")
    print("\n📋 Next Steps:")
    print("1. Review SHARING.md for distribution options")
    print("2. Consider creating a GitHub repository")
    print("3. Share with your classmates")
    print("4. Collaborate and improve together!")
    print("\n🎯 Your classmates will love this toolkit!")

if __name__ == "__main__":
    main() 