# 🎯 Security Fundamentals - Clean Demo Flashcards

## CIA Triad & Basic Security

**Q: What does CIA stand for in cybersecurity?**
A: Confidentiality, Integrity, Availability - the three fundamental principles of information security.

**Q: Define Confidentiality in the CIA Triad**
A: Ensuring that information is accessible only to those authorized to access it. Prevents unauthorized disclosure of sensitive data.

**Q: Define Integrity in the CIA Triad** 
A: Ensuring that information is accurate, complete, and has not been modified by unauthorized parties.

**Q: Define Availability in the CIA Triad**
A: Ensuring that information and systems are accessible when needed by authorized users.

**Q: What is the difference between authentication and authorization?**
A: Authentication verifies WHO you are (identity verification), while authorization determines WHAT you can access (permission control).

## Cryptography Basics

**Q: What is the main difference between symmetric and asymmetric encryption?**
A: Symmetric uses the same key for encryption/decryption (faster, shared secret), while asymmetric uses different keys - public/private key pairs (slower, no shared secret needed).

**Q: What is RSA and what is it used for?**
A: RSA is an asymmetric encryption algorithm using public/private key pairs. Used for secure key exchange, digital signatures, and encrypting small amounts of data.

**Q: What is AES?**
A: Advanced Encryption Standard - a symmetric encryption algorithm that's fast and secure. Uses 128, 192, or 256-bit keys.

**Q: What is hashing and how is it different from encryption?**
A: Hashing is a one-way function that creates a fixed-size digest from input data. Unlike encryption, it cannot be reversed - used for data integrity verification.

**Q: What is HMAC?**
A: Hash-based Message Authentication Code - combines a hash function with a secret key to provide both data integrity and authentication.

## Network Security

**Q: What is a firewall?**
A: A network security device that monitors and controls incoming/outgoing network traffic based on predetermined security rules.

**Q: What is the difference between HTTP and HTTPS?**
A: HTTPS (HTTP Secure) adds TLS/SSL encryption to HTTP, protecting data in transit between client and server.

**Q: What is a VPN?**
A: Virtual Private Network - creates a secure, encrypted tunnel over the internet for private communication.

## Common Attacks

**Q: What is phishing?**
A: A social engineering attack using fake emails, websites, or messages to trick users into revealing sensitive information like passwords or credit card numbers.

**Q: What is SQL injection?**
A: A web application attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access/modify database data.

**Q: What is Cross-Site Scripting (XSS)?**
A: A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data or hijacking sessions.

**Q: What is a man-in-the-middle attack?**
A: An attack where the attacker intercepts and potentially alters communications between two parties who believe they're communicating directly.

## Malware Types

**Q: What is a virus vs. a worm?**
A: A virus requires a host file and user action to spread, while a worm can replicate and spread automatically across networks without user interaction.

**Q: What is ransomware?**
A: Malware that encrypts victim's files and demands payment (ransom) for the decryption key.

**Q: What is a Trojan horse?**
A: Malware disguised as legitimate software that performs hidden malicious functions when executed.

## Access Control

**Q: What is the principle of least privilege?**
A: Users should be given the minimum levels of access necessary to perform their job functions - nothing more.

**Q: What is multi-factor authentication (MFA)?**
A: Security method requiring two or more verification factors: something you know (password), something you have (token), something you are (biometric).

**Q: What is role-based access control (RBAC)?**
A: Access control method where permissions are assigned to roles, and users are assigned to roles based on their job functions.

## Incident Response

**Q: What are the four main phases of incident response?**
A: 1) Preparation, 2) Detection & Analysis, 3) Containment, Eradication & Recovery, 4) Post-Incident Activity/Lessons Learned.

**Q: What should be the first priority during a security incident?**
A: Containment - prevent the incident from spreading or causing further damage while preserving evidence.

## Privacy & Compliance

**Q: What is data anonymization?**
A: The process of removing or altering personally identifiable information so individuals cannot be identified from the dataset.

**Q: What is k-anonymity?**
A: A privacy preservation technique ensuring each record is indistinguishable from at least k-1 other records based on quasi-identifiers. 