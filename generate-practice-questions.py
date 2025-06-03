#!/usr/bin/env python3
"""
Practice Question Generator for Security Exam
Creates questions matching mock exam style based on processed materials

Usage: python generate-practice-questions.py
"""

import random
from pathlib import Path
from typing import List, Dict

class SecurityQuestionGenerator:
    def __init__(self):
        self.question_templates = {
            "CIA_TRIAD": [
                "Explain three specific threats to {aspect} and provide corresponding protection measures for each.",
                "A {organization} wants to ensure {aspect} of their {system}. Describe three implementation strategies they should consider.",
                "Compare {aspect} requirements in a {context1} versus a {context2} environment. Provide specific examples.",
                "You are consulting for a {organization}. Their {aspect} has been compromised. Outline a recovery plan with specific steps."
            ],
            "CRYPTOGRAPHY": [
                "Explain the difference between {concept1} and {concept2}. Provide a practical example of when each would be used.",
                "A company needs to implement {technique}. Describe the step-by-step process and potential security considerations.",
                "Compare {algorithm1} and {algorithm2}. Discuss their strengths, weaknesses, and appropriate use cases.",
                "Design a secure communication protocol using {method}. Explain each component and its purpose."
            ],
            "ATTACKS": [
                "Describe how a {attack_type} attack works. Include the attacker's methodology and potential countermeasures.",
                "Compare {attack1} and {attack2}. Explain the differences in execution and detection methods.",
                "A {organization} experienced a {attack_type} attack. Create an incident response plan with specific phases.",
                "Analyze the security vulnerabilities that enable {attack_type}. Propose three defensive strategies."
            ],
            "WEB_SECURITY": [
                "Explain the difference between {xss_type1} and {xss_type2} XSS. Provide code examples for each.",
                "A web application is vulnerable to {vulnerability}. Demonstrate how an attacker would exploit this and how to fix it.",
                "Design a secure web application architecture that prevents {attack_list}. Explain each security layer.",
                "Compare client-side and server-side security measures for preventing {attack_type}."
            ],
            "PRIVACY": [
                "Explain {privacy_concept} and provide a practical implementation example with sample data.",
                "A dataset needs {anonymization_level} anonymization. Design a strategy that minimizes information loss.",
                "Compare {technique1} and {technique2} for privacy protection. Discuss their effectiveness and limitations.",
                "Create a privacy-preserving data sharing protocol for {scenario}. Include technical and policy measures."
            ],
            "MODELS": [
                "Explain the {model} security model. Draw a diagram showing how it works and provide a real-world application example.",
                "Compare {model1} and {model2} security models. Discuss when each would be most appropriate.",
                "A {organization} wants to implement the {model} model. Describe the implementation challenges and solutions.",
                "Analyze how the {model} model addresses {security_aspect}. Provide specific examples of rule enforcement."
            ]
        }
        
        self.fill_values = {
            "aspect": ["confidentiality", "integrity", "availability"],
            "organization": ["military base", "hospital", "bank", "university", "government agency", "tech startup"],
            "system": ["database", "network infrastructure", "communication system", "file server", "web application"],
            "context1": ["military", "commercial", "healthcare", "financial"],
            "context2": ["academic", "government", "retail", "manufacturing"],
            "concept1": ["symmetric encryption", "steganography", "hashing", "digital signatures"],
            "concept2": ["asymmetric encryption", "encryption", "encoding", "certificates"],
            "technique": ["HMAC", "RSA key exchange", "AES encryption", "digital signatures"],
            "algorithm1": ["AES", "RSA", "SHA-256", "Caesar cipher"],
            "algorithm2": ["DES", "ECC", "MD5", "Vigenère cipher"],
            "method": ["public key cryptography", "symmetric encryption", "hash functions"],
            "attack_type": ["phishing", "man-in-the-middle", "SQL injection", "buffer overflow", "social engineering"],
            "attack1": ["vishing", "reflected XSS", "brute force", "ARP spoofing"],
            "attack2": ["whaling", "stored XSS", "dictionary attack", "DNS spoofing"],
            "xss_type1": ["DOM-based", "reflected", "persistent"],
            "xss_type2": ["stored", "non-persistent", "blind"],
            "vulnerability": ["XSS", "SQL injection", "CSRF", "directory traversal"],
            "attack_list": ["XSS, SQL injection, and CSRF", "buffer overflows and injection attacks"],
            "privacy_concept": ["k-anonymity", "l-diversity", "t-closeness", "differential privacy"],
            "anonymization_level": ["k=3", "k=5", "strong"],
            "technique1": ["generalization", "k-anonymity", "pseudonymization"],
            "technique2": ["suppression", "l-diversity", "tokenization"],
            "scenario": ["medical research", "financial analysis", "academic collaboration"],
            "model": ["Bell-LaPadula", "Biba", "Clark-Wilson", "Chinese Wall"],
            "model1": ["Bell-LaPadula", "Biba"],
            "model2": ["Clark-Wilson", "Chinese Wall"],
            "security_aspect": ["confidentiality", "integrity", "access control"]
        }

    def generate_question(self, category: str) -> str:
        """Generate a single question for the given category"""
        if category not in self.question_templates:
            return "Invalid category"
        
        template = random.choice(self.question_templates[category])
        
        # Fill in the template with random values
        filled_question = template
        for placeholder, values in self.fill_values.items():
            if f"{{{placeholder}}}" in filled_question:
                filled_question = filled_question.replace(f"{{{placeholder}}}", random.choice(values))
        
        return filled_question

    def generate_specific_questions(self) -> List[Dict[str, str]]:
        """Generate specific questions based on mock exam patterns"""
        specific_questions = [
            {
                "category": "Security Fundamentals",
                "question": "In cybersecurity, attackers have significant advantages over defenders. Explain four key advantages that attackers possess and how defenders can mitigate each advantage.",
                "points": "8 points (2 per advantage + mitigation)"
            },
            {
                "category": "CIA Triad", 
                "question": "A cryptocurrency exchange needs to ensure the availability of their trading platform. Identify three specific threats to availability and propose three corresponding protection measures.",
                "points": "6 points"
            },
            {
                "category": "Security Models",
                "question": "What is the Bell-LaPadula Model? Explain how it works, draw a simple diagram showing the interaction between security levels, and provide one example of an organization that would benefit from implementing this model. Justify your choice.",
                "points": "10 points"
            },
            {
                "category": "Cryptography",
                "question": "Explain the difference between steganography and encryption. What role does LSB (Least Significant Bit) play in steganography? Provide a practical example of when you would use steganography instead of encryption.",
                "points": "8 points"
            },
            {
                "category": "Classical Cryptography",
                "question": "What is the difference between substitution and transposition in classical cryptography? Provide two specific examples of ciphers that use each technique and explain how they work.",
                "points": "8 points"
            },
            {
                "category": "Hash Functions",
                "question": "How does HMAC (Hash-based Message Authentication Code) work? Explain when the key is added to the message during the process and what is ultimately attached to the message that gets sent.",
                "points": "6 points"
            },
            {
                "category": "Incident Response",
                "question": "What are the four phases of incident response? Provide a detailed explanation of each phase and give specific examples of activities that occur in each phase.",
                "points": "8 points"
            },
            {
                "category": "Social Engineering",
                "question": "Explain the differences between Vishing, Whaling, and Phishing. Provide specific examples of each attack type and describe how an organization can defend against them.",
                "points": "9 points"
            },
            {
                "category": "Web Security",
                "question": "What is the difference between DOM-based XSS and Persistent (Stored) XSS? Explain each type with a practical example showing how the attack would be executed and how it would be prevented.",
                "points": "10 points"
            },
            {
                "category": "Privacy",
                "question": "What is k-anonymity? Explain the concept comprehensively, including what k represents, how it's achieved, and provide an example with sample data showing how a dataset would be modified to achieve k=3 anonymity.",
                "points": "10 points"
            }
        ]
        return specific_questions

    def generate_practical_exercises(self) -> List[Dict[str, str]]:
        """Generate practical exercises similar to mock exam section 2"""
        exercises = [
            {
                "title": "XSS Attack Scenario",
                "scenario": "You discover that a forum website allows users to post comments with basic HTML formatting. When you post the following comment: `<b>This text is bold</b>`, it renders correctly with bold formatting.",
                "questions": [
                    "1. How could you use this knowledge to execute an XSS attack? Describe your attack strategy and provide the specific payload you would use.",
                    "2. What type of XSS vulnerability is this? Explain your reasoning.",
                    "3. How would you recommend the website developers fix this vulnerability? Provide specific technical solutions."
                ],
                "points": "12 points"
            },
            {
                "title": "Data Anonymization Challenge",
                "scenario": "You have a medical research dataset with the following columns: Age, ZIP Code, Gender, Medical Condition. The dataset contains sensitive medical information that needs to be shared with researchers while protecting patient privacy.",
                "data": """
Original Data:
Age | ZIP | Gender | Condition
25  | 1001| Female | Diabetes
28  | 1002| Male   | Hypertension  
31  | 1001| Female | Diabetes
26  | 1003| Male   | Asthma
29  | 1002| Female | Hypertension
32  | 1001| Male   | Diabetes
                """,
                "questions": [
                    "1. Transform this dataset to achieve k=3 anonymity while preserving as much useful information as possible.",
                    "2. Explain your anonymization strategy and justify your choices.",
                    "3. What are the limitations of your anonymized dataset for research purposes?"
                ],
                "points": "15 points"
            },
            {
                "title": "Security Model Implementation",
                "scenario": "A defense contractor needs to implement a security system for classified documents. They have three classification levels: Public, Confidential, and Secret. Users have corresponding clearance levels.",
                "questions": [
                    "1. Which security model would be most appropriate? Explain your choice.",
                    "2. Design the access control rules for this system. Show what read/write permissions each user type should have.",
                    "3. Provide a specific example scenario showing how the model would prevent unauthorized access."
                ],
                "points": "12 points"
            },
            {
                "title": "Incident Response Simulation",
                "scenario": "At 2 PM on Monday, your organization's monitoring system alerts you that unusual network traffic is occurring. Several employees report that their computers are running slowly, and some files appear to be encrypted with ransom demands.",
                "questions": [
                    "1. What type of attack is likely occurring? Explain your reasoning.",
                    "2. Outline your immediate response actions for each phase of incident response.",
                    "3. What preventive measures should be implemented to avoid future occurrences?"
                ],
                "points": "15 points"
            }
        ]
        return exercises

