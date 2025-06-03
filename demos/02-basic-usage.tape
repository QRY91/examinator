Output basic-usage.gif

Set FontSize 14
Set Width 1200
Set Height 600
Set PlaybackSpeed 2.5
Set Theme "Monokai Pro"

Hide
Type "cd examinator"
Enter
Show

Sleep 1s
Type "# EXAMINATOR - Basic Usage Demo"
Enter
Sleep 2s

Type "# Step 1: Create input directory and add your materials"
Enter
Sleep 1s

Type "mkdir -p input"
Enter
Sleep 1s

Type "# (Put your PDFs and markdown files in input/)"
Enter
Sleep 1s

Type "# For demo - let's check what scripts we have"
Enter
Sleep 1s

Type "ls -la *.py"
Enter
Sleep 2s

Type "# Step 2: Run the complete pipeline"
Enter
Type "# (This would process your actual materials)"
Enter
Sleep 1s

Type "echo 'python3 ingest.py          # Extract from PDFs'"
Enter
Sleep 2s

Type "echo 'python3 tidy.py --all      # Clean summaries'"
Enter
Sleep 2s

Type "echo 'python3 refine.py          # Generate guides'"
Enter
Sleep 2s

Type "echo 'python3 generate-practice-questions.py  # Create exam'"
Enter
Sleep 2s

Type "# Step 3: Study with flashcards"
Enter
Sleep 1s

Type "echo 'python3 flashcards.py      # Interactive study'"
Enter
Sleep 2s

Type "# Output goes to output/ and output/refined/"
Enter
Type "mkdir -p output/refined"
Enter
Sleep 1s

Type "# Ready to dominate your exams!"
Enter
Sleep 2s 