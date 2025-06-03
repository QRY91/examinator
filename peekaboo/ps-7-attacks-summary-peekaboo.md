# 🫣 Ps_7_Attacks (2) Summary - Peekaboo Study Guide
*Generated from: ps_7_attacks-(2)-summary.md*

**Click the details to reveal answers! Perfect for GitHub study sessions.**

---

# ⚔️ Attacks & Network Security - Clean Study Guide
## Network Attacks
**What is a Denial of Service (DoS) attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

An attack that makes a system or network resource unavailable by overwhelming it with traffic or requests.

</details>

**What is a Distributed Denial of Service (DDoS) attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

A DoS attack using multiple compromised systems (botnet) to flood the target with traffic from many sources.

</details>

**What is ARP poisoning/spoofing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Attack that associates the attacker's MAC address with the IP address of another host, redirecting network traffic through the attacker.

</details>

**What is DNS poisoning?**
<details>
<summary>🤔 Click to reveal answer</summary>

Corrupting DNS cache data to redirect domain name queries to malicious IP addresses instead of legitimate ones.

</details>

**What is a replay attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Intercepting and retransmitting valid network communications to gain unauthorized access or repeat transactions.

</details>

**What is IP spoofing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Forging the source IP address in packets to impersonate another system and bypass security controls.

</details>

## Wireless Security Attacks
**What is a man-in-the-middle (MITM) attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Intercepting and potentially altering communications between two parties who believe they're communicating directly.

</details>

**What are the main weaknesses of WEP?**
<details>
<summary>🤔 Click to reveal answer</summary>

Static encryption keys, weak 24-bit initialization vector (IV), and RC4 stream cipher vulnerabilities.

</details>

**What improvements does WPA2 provide over WEP?**
<details>
<summary>🤔 Click to reveal answer</summary>

Uses AES encryption, dynamic key generation per packet, and stronger authentication methods.

</details>

**What is a rogue access point?**
<details>
<summary>🤔 Click to reveal answer</summary>

Unauthorized wireless access point that can intercept wireless communications or provide network access to attackers.

</details>

**What is wardriving?**
<details>
<summary>🤔 Click to reveal answer</summary>

Searching for wireless networks while driving around to find unsecured or vulnerable access points.

</details>

## Web Application Attacks
**What is MAC address spoofing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Changing a device's MAC address to impersonate another device and bypass MAC address filtering.

</details>

**What is SQL injection?**
<details>
<summary>🤔 Click to reveal answer</summary>

Inserting malicious SQL code into application queries to access, modify, or delete database information.

</details>

**How can you prevent SQL injection?**
<details>
<summary>🤔 Click to reveal answer</summary>

Use parameterized queries/prepared statements, input validation, and principle of least privilege for database accounts.

</details>

**What is Cross-Site Scripting (XSS)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Injecting malicious scripts into web pages that execute in other users' browsers to steal data or hijack sessions.

</details>

**What is directory traversal?**
<details>
<summary>🤔 Click to reveal answer</summary>

Accessing files outside the web application's intended directory structure using relative path sequences (../).

</details>

**What is Cross-Site Request Forgery (CSRF)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Tricking users into performing unwanted actions on web applications where they're authenticated.

</details>

## Advanced Attack Techniques
**What is session hijacking?**
<details>
<summary>🤔 Click to reveal answer</summary>

Stealing or predicting session tokens to impersonate legitimate users and gain unauthorized access.

</details>

**What is a watering hole attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Compromising websites frequently visited by target organizations to infect visitors with malware.

</details>

**What is credential stuffing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Using stolen username/password combinations from one breach to attempt login on other services.

</details>

**What is password spraying?**
<details>
<summary>🤔 Click to reveal answer</summary>

Attempting common passwords against many user accounts to avoid account lockouts from repeated failed attempts.

</details>

## Defense Strategies
**What is a supply chain attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Compromising software or hardware during the development/distribution process to affect end users.

</details>

**How can you defend against DoS/DDoS attacks?**
<details>
<summary>🤔 Click to reveal answer</summary>

Use firewalls, rate limiting, load balancers, CDNs, and DDoS protection services.

</details>

**What is network segmentation?**
<details>
<summary>🤔 Click to reveal answer</summary>

Dividing networks into separate segments to limit attack spread and control access between segments.

</details>

**What is intrusion detection/prevention (IDS/IPS)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Systems that monitor network traffic for malicious activity and can alert or block suspicious behavior.

</details>

## Encryption & Protocol Security
**What is the principle of least privilege?**
<details>
<summary>🤔 Click to reveal answer</summary>

Granting users/systems only the minimum access rights needed to perform their functions.

</details>

**Why should you avoid unencrypted protocols?**
<details>
<summary>🤔 Click to reveal answer</summary>

Data transmitted in plaintext can be easily intercepted and read by attackers monitoring network traffic.

</details>

**What is the difference between authentication and encryption?**
<details>
<summary>🤔 Click to reveal answer</summary>

Authentication verifies identity, while encryption protects data confidentiality during transmission or storage.

</details>

**What are secure alternatives to insecure protocols?**
<details>
<summary>🤔 Click to reveal answer</summary>

HTTPS instead of HTTP, SFTP instead of FTP, SSH instead of Telnet, SNMP v3 instead of v1/v2.

</details>

## Penetration Testing
**What is Perfect Forward Secrecy?**
<details>
<summary>🤔 Click to reveal answer</summary>

Ensuring that compromise of long-term keys doesn't compromise past session keys or communications.

</details>

**What is penetration testing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Authorized simulated attacks on systems to identify vulnerabilities before real attackers find them.

</details>

**What are the phases of penetration testing?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Planning/Reconnaissance, 2) Scanning/Enumeration, 3) Exploitation, 4) Post-exploitation, 5) Reporting.

</details>

**What is the difference between black box and white box testing?**
<details>
<summary>🤔 Click to reveal answer</summary>

Black box tests with no prior knowledge of the system, white box tests with full system knowledge and access.

</details>

## Security Monitoring
**What are common penetration testing tools?**
<details>
<summary>🤔 Click to reveal answer</summary>

Nmap (network scanning), Metasploit (exploitation), Burp Suite (web apps), Wireshark (packet analysis).

</details>

**What should be logged for security monitoring?**
<details>
<summary>🤔 Click to reveal answer</summary>

Failed login attempts, privilege escalations, file access, network connections, and system changes.

</details>

**What is behavioral analysis in security?**
<details>
<summary>🤔 Click to reveal answer</summary>

Monitoring for unusual patterns in user behavior, network traffic, or system activity that may indicate attacks.

</details>

**What is threat hunting?**
<details>
<summary>🤔 Click to reveal answer</summary>

Proactively searching for signs of threats and attackers that may have evaded automated security controls.

</details>
