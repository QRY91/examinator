# 🫣 Practice Exam - Peekaboo Study Guide
*Generated from: practice-exam.md*

**Click the details to reveal answers! Perfect for GitHub study sessions.**

---

# 🎯 Privacy & Security - Practice Exam
**Time Limit**: 3 hours
**Total Points**: 100 points
**Instructions**: Answer all questions completely. Show your work for practical exercises.
---
## Section 1: Open Questions (60 points)
### Question 1: Security Fundamentals (8 points (2 per advantage + mitigation))
In cybersecurity, attackers have significant advantages over defenders. Explain four key advantages that attackers possess and how defenders can mitigate each advantage.
**Answer:**
_[Write your answer here]_
---
### Question 2: CIA Triad (6 points)
A cryptocurrency exchange needs to ensure the availability of their trading platform. Identify three specific threats to availability and propose three corresponding protection measures.
**Answer:**
_[Write your answer here]_
---
### Question 3: Security Models (10 points)
What is the Bell-LaPadula Model? Explain how it works, draw a simple diagram showing the interaction between security levels, and provide one example of an organization that would benefit from implementing this model. Justify your choice.
**Answer:**
_[Write your answer here]_
---
### Question 4: Cryptography (8 points)
Explain the difference between steganography and encryption. What role does LSB (Least Significant Bit) play in steganography? Provide a practical example of when you would use steganography instead of encryption.
**Answer:**
_[Write your answer here]_
---
### Question 5: Classical Cryptography (8 points)
What is the difference between substitution and transposition in classical cryptography? Provide two specific examples of ciphers that use each technique and explain how they work.
**Answer:**
_[Write your answer here]_
---
### Question 6: Hash Functions (6 points)
How does HMAC (Hash-based Message Authentication Code) work? Explain when the key is added to the message during the process and what is ultimately attached to the message that gets sent.
**Answer:**
_[Write your answer here]_
---
### Question 7: Incident Response (8 points)
What are the four phases of incident response? Provide a detailed explanation of each phase and give specific examples of activities that occur in each phase.
**Answer:**
_[Write your answer here]_
---
### Question 8: Social Engineering (9 points)
Explain the differences between Vishing, Whaling, and Phishing. Provide specific examples of each attack type and describe how an organization can defend against them.
**Answer:**
_[Write your answer here]_
---
### Question 9: Web Security (10 points)
What is the difference between DOM-based XSS and Persistent (Stored) XSS? Explain each type with a practical example showing how the attack would be executed and how it would be prevented.
**Answer:**
_[Write your answer here]_
---
### Question 10: Privacy (10 points)
What is k-anonymity? Explain the concept comprehensively, including what k represents, how it's achieved, and provide an example with sample data showing how a dataset would be modified to achieve k=3 anonymity.
**Answer:**
_[Write your answer here]_
---
## Section 2: Practical Exercises (40 points)
### Exercise 1: XSS Attack Scenario (12 points)
**Scenario**: You discover that a forum website allows users to post comments with basic HTML formatting. When you post the following comment: `<b>This text is bold</b>`, it renders correctly with bold formatting.
**Questions:**
1. How could you use this knowledge to execute an XSS attack? Describe your attack strategy and provide the specific payload you would use.
**Answer:**
_[Write your answer here]_
2. What type of XSS vulnerability is this? Explain your reasoning.
**Answer:**
_[Write your answer here]_
3. How would you recommend the website developers fix this vulnerability? Provide specific technical solutions.
**Answer:**
_[Write your answer here]_
---
### Exercise 2: Data Anonymization Challenge (15 points)
**Scenario**: You have a medical research dataset with the following columns: Age, ZIP Code, Gender, Medical Condition. The dataset contains sensitive medical information that needs to be shared with researchers while protecting patient privacy.
```
Original Data:
Age | ZIP | Gender | Condition
25  | 1001| Female | Diabetes
28  | 1002| Male   | Hypertension
31  | 1001| Female | Diabetes
26  | 1003| Male   | Asthma
29  | 1002| Female | Hypertension
32  | 1001| Male   | Diabetes
```
**Questions:**
1. Transform this dataset to achieve k=3 anonymity while preserving as much useful information as possible.
**Answer:**
_[Write your answer here]_
2. Explain your anonymization strategy and justify your choices.
**Answer:**
_[Write your answer here]_
3. What are the limitations of your anonymized dataset for research purposes?
**Answer:**
_[Write your answer here]_
---
### Exercise 3: Security Model Implementation (12 points)
**Scenario**: A defense contractor needs to implement a security system for classified documents. They have three classification levels: Public, Confidential, and Secret. Users have corresponding clearance levels.
**Questions:**
1. Which security model would be most appropriate? Explain your choice.
**Answer:**
_[Write your answer here]_
2. Design the access control rules for this system. Show what read/write permissions each user type should have.
**Answer:**
_[Write your answer here]_
3. Provide a specific example scenario showing how the model would prevent unauthorized access.
**Answer:**
_[Write your answer here]_
---
### Exercise 4: Incident Response Simulation (15 points)
**Scenario**: At 2 PM on Monday, your organization's monitoring system alerts you that unusual network traffic is occurring. Several employees report that their computers are running slowly, and some files appear to be encrypted with ransom demands.
**Questions:**
1. What type of attack is likely occurring? Explain your reasoning.
**Answer:**
_[Write your answer here]_
2. Outline your immediate response actions for each phase of incident response.
**Answer:**
_[Write your answer here]_
3. What preventive measures should be implemented to avoid future occurrences?
**Answer:**
_[Write your answer here]_
---
## 📚 Study Tips
- Review the Bell-LaPadula and Biba models thoroughly
- Practice drawing security model diagrams
- Understand the differences between XSS types
- Know the incident response phases by heart
- Practice k-anonymity calculations with sample data
- Review cryptographic concepts and their applications