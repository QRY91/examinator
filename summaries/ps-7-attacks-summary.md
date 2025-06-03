# ⚔️ Attacks & Network Security - Clean Study Guide

## Network Attacks

**Q: What is a Denial of Service (DoS) attack?**
A: An attack that makes a system or network resource unavailable by overwhelming it with traffic or requests.

**Q: What is a Distributed Denial of Service (DDoS) attack?**
A: A DoS attack using multiple compromised systems (botnet) to flood the target with traffic from many sources.

**Q: What is ARP poisoning/spoofing?**
A: Attack that associates the attacker's MAC address with the IP address of another host, redirecting network traffic through the attacker.

**Q: What is DNS poisoning?**
A: Corrupting DNS cache data to redirect domain name queries to malicious IP addresses instead of legitimate ones.

**Q: What is a replay attack?**
A: Intercepting and retransmitting valid network communications to gain unauthorized access or repeat transactions.

**Q: What is IP spoofing?**
A: Forging the source IP address in packets to impersonate another system and bypass security controls.

**Q: What is a man-in-the-middle (MITM) attack?**
A: Intercepting and potentially altering communications between two parties who believe they're communicating directly.

## Wireless Security Attacks

**Q: What are the main weaknesses of WEP?**
A: Static encryption keys, weak 24-bit initialization vector (IV), and RC4 stream cipher vulnerabilities.

**Q: What improvements does WPA2 provide over WEP?**
A: Uses AES encryption, dynamic key generation per packet, and stronger authentication methods.

**Q: What is a rogue access point?**
A: Unauthorized wireless access point that can intercept wireless communications or provide network access to attackers.

**Q: What is wardriving?**
A: Searching for wireless networks while driving around to find unsecured or vulnerable access points.

**Q: What is MAC address spoofing?**
A: Changing a device's MAC address to impersonate another device and bypass MAC address filtering.

## Web Application Attacks

**Q: What is SQL injection?**
A: Inserting malicious SQL code into application queries to access, modify, or delete database information.

**Q: How can you prevent SQL injection?**
A: Use parameterized queries/prepared statements, input validation, and principle of least privilege for database accounts.

**Q: What is Cross-Site Scripting (XSS)?**
A: Injecting malicious scripts into web pages that execute in other users' browsers to steal data or hijack sessions.

**Q: What is directory traversal?**
A: Accessing files outside the web application's intended directory structure using relative path sequences (../).

**Q: What is Cross-Site Request Forgery (CSRF)?**
A: Tricking users into performing unwanted actions on web applications where they're authenticated.

**Q: What is session hijacking?**
A: Stealing or predicting session tokens to impersonate legitimate users and gain unauthorized access.

## Advanced Attack Techniques

**Q: What is a watering hole attack?**
A: Compromising websites frequently visited by target organizations to infect visitors with malware.

**Q: What is credential stuffing?**
A: Using stolen username/password combinations from one breach to attempt login on other services.

**Q: What is password spraying?**
A: Attempting common passwords against many user accounts to avoid account lockouts from repeated failed attempts.

**Q: What is a supply chain attack?**
A: Compromising software or hardware during the development/distribution process to affect end users.

## Defense Strategies

**Q: How can you defend against DoS/DDoS attacks?**
A: Use firewalls, rate limiting, load balancers, CDNs, and DDoS protection services.

**Q: What is network segmentation?**
A: Dividing networks into separate segments to limit attack spread and control access between segments.

**Q: What is intrusion detection/prevention (IDS/IPS)?**
A: Systems that monitor network traffic for malicious activity and can alert or block suspicious behavior.

**Q: What is the principle of least privilege?**
A: Granting users/systems only the minimum access rights needed to perform their functions.

## Encryption & Protocol Security

**Q: Why should you avoid unencrypted protocols?**
A: Data transmitted in plaintext can be easily intercepted and read by attackers monitoring network traffic.

**Q: What is the difference between authentication and encryption?**
A: Authentication verifies identity, while encryption protects data confidentiality during transmission or storage.

**Q: What are secure alternatives to insecure protocols?**
A: HTTPS instead of HTTP, SFTP instead of FTP, SSH instead of Telnet, SNMP v3 instead of v1/v2.

**Q: What is Perfect Forward Secrecy?**
A: Ensuring that compromise of long-term keys doesn't compromise past session keys or communications.

## Penetration Testing

**Q: What is penetration testing?**
A: Authorized simulated attacks on systems to identify vulnerabilities before real attackers find them.

**Q: What are the phases of penetration testing?**
A: 1) Planning/Reconnaissance, 2) Scanning/Enumeration, 3) Exploitation, 4) Post-exploitation, 5) Reporting.

**Q: What is the difference between black box and white box testing?**
A: Black box tests with no prior knowledge of the system, white box tests with full system knowledge and access.

**Q: What are common penetration testing tools?**
A: Nmap (network scanning), Metasploit (exploitation), Burp Suite (web apps), Wireshark (packet analysis).

## Security Monitoring

**Q: What should be logged for security monitoring?**
A: Failed login attempts, privilege escalations, file access, network connections, and system changes.

**Q: What is behavioral analysis in security?**
A: Monitoring for unusual patterns in user behavior, network traffic, or system activity that may indicate attacks.

**Q: What is threat hunting?**
A: Proactively searching for signs of threats and attackers that may have evaded automated security controls.
