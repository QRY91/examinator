Output install.gif

Set FontSize 14
Set Width 1200
Set Height 600
Set PlaybackSpeed 2.0
Set Theme "Monokai Pro"

Hide
Type "# Cloning examinator repo"
Enter
Type "git clone https://github.com/QRY91/examinator.git"
Enter
Sleep 2s
Type "cd examinator"
Enter
Show

Sleep 1s
Type "# EXAMINATOR - Installation Demo"
Enter
Sleep 2s

Type "# Step 1: Install required packages"
Enter
Sleep 1s

Type "pip3 install textual --user --break-system-packages"
Enter
Sleep 3s

Type "pip3 install PyMuPDF --user --break-system-packages"
Enter
Sleep 3s

Type "# Step 2: Make scripts executable"
Enter
Sleep 1s

Type "chmod +x *.py"
Enter
Sleep 1s

Type "# Step 3: Check if everything works"
Enter
Sleep 1s

Type "python3 --version"
Enter
Sleep 1s

Type "python3 -c 'import textual'"
Enter
Sleep 1s

Type "python3 -c 'import fitz'"
Enter
Sleep 1s

Type "ls -la *.py"
Enter
Sleep 2s

Type "# Ready to crush exams! Try: python3 flashcards.py"
Enter
Sleep 2s 