def create_practice_exam():
    """Create a complete practice exam"""
    generator = SecurityQuestionGenerator()
    
    # Create exam header
    exam_content = [
        "# 🎯 Privacy & Security - Practice Exam\n",
        "**Time Limit**: 3 hours",
        "**Total Points**: 100 points",
        "**Instructions**: Answer all questions completely. Show your work for practical exercises.\n",
        "---\n",
        "## Section 1: Open Questions (60 points)\n"
    ]
    
    # Add specific questions
    specific_questions = generator.generate_specific_questions()
    for i, q in enumerate(specific_questions, 1):
        exam_content.append(f"### Question {i}: {q['category']} ({q['points']})")
        exam_content.append(f"{q['question']}\n")
        exam_content.append("**Answer:**")
        exam_content.append("_[Write your answer here]_\n")
        exam_content.append("---\n")
    
    # Add practical exercises
    exam_content.append("## Section 2: Practical Exercises (40 points)\n")
    exercises = generator.generate_practical_exercises()
    
    for i, exercise in enumerate(exercises, 1):
        exam_content.append(f"### Exercise {i}: {exercise['title']} ({exercise['points']})")
        exam_content.append(f"**Scenario**: {exercise['scenario']}")
        
        if 'data' in exercise:
            exam_content.append(f"```\n{exercise['data']}\n```")
        
        exam_content.append("\n**Questions:**")
        for question in exercise['questions']:
            exam_content.append(question)
            exam_content.append("\n**Answer:**")
            exam_content.append("_[Write your answer here]_\n")
        
        exam_content.append("---\n")
    
    # Add study tips
    exam_content.extend([
        "## 📚 Study Tips",
        "- Review the Bell-LaPadula and Biba models thoroughly",
        "- Practice drawing security model diagrams",
        "- Understand the differences between XSS types", 
        "- Know the incident response phases by heart",
        "- Practice k-anonymity calculations with sample data",
        "- Review cryptographic concepts and their applications",
        ""
    ])
    
    return '\n'.join(exam_content)

