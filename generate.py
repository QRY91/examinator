#!/usr/bin/env python3
"""
🌶️ Spicy Question Generator - Local LLM Practice Questions
Uses Ollama + Mistral to generate targeted practice questions from study materials
One file at a time, slower but free and private!
"""

import json
import subprocess
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any
import time

class SpicyQuestionGenerator:
    def __init__(self, model: str = "mistral:latest"):
        self.model = model
        self.output_dir = Path("output")  # For comprehensive questions/scenarios  
        self.flashcards_dir = Path("flashcards")  # Dedicated flashcards directory
        self.summaries_dir = Path("summaries")
        
    def _call_ollama(self, prompt: str, timeout: int = 60) -> str:
        """Call Ollama to generate content"""
        try:
            print(f"🧠 Calling {self.model}... (timeout: {timeout}s)")
            result = subprocess.run([
                "ollama", "run", self.model
            ], input=prompt, capture_output=True, text=True, timeout=timeout)
            
            if result.returncode != 0:
                return f"❌ LLM Error: {result.stderr}"
            
            print(f"✅ Response received ({len(result.stdout)} chars)")
            return result.stdout.strip()
            
        except subprocess.TimeoutExpired:
            return f"⏰ Timeout after {timeout} seconds"
        except Exception as e:
            return f"💥 Error: {str(e)}"
    
    def test_ollama_connection(self) -> bool:
        """Test if Ollama is running and model is available"""
        try:
            print(f"🔌 Testing connection to {self.model}...")
            result = subprocess.run([
                "ollama", "run", self.model
            ], input="Hello, respond with just 'OK'", capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                print("✅ Ollama connection successful!")
                return True
            else:
                print(f"❌ Ollama error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            print("💡 Make sure Ollama is running: 'ollama serve'")
            print(f"💡 And model is installed: 'ollama pull {self.model}'")
            return False

    def extract_study_content(self, file_path: Path) -> str:
        """Extract the key concepts from a study file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove markdown formatting for cleaner LLM input
            content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)  # Remove bold
            content = re.sub(r'#{1,6}\s+', '', content)  # Remove headers
            content = re.sub(r'\n\s*\n', '\n', content)  # Remove empty lines
            
            return content.strip()
            
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return ""

    def generate_multiple_choice_questions(self, content: str, num_questions: int = 5) -> str:
        """Generate multiple choice questions from study content"""
        
        prompt = f"""You are an expert educator creating practice exam questions. 

Based on this cybersecurity study material, create {num_questions} challenging multiple-choice questions.

STUDY MATERIAL:
{content[:3000]}  

REQUIREMENTS:
1. Each question should test understanding, not just memorization
2. Include practical scenarios when possible
3. All 4 options should be plausible (no obvious wrong answers)
4. Focus on concepts that would appear on a real security exam
5. Mix difficulty levels (some easy recall, some harder application)

FORMAT each question as:
**Question X:** [Question text]
A) [Option A]
B) [Option B] 
C) [Option C]
D) [Option D]
**Answer:** [Correct letter with brief explanation]

Generate exactly {num_questions} questions now:"""

        result = self._call_ollama(prompt, timeout=90)
        return self._validate_flashcard_output(result, num_cards)
    
    def _validate_flashcard_output(self, output: str, expected_count: int) -> str:
        """Validate and clean flashcard output to prevent garbage"""
        if not output or len(output.strip()) < 50:
            return "❌ Error: AI generated insufficient content"
        
        # Count valid flashcards (look for numbered format)
        import re
        flashcard_pattern = r'\d+\.\s*\*\*.*?\*\*:\s*.+'
        matches = re.findall(flashcard_pattern, output, re.MULTILINE)
        
        if len(matches) < expected_count // 2:  # At least half the expected cards
            return f"❌ Error: AI generated only {len(matches)} valid flashcards out of {expected_count} expected"
        
        # Check for garbage patterns
        garbage_indicators = [
            "I cannot", "I'm sorry", "As an AI", "I don't have access",
            "```", "---", "Note:", "Disclaimer:", "Please note"
        ]
        
        for indicator in garbage_indicators:
            if indicator in output:
                return f"❌ Error: AI output contains garbage pattern: '{indicator}'"
        
        # Clean up the output
        lines = output.strip().split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):  # Remove headers and empty lines
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)

    def generate_scenario_questions(self, content: str, num_scenarios: int = 3) -> str:
        """Generate practical scenario-based questions"""
        
        prompt = f"""You are a cybersecurity instructor creating practical scenario questions.

