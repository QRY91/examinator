# Web Security Xss Exam Guide

## 📚 Study Questions & Answers

### 1. What is Cross-Site Scripting (XSS)?

<details>
<summary>🤔 Click to reveal answer</summary>

A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data, hijacking sessions, or redirecting users.

</details>

### 2. What are the three main types of XSS?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Reflected XSS (non-persistent), 2) Stored XSS (persistent), 3) DOM-based XSS (client-side).

</details>

### 3. What is the difference between Stored XSS and Reflected XSS?

<details>
<summary>🤔 Click to reveal answer</summary>

Stored XSS saves malicious script on the server (in database/files) and affects all users who view it. Reflected XSS executes immediately from user input without being stored.

</details>

### 4. What is DOM-based XSS?

<details>
<summary>🤔 Click to reveal answer</summary>

XSS that occurs entirely in the client-side JavaScript when the page's DOM is modified with user-controlled data, without sending data to the server.

</details>

### 5. How can you prevent XSS attacks?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Input validation/sanitization, 2) Output encoding, 3) Content Security Policy (CSP), 4) Use secure frameworks, 5) HTTP-only cookies.
### SQL Injection

</details>

### 6. What is SQL injection?

<details>
<summary>🤔 Click to reveal answer</summary>

An attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access, modify, or delete database data.

</details>

### 7. How can you prevent SQL injection?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Use parameterized queries/prepared statements, 2) Input validation, 3) Principle of least privilege for database accounts, 4) Stored procedures, 5) Escape special characters.

</details>

### 8. What is the difference between SQL injection and XSS?

<details>
<summary>🤔 Click to reveal answer</summary>

SQL injection targets the database layer by manipulating SQL queries, while XSS targets users by injecting client-side scripts into web pages.
### Web Application Security

</details>

### 9. What is input validation?

<details>
<summary>🤔 Click to reveal answer</summary>

The process of checking that user input meets expected criteria (format, length, type) before processing it in the application.

</details>

### 10. What is output encoding?

<details>
<summary>🤔 Click to reveal answer</summary>

Converting potentially dangerous characters into safe representations before displaying them to users (e.g., converting < to &lt;).

</details>

### 11. What is Content Security Policy (CSP)?

<details>
<summary>🤔 Click to reveal answer</summary>

A security header that helps prevent XSS by controlling which resources the browser is allowed to load for a web page.

</details>

### 12. What is CSRF (Cross-Site Request Forgery)?

<details>
<summary>🤔 Click to reveal answer</summary>

An attack that tricks users into performing unwanted actions on a web application where they're authenticated, by exploiting their existing session.

</details>

### 13. How do you prevent CSRF attacks?

<details>
<summary>🤔 Click to reveal answer</summary>

1) CSRF tokens, 2) SameSite cookie attribute, 3) Verify referer headers, 4) Double-submit cookies, 5) Custom headers for AJAX requests.
### Secure Development

</details>

### 14. What is the principle of defense in depth for web security?

<details>
<summary>🤔 Click to reveal answer</summary>

Using multiple layers of security controls (input validation, output encoding, CSP, WAF, secure coding) rather than relying on a single protection mechanism.

</details>

### 15. What is a Web Application Firewall (WAF)?

<details>
<summary>🤔 Click to reveal answer</summary>

A security appliance that filters HTTP traffic to protect web applications from attacks like XSS, SQL injection, and other web exploits.

</details>

### 16. What are HTTP security headers?

<details>
<summary>🤔 Click to reveal answer</summary>

Special headers that enhance web security: Content-Security-Policy, X-Frame-Options, X-XSS-Protection, Strict-Transport-Security, etc.
## 💡 Study Tips
- Practice identifying XSS vulnerabilities in code samples
- Learn to write parameterized queries in your programming language
- Understand the difference between client-side and server-side validation
- Practice hands-on XSS and SQL injection exercises in safe environments
- Review OWASP Top 10 web application security risks

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**