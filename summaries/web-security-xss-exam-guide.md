# 🌐 Web Security & XSS - Clean Study Guide

## 🎯 Expected Exam Questions
1. DOM-based XSS vs Persistent XSS - explain with examples and prevention
2. XSS attack strategy and website protection methods
3. SQL injection prevention techniques

## 📚 Key Concepts & Definitions

### Cross-Site Scripting (XSS)

**Q: What is Cross-Site Scripting (XSS)?**
A: A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data, hijacking sessions, or redirecting users.

**Q: What are the three main types of XSS?**
A: 1) Reflected XSS (non-persistent), 2) Stored XSS (persistent), 3) DOM-based XSS (client-side).

**Q: What is the difference between Stored XSS and Reflected XSS?**
A: Stored XSS saves malicious script on the server (in database/files) and affects all users who view it. Reflected XSS executes immediately from user input without being stored.

**Q: What is DOM-based XSS?**
A: XSS that occurs entirely in the client-side JavaScript when the page's DOM is modified with user-controlled data, without sending data to the server.

**Q: How can you prevent XSS attacks?**
A: 1) Input validation/sanitization, 2) Output encoding, 3) Content Security Policy (CSP), 4) Use secure frameworks, 5) HTTP-only cookies.

### SQL Injection

**Q: What is SQL injection?**
A: An attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access, modify, or delete database data.

**Q: How can you prevent SQL injection?**
A: 1) Use parameterized queries/prepared statements, 2) Input validation, 3) Principle of least privilege for database accounts, 4) Stored procedures, 5) Escape special characters.

**Q: What is the difference between SQL injection and XSS?**
A: SQL injection targets the database layer by manipulating SQL queries, while XSS targets users by injecting client-side scripts into web pages.

### Web Application Security

**Q: What is input validation?**
A: The process of checking that user input meets expected criteria (format, length, type) before processing it in the application.

**Q: What is output encoding?**
A: Converting potentially dangerous characters into safe representations before displaying them to users (e.g., converting < to &lt;).

**Q: What is Content Security Policy (CSP)?**
A: A security header that helps prevent XSS by controlling which resources the browser is allowed to load for a web page.

**Q: What is CSRF (Cross-Site Request Forgery)?**
A: An attack that tricks users into performing unwanted actions on a web application where they're authenticated, by exploiting their existing session.

**Q: How do you prevent CSRF attacks?**
A: 1) CSRF tokens, 2) SameSite cookie attribute, 3) Verify referer headers, 4) Double-submit cookies, 5) Custom headers for AJAX requests.

### Secure Development

**Q: What is the principle of defense in depth for web security?**
A: Using multiple layers of security controls (input validation, output encoding, CSP, WAF, secure coding) rather than relying on a single protection mechanism.

**Q: What is a Web Application Firewall (WAF)?**
A: A security appliance that filters HTTP traffic to protect web applications from attacks like XSS, SQL injection, and other web exploits.

**Q: What are HTTP security headers?**
A: Special headers that enhance web security: Content-Security-Policy, X-Frame-Options, X-XSS-Protection, Strict-Transport-Security, etc.

## 💡 Study Tips
- Practice identifying XSS vulnerabilities in code samples
- Learn to write parameterized queries in your programming language
- Understand the difference between client-side and server-side validation
- Practice hands-on XSS and SQL injection exercises in safe environments
- Review OWASP Top 10 web application security risks
