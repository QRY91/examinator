#!/usr/bin/env python3
"""
Exam-Targeted Study Guide Refiner
Analyzes mock exam questions and creates targeted study materials
Matches assignment content to exam question patterns

Usage: python refine.py
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Set
from collections import defaultdict

# Mock exam question patterns extracted from the PDF
EXAM_QUESTIONS = {
    "CIA Triad & Security Fundamentals": [
        "What threatens availability of a system? How to protect availability?",
        "Attacker advantages vs defender - explain three advantages",
        "Bell LaPadula Model - how it works, diagram, real-world application"
    ],
    "Cryptography & Steganography": [
        "What is steganography? Difference from encryption? LSB role?",
        "Substitution vs transposition - examples from classical cryptography",
        "How does HMAC work? Key addition process? Final message format?"
    ],
    "Incident Response & Social Engineering": [
        "Four phases of incident response - explain each phase",
        "Difference between Vishing, Whaling, and Phishing"
    ],
    "Web Security & XSS": [
        "DOM-based XSS vs Persistent XSS - explain with examples",
        "XSS attack strategy and website protection methods"
    ],
    "Privacy & Anonymization": [
        "What is k-anonymity? Complete explanation",
        "Pseudonymization for k=3 anonymity with minimal information loss"
    ]
}

def extract_relevant_content(summaries_dir: Path, question_keywords: List[str]) -> List[str]:
    """Extract content relevant to specific exam topics"""
    relevant_content = []
    
    for summary_file in summaries_dir.glob("*-summary.md"):
        try:
            with open(summary_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find concepts that match question keywords
            concepts = re.findall(r'- \*\*(.*?)\*\*:\s*(.*?)(?=\n-|\n#|\n\n|\Z)', content, re.DOTALL)
            
            for term, definition in concepts:
                term_lower = term.lower()
                definition_lower = definition.lower()
                
                # Check if any keyword matches
                if any(keyword.lower() in term_lower or keyword.lower() in definition_lower 
                       for keyword in question_keywords):
                    clean_def = re.sub(r'\s+', ' ', definition.strip())
                    relevant_content.append(f"**{term.strip()}**: {clean_def}")
        
        except Exception as e:
            print(f"⚠️  Error processing {summary_file}: {e}")
    
    return relevant_content

def create_exam_focused_guide(topic: str, questions: List[str], content: List[str]) -> str:
    """Create an exam-focused study guide for a topic"""
    
    guide = [f"# {topic} - Exam Focus Guide\n"]
    
    # Add exam questions first
    guide.append("## 🎯 Expected Exam Questions")
    for i, question in enumerate(questions, 1):
        guide.append(f"{i}. {question}")
    guide.append("")
    
    # Add relevant study content
    guide.append("## 📚 Key Concepts & Definitions")
    if content:
        for concept in content:
            guide.append(f"- {concept}")
    else:
        guide.append("- ⚠️ No matching content found - review course materials!")
    guide.append("")
    
    # Add study tips
    guide.append("## 💡 Study Tips")
    guide.append("- Practice explaining concepts in your own words")
    guide.append("- Draw diagrams where applicable (e.g., Bell LaPadula Model)")
    guide.append("- Create real-world examples for each concept")
    guide.append("- Practice hands-on exercises if relevant")
    guide.append("")
    
    return '\n'.join(guide)

def generate_keyword_map() -> Dict[str, List[str]]:
    """Generate keywords for each exam topic"""
    return {
        "CIA Triad & Security Fundamentals": [
            "availability", "confidentiality", "integrity", "CIA", "bell lapadula", 
            "access control", "security model", "attacker", "defender", "threat"
        ],
        "Cryptography & Steganography": [
            "steganography", "LSB", "substitution", "transposition", "classical cryptography",
            "caesar", "vigenere", "HMAC", "hash", "key", "encryption", "encoding"
        ],
        "Incident Response & Social Engineering": [
            "incident response", "phishing", "vishing", "whaling", "social engineering",
            "preparation", "detection", "containment", "recovery", "lessons learned"
        ],
        "Web Security & XSS": [
            "XSS", "cross-site scripting", "DOM", "persistent", "reflected", "stored",
            "web application", "injection", "sanitization", "validation"
        ],
        "Privacy & Anonymization": [
            "k-anonymity", "pseudonymization", "anonymization", "privacy", "data protection",
            "quasi-identifier", "sensitive attribute", "generalization", "suppression"
        ]
    }

def create_comprehensive_exam_prep() -> str:
    """Create a comprehensive exam preparation overview"""
    
    content = [
        "# 🎯 Privacy & Security Exam - Complete Prep Guide\n",
        "## 📋 Exam Structure",
        "- **Duration**: 3 hours",
        "- **Format**: Open questions + Practical exercises", 
        "- **Materials**: Calculator, laptop, internet, course materials allowed",
        "- **Sections**: Theory questions + Hands-on problems\n",
        
        "## 🎪 Question Types Analysis",
        "Based on the mock exam, expect these question patterns:",
        "",
        "### 1. Conceptual Explanations",
        "- Define concepts clearly and completely",
        "- Compare/contrast related concepts (e.g., XSS types)",
        "- Explain processes step-by-step (e.g., HMAC, incident response)",
        "",
        "### 2. Real-world Applications", 
        "- Security models in business contexts",
        "- Attack scenarios and defenses",
        "- Privacy protection techniques",
        "",
        "### 3. Hands-on Problem Solving",
        "- XSS attack construction and mitigation",
        "- Data anonymization exercises", 
        "- Cryptographic implementations",
        "",
        "## 🚀 Study Strategy",
        "1. **Master the fundamentals** (CIA triad, security models)",
        "2. **Practice explanations** - explain concepts out loud",
        "3. **Draw diagrams** for complex models (Bell LaPadula)",
        "4. **Hands-on practice** with XSS, anonymization",
        "5. **Create examples** for each major concept",
        "",
        "## ⏰ Last-minute Review Checklist",
        "- [ ] CIA Triad definitions and examples",
        "- [ ] Bell LaPadula Model diagram and use cases", 
        "- [ ] Steganography vs Encryption differences",
        "- [ ] HMAC process steps",
        "- [ ] Incident response phases",
        "- [ ] Phishing variants (vishing, whaling)",
        "- [ ] XSS types and mitigation",
        "- [ ] K-anonymity calculation",
        "",
        "## 🎯 Focus Areas",
        "High-probability exam topics based on mock exam:",
        "- Security fundamentals & CIA triad",
        "- Cryptography basics & steganography", 
        "- Web application security (XSS)",
        "- Privacy protection techniques",
        "- Incident response procedures",
        ""
    ]
    
    return '\n'.join(content)

def main():
    output_dir = Path("output")
    refined_dir = output_dir / "refined"
    refined_dir.mkdir(exist_ok=True)
    
    print("🎯 Creating Exam-Focused Study Guides")
    print("=" * 50)
    
    # Generate keyword mapping
    keyword_map = generate_keyword_map()
    
    guides_created = 0
    
    # Create focused guides for each exam topic
    for topic, questions in EXAM_QUESTIONS.items():
        print(f"\n📚 Processing: {topic}")
        
        # Get relevant keywords
        keywords = keyword_map.get(topic, [])
        
        # Extract relevant content from existing summaries
        relevant_content = extract_relevant_content(output_dir, keywords)
        
        print(f"✅ Found {len(relevant_content)} relevant concepts")
        
        # Create exam-focused guide
        guide_content = create_exam_focused_guide(topic, questions, relevant_content)
        
        # Save guide
        filename = topic.lower().replace(' & ', '-').replace(' ', '-') + "-exam-guide.md"
        guide_path = refined_dir / filename
        
        try:
            with open(guide_path, 'w', encoding='utf-8') as f:
                f.write(guide_content)
            print(f"✨ Created: {guide_path.name}")
            guides_created += 1
        except Exception as e:
            print(f"❌ Error creating {filename}: {e}")
    
    # Create comprehensive overview
    print(f"\n📋 Creating comprehensive exam prep guide")
    overview_content = create_comprehensive_exam_prep()
    overview_path = refined_dir / "00-exam-overview.md"
    
    try:
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write(overview_content)
        print(f"✨ Created: {overview_path.name}")
        guides_created += 1
    except Exception as e:
        print(f"❌ Error creating overview: {e}")
    
    print("\n" + "=" * 50)
    print(f"✅ Created {guides_created} exam-focused guides")
    print(f"📁 Saved to: {refined_dir}")
    print(f"🎯 Ready for targeted exam preparation!")

if __name__ == "__main__":
    main() 