def main():
    # Create refined directory if it doesn't exist
    refined_dir = Path("output/refined")
    refined_dir.mkdir(exist_ok=True)
    
    print("🎯 Generating Practice Questions")
    print("=" * 50)
    
    # Generate complete practice exam
    practice_exam = create_practice_exam()
    
    # Save practice exam
    exam_path = refined_dir / "practice-exam.md"
    try:
        with open(exam_path, 'w', encoding='utf-8') as f:
            f.write(practice_exam)
        print(f"✨ Created complete practice exam: {exam_path.name}")
    except Exception as e:
        print(f"❌ Error creating practice exam: {e}")
    
    # Generate random questions for additional practice
    generator = SecurityQuestionGenerator()
    random_questions = []
    
    categories = ["CIA_TRIAD", "CRYPTOGRAPHY", "ATTACKS", "WEB_SECURITY", "PRIVACY", "MODELS"]
    
    for category in categories:
        for _ in range(3):  # 3 questions per category
            question = generator.generate_question(category)
            random_questions.append(f"**{category.replace('_', ' ').title()}**: {question}")
    
    # Save random questions
    random_content = [
        "# 🎲 Additional Practice Questions\n",
        "These questions are randomly generated for extra practice:\n"
    ]
    
    for i, question in enumerate(random_questions, 1):
        random_content.append(f"{i}. {question}\n")
    
    random_path = refined_dir / "additional-practice-questions.md"
    try:
        with open(random_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(random_content))
        print(f"✨ Created additional questions: {random_path.name}")
    except Exception as e:
        print(f"❌ Error creating additional questions: {e}")
    
    print("\n" + "=" * 50)
    print(f"✅ Practice question generation complete!")
    print(f"📁 Files saved to: {refined_dir}")
    print(f"🎯 Ready for intensive exam practice!")

if __name__ == "__main__":
    main() 