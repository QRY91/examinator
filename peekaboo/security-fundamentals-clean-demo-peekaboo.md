# 🫣 Security Fundamentals Clean Demo - Peekaboo Study Guide
*Generated from: security-fundamentals-clean-demo.md*

**Click the details to reveal answers! Perfect for GitHub study sessions.**

---

# 🎯 Security Fundamentals - Clean Demo Flashcards
## CIA Triad & Basic Security
** What does CIA stand for in cybersecurity?**
<details>
<summary>🤔 Click to reveal answer</summary>

Confidentiality, Integrity, Availability - the three fundamental principles of information security.

</details>

** Define Confidentiality in the CIA Triad**
<details>
<summary>🤔 Click to reveal answer</summary>

Ensuring that information is accessible only to those authorized to access it. Prevents unauthorized disclosure of sensitive data.

</details>

** Define Integrity in the CIA Triad**
<details>
<summary>🤔 Click to reveal answer</summary>

Ensuring that information is accurate, complete, and has not been modified by unauthorized parties.

</details>

** Define Availability in the CIA Triad**
<details>
<summary>🤔 Click to reveal answer</summary>

Ensuring that information and systems are accessible when needed by authorized users.

</details>

## Cryptography Basics
** What is the difference between authentication and authorization?**
<details>
<summary>🤔 Click to reveal answer</summary>

Authentication verifies WHO you are (identity verification), while authorization determines WHAT you can access (permission control).

</details>

** What is the main difference between symmetric and asymmetric encryption?**
<details>
<summary>🤔 Click to reveal answer</summary>

Symmetric uses the same key for encryption/decryption (faster, shared secret), while asymmetric uses different keys - public/private key pairs (slower, no shared secret needed).

</details>

** What is RSA and what is it used for?**
<details>
<summary>🤔 Click to reveal answer</summary>

RSA is an asymmetric encryption algorithm using public/private key pairs. Used for secure key exchange, digital signatures, and encrypting small amounts of data.

</details>

** What is AES?**
<details>
<summary>🤔 Click to reveal answer</summary>

Advanced Encryption Standard - a symmetric encryption algorithm that's fast and secure. Uses 128, 192, or 256-bit keys.

</details>

** What is hashing and how is it different from encryption?**
<details>
<summary>🤔 Click to reveal answer</summary>

Hashing is a one-way function that creates a fixed-size digest from input data. Unlike encryption, it cannot be reversed - used for data integrity verification.

</details>

## Network Security
** What is HMAC?**
<details>
<summary>🤔 Click to reveal answer</summary>

Hash-based Message Authentication Code - combines a hash function with a secret key to provide both data integrity and authentication.

</details>

** What is a firewall?**
<details>
<summary>🤔 Click to reveal answer</summary>

A network security device that monitors and controls incoming/outgoing network traffic based on predetermined security rules.

</details>

** What is the difference between HTTP and HTTPS?**
<details>
<summary>🤔 Click to reveal answer</summary>

HTTPS (HTTP Secure) adds TLS/SSL encryption to HTTP, protecting data in transit between client and server.

</details>

## Common Attacks
** What is a VPN?**
<details>
<summary>🤔 Click to reveal answer</summary>

Virtual Private Network - creates a secure, encrypted tunnel over the internet for private communication.

</details>

** What is phishing?**
<details>
<summary>🤔 Click to reveal answer</summary>

A social engineering attack using fake emails, websites, or messages to trick users into revealing sensitive information like passwords or credit card numbers.

</details>

** What is SQL injection?**
<details>
<summary>🤔 Click to reveal answer</summary>

A web application attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access/modify database data.

</details>

** What is Cross-Site Scripting (XSS)?**
<details>
<summary>🤔 Click to reveal answer</summary>

A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data or hijacking sessions.

</details>

## Malware Types
** What is a man-in-the-middle attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

An attack where the attacker intercepts and potentially alters communications between two parties who believe they're communicating directly.

</details>

** What is a virus vs. a worm?**
<details>
<summary>🤔 Click to reveal answer</summary>

A virus requires a host file and user action to spread, while a worm can replicate and spread automatically across networks without user interaction.

</details>

** What is ransomware?**
<details>
<summary>🤔 Click to reveal answer</summary>

Malware that encrypts victim's files and demands payment (ransom) for the decryption key.

</details>

## Access Control
** What is a Trojan horse?**
<details>
<summary>🤔 Click to reveal answer</summary>

Malware disguised as legitimate software that performs hidden malicious functions when executed.

</details>

** What is the principle of least privilege?**
<details>
<summary>🤔 Click to reveal answer</summary>

Users should be given the minimum levels of access necessary to perform their job functions - nothing more.

</details>

** What is multi-factor authentication (MFA)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Security method requiring two or more verification factors: something you know (password), something you have (token), something you are (biometric).

</details>

## Incident Response
** What is role-based access control (RBAC)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Access control method where permissions are assigned to roles, and users are assigned to roles based on their job functions.

</details>

** What are the four main phases of incident response?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Preparation, 2) Detection & Analysis, 3) Containment, Eradication & Recovery, 4) Post-Incident Activity/Lessons Learned.

</details>

## Privacy & Compliance
** What should be the first priority during a security incident?**
<details>
<summary>🤔 Click to reveal answer</summary>

Containment - prevent the incident from spreading or causing further damage while preserving evidence.

</details>

** What is data anonymization?**
<details>
<summary>🤔 Click to reveal answer</summary>

The process of removing or altering personally identifiable information so individuals cannot be identified from the dataset.

</details>

** What is k-anonymity?**
<details>
<summary>🤔 Click to reveal answer</summary>

A privacy preservation technique ensuring each record is indistinguishable from at least k-1 other records based on quasi-identifiers.

</details>
