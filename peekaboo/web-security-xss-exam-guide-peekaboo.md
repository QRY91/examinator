# 🫣 Web Security Xss Exam Guide - Peekaboo Study Guide
*Generated from: web-security-xss-exam-guide.md*

**Click the details to reveal answers! Perfect for GitHub study sessions.**

---

# 🌐 Web Security & XSS - Clean Study Guide
## 🎯 Expected Exam Questions
1. DOM-based XSS vs Persistent XSS - explain with examples and prevention
2. XSS attack strategy and website protection methods
3. SQL injection prevention techniques
## 📚 Key Concepts & Definitions
### Cross-Site Scripting (XSS)
**What is Cross-Site Scripting (XSS)?**
<details>
<summary>🤔 Click to reveal answer</summary>

A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data, hijacking sessions, or redirecting users.

</details>

**What are the three main types of XSS?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Reflected XSS (non-persistent), 2) Stored XSS (persistent), 3) DOM-based XSS (client-side).

</details>

**What is the difference between Stored XSS and Reflected XSS?**
<details>
<summary>🤔 Click to reveal answer</summary>

Stored XSS saves malicious script on the server (in database/files) and affects all users who view it. Reflected XSS executes immediately from user input without being stored.

</details>

**What is DOM-based XSS?**
<details>
<summary>🤔 Click to reveal answer</summary>

XSS that occurs entirely in the client-side JavaScript when the page's DOM is modified with user-controlled data, without sending data to the server.

</details>

### SQL Injection
**How can you prevent XSS attacks?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Input validation/sanitization, 2) Output encoding, 3) Content Security Policy (CSP), 4) Use secure frameworks, 5) HTTP-only cookies.

</details>

**What is SQL injection?**
<details>
<summary>🤔 Click to reveal answer</summary>

An attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access, modify, or delete database data.

</details>

**How can you prevent SQL injection?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Use parameterized queries/prepared statements, 2) Input validation, 3) Principle of least privilege for database accounts, 4) Stored procedures, 5) Escape special characters.

</details>

### Web Application Security
**What is the difference between SQL injection and XSS?**
<details>
<summary>🤔 Click to reveal answer</summary>

SQL injection targets the database layer by manipulating SQL queries, while XSS targets users by injecting client-side scripts into web pages.

</details>

**What is input validation?**
<details>
<summary>🤔 Click to reveal answer</summary>

The process of checking that user input meets expected criteria (format, length, type) before processing it in the application.

</details>

**What is output encoding?**
<details>
<summary>🤔 Click to reveal answer</summary>

Converting potentially dangerous characters into safe representations before displaying them to users (e.g., converting < to &lt;).

</details>

**What is Content Security Policy (CSP)?**
<details>
<summary>🤔 Click to reveal answer</summary>

A security header that helps prevent XSS by controlling which resources the browser is allowed to load for a web page.

</details>

**What is CSRF (Cross-Site Request Forgery)?**
<details>
<summary>🤔 Click to reveal answer</summary>

An attack that tricks users into performing unwanted actions on a web application where they're authenticated, by exploiting their existing session.

</details>

### Secure Development
**How do you prevent CSRF attacks?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) CSRF tokens, 2) SameSite cookie attribute, 3) Verify referer headers, 4) Double-submit cookies, 5) Custom headers for AJAX requests.

</details>

**What is the principle of defense in depth for web security?**
<details>
<summary>🤔 Click to reveal answer</summary>

Using multiple layers of security controls (input validation, output encoding, CSP, WAF, secure coding) rather than relying on a single protection mechanism.

</details>

**What is a Web Application Firewall (WAF)?**
<details>
<summary>🤔 Click to reveal answer</summary>

A security appliance that filters HTTP traffic to protect web applications from attacks like XSS, SQL injection, and other web exploits.

</details>

## 💡 Study Tips
**What are HTTP security headers?**
<details>
<summary>🤔 Click to reveal answer</summary>

Special headers that enhance web security: Content-Security-Policy, X-Frame-Options, X-XSS-Protection, Strict-Transport-Security, etc. - Practice identifying XSS vulnerabilities in code samples - Learn to write parameterized queries in your programming language - Understand the difference between client-side and server-side validation - Practice hands-on XSS and SQL injection exercises in safe environments - Review OWASP Top 10 web application security risks

</details>