Based on this study material, create {num_scenarios} realistic workplace scenarios that test application of these concepts.

STUDY MATERIAL:
{content[:3000]}

REQUIREMENTS:
1. Each scenario should be realistic and job-relevant
2. Questions should require applying multiple concepts
3. Include enough context for a complete answer
4. Make scenarios specific and actionable

FORMAT each scenario as:
**Scenario X:** [Detailed realistic scenario setup]

**Your Task:** [What the student needs to do/analyze/recommend]

**Key Considerations:** [What concepts should be applied]

Generate exactly {num_scenarios} scenarios now:"""

        return self._call_ollama(prompt, timeout=90)

    def generate_definition_drills(self, content: str, num_terms: int = 10) -> str:
        """Generate definition drilling questions"""
        
        prompt = f"""Extract the most important technical terms from this cybersecurity material and create definition drill questions.

STUDY MATERIAL:
{content[:3000]}

Create {num_terms} "fill-in-the-blank" or "define this term" questions focusing on the key vocabulary.

REQUIREMENTS:
1. Focus on terms that are frequently confused or have precise technical meanings
2. Include both acronyms and concepts
3. Make questions test precise understanding, not just vague recognition

FORMAT each as:
**Term X:** [Question asking for definition or fill-in-the-blank]
**Answer:** [Precise definition with key points]

Generate exactly {num_terms} definition questions now:"""

        return self._call_ollama(prompt, timeout=60)

    def generate_flashcards(self, content: str, num_cards: int = 15) -> str:
        """Generate flashcards from study content with quality validation"""
        
        prompt = f"""You are creating study flashcards. Be precise and factual.

SOURCE MATERIAL:
{content[:3000]}

REQUIREMENTS:
- Create exactly {num_cards} flashcards
- Each tests ONE specific concept
- Questions must be clear and complete
- Answers must be factual and concise (1-2 sentences max)
- No repetition between cards
- Focus on testable facts, not opinions

FORMAT (use exactly this format):
1. **[Clear question or "What is..." or "How does..."]**: [Factual answer in 1-2 sentences]

EXAMPLE:
1. **What is the main purpose of SSL/TLS encryption**: To provide secure communication over networks by encrypting data in transit and authenticating server identity.

