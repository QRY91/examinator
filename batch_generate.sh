#!/bin/bash
# EXAMINATOR BATCH FLASHCARD GENERATOR

echo "🤖 EXAMINATOR MECH: BATCH PROCESSING INITIATED!"
echo "🎯 Target: C# Model Files"

# Process all C# files in Models directory
for file in input/ENGAGE/PXLPRO2025Shoppers25/Webshop.MVC/Models/*.cs; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "💥 FIRING ON: $filename"
        python3 generate.py --flashcards -f "$file"
        echo "✅ $filename DESTROYED!"
        echo ""
    fi
done

echo "🚀 BATCH DESTRUCTION COMPLETE!"
echo "📚 Generated flashcards ready for combat!"
