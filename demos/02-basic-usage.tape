Output basic-usage.gif

Set FontSize 14
Set Width 1200
Set Height 600
Set PlaybackSpeed 2.5
Set Theme "Monokai Pro"

Hide
Type "cd ~/security-prep"
Enter
Show

Sleep 1s
Type "# Basic Usage Demo - Process Study Materials"
Enter
Sleep 2s

Type "# Step 1: Check what's in input/ directory"
Enter
Sleep 1s

Type "ls -la input/"
Enter
Sleep 2s

Type "# Step 2: Run the complete pipeline"
Enter
Sleep 1s

Type "python3 ingest.py"
Enter
Sleep 4s

Type "# Step 3: Clean up duplicates and errors"
Enter
Sleep 1s

Type "python3 tidy.py --all"
Enter
Sleep 3s

Type "# Step 4: Generate exam-focused guides"
Enter
Sleep 1s

Type "python3 refine.py"
Enter
Sleep 3s

Type "# Step 5: Create practice questions"
Enter
Sleep 1s

Type "python3 generate-practice-questions.py"
Enter
Sleep 3s

Type "# Step 6: Check what we generated"
Enter
Sleep 1s

Type "ls -la output/"
Enter
Sleep 1s

Type "ls -la output/refined/"
Enter
Sleep 2s

Type "# Ready to study! Check output/refined/ for guides"
Enter
Sleep 2s 