#!/usr/bin/env python3
"""
Tidy - Filename sanitization and cleanup utility
Standardizes filenames to consistent kebab-case format
"""

import re
from pathlib import Path
from typing import Dict, List

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to consistent kebab-case format
    
    Rules:
    - Convert to lowercase
    - Replace underscores with hyphens  
    - Remove/replace special characters
    - Remove multiple consecutive hyphens
    - Remove leading/trailing hyphens
    - Keep .md extension
    """
    # Get name and extension
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    
    # Convert to lowercase
    clean = stem.lower()
    
    # Replace problematic characters
    clean = re.sub(r'[_\s]+', '-', clean)  # underscores and spaces to hyphens
    clean = re.sub(r'[()[\]{}]', '', clean)  # remove brackets/parens
    clean = re.sub(r'[^\w\-]', '-', clean)  # other special chars to hyphens
    
    # Clean up multiple hyphens
    clean = re.sub(r'-+', '-', clean)
    
    # Remove leading/trailing hyphens
    clean = clean.strip('-')
    
    # Ensure we have something
    if not clean:
        clean = 'untitled'
    
    return f"{clean}{suffix}"

def preview_renames(directory: Path) -> Dict[str, str]:
    """Preview what files would be renamed"""
    renames = {}
    
    for file_path in directory.glob("*.md"):
        original = file_path.name
        sanitized = sanitize_filename(original)
        
        if original != sanitized:
            renames[original] = sanitized
    
    return renames

def apply_renames(directory: Path, renames: Dict[str, str], dry_run: bool = True) -> int:
    """Apply filename renames"""
    renamed_count = 0
    
    for original, sanitized in renames.items():
        original_path = directory / original
        sanitized_path = directory / sanitized
        
        # Check for conflicts
        if sanitized_path.exists() and sanitized_path != original_path:
            print(f"⚠️  Conflict: {sanitized} already exists, skipping {original}")
            continue
        
        if dry_run:
            print(f"🔄 Would rename: {original} → {sanitized}")
        else:
            try:
                original_path.rename(sanitized_path)
                print(f"✅ Renamed: {original} → {sanitized}")
                renamed_count += 1
            except Exception as e:
                print(f"❌ Error renaming {original}: {e}")
    
    return renamed_count

def tidy_directory(directory_name: str, dry_run: bool = True) -> None:
    """Tidy up filenames in a directory"""
    directory = Path(directory_name)
    
    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        return
    
    print(f"🧹 Tidying filenames in: {directory}")
    
    # Preview renames
    renames = preview_renames(directory)
    
    if not renames:
        print("✨ All filenames already tidy!")
        return
    
    print(f"\n📋 Found {len(renames)} files to rename:")
    
    # Apply renames
    renamed_count = apply_renames(directory, renames, dry_run)
    
    if dry_run:
        print(f"\n🔍 This was a dry run. To apply changes, run with --apply")
    else:
        print(f"\n🎉 Tidying complete! Renamed {renamed_count} files.")

def main():
    """Main tidy function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🧹 Tidy up filenames to consistent kebab-case")
    parser.add_argument("--apply", action="store_true", help="Actually apply renames (default: dry run)")
    parser.add_argument("--dir", default="summaries", help="Directory to tidy (default: summaries)")
    
    args = parser.parse_args()
    
    print("🧹 EXAMINATOR FILENAME TIDIER")
    print("=" * 40)
    
    # Tidy specified directory
    tidy_directory(args.dir, dry_run=not args.apply)
    
    # Also check other directories
    if args.dir == "summaries":
        print("\n📁 Checking other directories...")
        for other_dir in ["flashcards", "peekaboo", "output"]:
            if Path(other_dir).exists():
                print(f"\n🔍 Checking {other_dir}/:")
                other_renames = preview_renames(Path(other_dir))
                if other_renames:
                    print(f"  {len(other_renames)} files need tidying. Run: python3 tidy.py --dir {other_dir}")
                else:
                    print("  ✨ Already tidy!")

if __name__ == "__main__":
    main() 