Generate exactly {num_cards} flashcards using this exact format:"""

        result = self._call_ollama(prompt, timeout=90)
        return self._validate_flashcard_output(result, num_cards)

    def generate_flashcards_with_spoilers(self, content: str, num_cards: int = 15) -> tuple[str, str]:
        """Generate flashcards in both regular format and spoiler format"""
        
        # Generate regular flashcards first
        regular_flashcards = self.generate_flashcards(content, num_cards)
        
        if regular_flashcards.startswith("❌") or regular_flashcards.startswith("⏰") or regular_flashcards.startswith("💥"):
            return regular_flashcards, regular_flashcards
        
        # Convert to spoiler format
        spoiler_lines = []
        for line in regular_flashcards.split('\n'):
            line = line.strip()
            
            # Handle both bullet point format (- **) and numbered format (1. **)
            if (line.startswith('- **') and '**: ' in line) or (line.startswith(tuple(f'{i}. **' for i in range(1, 100))) and '**: ' in line):
                # Extract question and answer
                if '**: ' in line:
                    parts = line.split('**: ', 1)
                    if len(parts) == 2:
                        question_part = parts[0] + '**'  # Keep the numbering/bullet and **Question**
                        answer = parts[1]
                        # Create spoiler version with HTML details/summary
                        spoiler_line = f"{question_part}: <details><summary>🤔 Click to reveal answer</summary>{answer}</details>"
                        spoiler_lines.append(spoiler_line)
                    else:
                        spoiler_lines.append(line)
                else:
                    spoiler_lines.append(line)
            else:
                spoiler_lines.append(line)
        
        spoiler_content = '\n'.join(spoiler_lines)
        return regular_flashcards, spoiler_content

    def generate_flashcards_only(self, file_path: Path, num_cards: int = 15, include_spoilers: bool = False) -> str:
        """Generate only flashcards for a study file in flashcard app format"""
        
        print(f"\n🃏 SPICY FLASHCARD GENERATION")  
        print(f"📁 File: {file_path.name}")
        print(f"🤖 Model: {self.model}")
        if include_spoilers:
            print("🫣 Including spoiler format for manual study")
        print("=" * 60)
        
        content = self.extract_study_content(file_path)
        if not content:
            return "❌ No content extracted from file"
        
        print(f"📄 Extracted {len(content)} characters of study content")
        print(f"🔄 Generating {num_cards} flashcards...")
        
        if include_spoilers:
            regular_flashcards, spoiler_flashcards = self.generate_flashcards_with_spoilers(content, num_cards)
            
            if regular_flashcards.startswith("❌"):
                return regular_flashcards
            
            # Format both versions
            topic_name = file_path.stem.replace('-', ' ').replace('_', ' ').title()
            
            combined_content = [
                f"# 🃏 {topic_name} - LLM Generated Flashcards",
                f"*Generated from: {file_path.name}*\n",
                "## 📱 App-Compatible Format (for flashcard app)",
                regular_flashcards,
                "\n---\n",
                "## 🫣 Spoiler Format (for manual study/sharing)",
                "*Click details to reveal answers*\n",
                spoiler_flashcards
            ]
            
            return '\n'.join(combined_content)
        else:
            # Regular generation
            flashcards = self.generate_flashcards(content, num_cards)
            
            if flashcards.startswith("❌") or flashcards.startswith("⏰") or flashcards.startswith("💥"):
                return flashcards
            
            # Format for flashcard app
            topic_name = file_path.stem.replace('-', ' ').replace('_', ' ').title()
            formatted_content = [
                f"# 🃏 {topic_name} - LLM Generated Flashcards",
                f"*Generated from: {file_path.name}*\n",
                flashcards
            ]
            
            return '\n'.join(formatted_content)

    def generate_comprehensive_questions(self, file_path: Path, question_types: List[str] = None) -> str:
        """Generate a comprehensive set of questions for a study file"""
        
        if question_types is None:
            question_types = ["multiple_choice", "scenarios", "definitions"]
        
        print(f"\n🎯 Processing: {file_path.name}")
        print("=" * 60)
        
        content = self.extract_study_content(file_path)
        if not content:
            return "❌ No content extracted from file"
        
        print(f"📄 Extracted {len(content)} characters of study content")
        
        all_questions = []
        topic_name = file_path.stem.replace('-', ' ').replace('_', ' ').title()
        
        # Header
        all_questions.append(f"# 🎯 Practice Questions: {topic_name}")
        all_questions.append(f"*Generated from: {file_path.name}*\n")
        
        # Generate different types of questions
        if "multiple_choice" in question_types:
            print("🔄 Generating multiple choice questions...")
            mc_questions = self.generate_multiple_choice_questions(content, 5)
            all_questions.append("## 📝 Multiple Choice Questions\n")
            all_questions.append(mc_questions)
            all_questions.append("\n")
        
        if "scenarios" in question_types:
            print("🔄 Generating scenario questions...")
            scenario_questions = self.generate_scenario_questions(content, 3)
            all_questions.append("## 🏢 Practical Scenarios\n")
            all_questions.append(scenario_questions)
            all_questions.append("\n")
        
        if "definitions" in question_types:
            print("🔄 Generating definition drills...")
            definition_questions = self.generate_definition_drills(content, 8)
            all_questions.append("## 📚 Definition Drills\n")
            all_questions.append(definition_questions)
            all_questions.append("\n")
        
        if "flashcards" in question_types:
            print("🔄 Generating flashcards...")
            flashcards = self.generate_flashcards(content, 15)
            all_questions.append("## 🃏 Flashcards\n")
            all_questions.append(flashcards)
            all_questions.append("\n")
        
        return "\n".join(all_questions)

    def save_questions(self, questions: str, original_file: Path) -> Path:
        """Save generated questions to output directory"""
        output_file = self.output_dir / f"{original_file.stem}-questions.md"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(questions)
            
            print(f"💾 Questions saved to: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"❌ Error saving questions: {e}")
            return None

    def save_flashcards(self, flashcards: str, original_file: Path) -> Path:
        """Save generated flashcards to flashcards directory"""
        output_file = self.flashcards_dir / f"{original_file.stem}-llm-flashcards.md"
        
        try:
            # Ensure flashcards directory exists
            self.flashcards_dir.mkdir(exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(flashcards)
            
            print(f"💾 Flashcards saved to: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"❌ Error saving flashcards: {e}")
            return None

    def process_file(self, file_path: Path, question_types: List[str] = None) -> bool:
        """Process a single file and generate questions"""
        
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return False
        
        print(f"\n🌶️ SPICY QUESTION GENERATION")
        print(f"📁 File: {file_path}")
        print(f"🤖 Model: {self.model}")
        
        # Generate questions
        questions = self.generate_comprehensive_questions(file_path, question_types)
        
        if questions.startswith("❌"):
            print(questions)
            return False
        
        # Save questions
        output_file = self.save_questions(questions, file_path)
        
        if output_file:
            print(f"\n🎉 Success! Generated questions for {file_path.name}")
            print(f"📄 Output: {output_file}")
            return True
        
        return False

    def process_flashcards_only(self, file_path: Path, num_cards: int = 15, include_spoilers: bool = False) -> bool:
        """Process a single file and generate only flashcards"""
        
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return False
        
        # Generate flashcards
        flashcards = self.generate_flashcards_only(file_path, num_cards, include_spoilers)
        
        if flashcards.startswith("❌"):
            print(flashcards)
            return False
        
        # Save flashcards
        output_file = self.save_flashcards(flashcards, file_path)
        
        if output_file:
            print(f"\n🎉 Success! Generated {num_cards} flashcards for {file_path.name}")
            print(f"📄 Output: {output_file}")
            if include_spoilers:
                print("🫣 Includes both app-compatible and spoiler formats")
            print(f"🃏 Ready for flashcard app!")
            return True
        
        return False

    def process_all_summaries(self, question_types: List[str] = None) -> None:
        """Process all files in summaries directory"""
        
        if not self.summaries_dir.exists():
            print(f"❌ Summaries directory not found: {self.summaries_dir}")
            return
        
        markdown_files = list(self.summaries_dir.glob("*.md"))
        
        if not markdown_files:
            print(f"❌ No markdown files found in {self.summaries_dir}")
            return
        
        print(f"🎯 Found {len(markdown_files)} study files")
        print("🌶️ Starting SPICY question generation...\n")
        
        successful = 0
        failed = 0
        
        for file_path in markdown_files:
            try:
                if self.process_file(file_path, question_types):
                    successful += 1
                else:
                    failed += 1
                    
                # Add delay between files to be nice to local LLM
                print("⏳ Waiting 2 seconds before next file...")
                time.sleep(2)
                
            except KeyboardInterrupt:
                print("\n⏸️ Generation interrupted by user")
                break
            except Exception as e:
                print(f"💥 Error processing {file_path.name}: {e}")
                failed += 1
        
        print(f"\n🏁 GENERATION COMPLETE")
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📁 Questions saved to: {self.output_dir}")

def generate_flashcards_from_file(file_path: str, num_cards: int = 15) -> str:
    """Wrapper function for fusion integration - generate flashcards from file"""
    generator = SpicyQuestionGenerator()
    file_path_obj = Path(file_path)
    
    if not generator.test_ollama_connection():
        raise Exception("Ollama connection failed")
    
    success = generator.process_flashcards_only(file_path_obj, num_cards=num_cards)
    if success:
        output_file = generator.flashcards_dir / f"{file_path_obj.stem}-llm-flashcards.md"
        return str(output_file)
    else:
        raise Exception(f"Failed to generate flashcards for {file_path}")

def generate_wiki_from_file(file_path: str) -> str:
    """Wrapper function for fusion integration - generate comprehensive content from file"""
    generator = SpicyQuestionGenerator()
    file_path_obj = Path(file_path)
    
    if not generator.test_ollama_connection():
        raise Exception("Ollama connection failed")
    
    success = generator.process_file(file_path_obj, question_types=["multiple_choice", "scenarios", "definitions"])
    if success:
        output_file = generator.output_dir / f"{file_path_obj.stem}-questions.md"
        return str(output_file)
    else:
        raise Exception(f"Failed to generate wiki content for {file_path}")

def main():
    parser = argparse.ArgumentParser(description="🌶️ Generate spicy practice questions using local LLM")
    parser.add_argument("--file", "-f", type=str, help="Process specific file")
    parser.add_argument("--model", "-m", type=str, default="mistral:latest", help="Ollama model to use")
    parser.add_argument("--types", "-t", nargs="+", 
                       choices=["multiple_choice", "scenarios", "definitions", "flashcards"], 
                       default=["multiple_choice", "scenarios", "definitions"],
                       help="Types of questions to generate")
    parser.add_argument("--flashcards", action="store_true", help="Generate only flashcards (faster)")
    parser.add_argument("--cards", "-c", type=int, default=15, help="Number of flashcards to generate (default: 15)")
    parser.add_argument("--spoilers", action="store_true", help="Include spoiler format with hidden answers")
    parser.add_argument("--test", action="store_true", help="Test Ollama connection only")
    
    args = parser.parse_args()
    
    generator = SpicyQuestionGenerator(model=args.model)
    
    # Test connection first
    if not generator.test_ollama_connection():
        print("\n💡 To get started:")
        print("1. Install Ollama: https://ollama.ai")
        print("2. Start service: ollama serve")
        print(f"3. Install model: ollama pull {args.model}")
        return
    
    if args.test:
        print("🎉 Connection test successful! Ready to generate questions.")
        return
    
    # Ensure directories exist
    generator.output_dir.mkdir(exist_ok=True)
    generator.flashcards_dir.mkdir(exist_ok=True)
    
    if args.flashcards:
        # Generate only flashcards
        if args.file:
            file_path = Path(args.file)
            if not file_path.exists():
                file_path = generator.summaries_dir / args.file
            generator.process_flashcards_only(file_path, args.cards, args.spoilers)
        else:
            print("❌ --flashcards requires --file. Use: python3 generate-practice-questions.py --flashcards -f filename.md")
            print("💡 Add --spoilers for hidden answers: --flashcards --spoilers -f filename.md")
    elif args.file:
        # Process single file with specified question types
        file_path = Path(args.file)
        if not file_path.exists():
            # Try in summaries directory
            file_path = generator.summaries_dir / args.file
        
        generator.process_file(file_path, args.types)
    else:
        # Process all summaries
        generator.process_all_summaries(args.types)

if __name__ == "__main__":
    main() 