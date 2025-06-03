# 🃏 Web Security Xss Exam Guide - LLM Generated Flashcards
*Generated from: web-security-xss-exam-guide.md*

## 📱 App-Compatible Format (for flashcard app)
1. **Cross-Site Scripting (XSS) vs Persistent XSS and Reflected XSS**: XSS is a web vulnerability where attackers inject malicious scripts into web pages. There are three main types: Stored XSS, Reflected XSS, and DOM-based XSS. In Stored XSS, the script is saved on the server and affects all users who view it. In Reflected XSS, the script executes immediately from user input without being stored.

   *Application*: Stored XSS allows attackers to persistently inject malicious scripts into a web page for all users. This can lead to data theft or session hijacking. Reflected XSS can be used in situations where the attacker wants to trick a user into clicking a harmful link, but the effects are temporary.

   *Prevention*: To prevent XSS attacks, employ input validation/sanitization, output encoding, Content Security Policy (CSP), use secure frameworks, and HTTP-only cookies.

2. **SQL injection vs Cross-Site Scripting (XSS)**: SQL injection targets the database layer by manipulating SQL queries, whereas XSS targets users by injecting client-side scripts into web pages.

   *Application*: SQL injection can allow attackers to access, modify, or delete sensitive data from a database, potentially causing serious damage to a website or application. On the other hand, XSS attacks can steal user data, hijack sessions, and redirect users to malicious sites.

   *Prevention*: To prevent SQL injection, use parameterized queries/prepared statements, input validation, the principle of least privilege for database accounts, stored procedures, and escape special characters.

3. **Defense in Depth for Web Security**: The principle of defense in depth is using multiple layers of security controls, such as input validation, output encoding, Content Security Policy (CSP), Web Application Firewall (WAF), and secure coding practices, instead of relying on a single protection mechanism to ensure comprehensive web application security.

   *Application*: Implementing the principle of defense in depth ensures that even if an attacker manages to bypass one layer of security, there are other layers in place to prevent them from compromising the system or accessing sensitive information.

---

## 🫣 Spoiler Format (for manual study/sharing)
*Click details to reveal answers*

1. **Cross-Site Scripting (XSS) vs Persistent XSS and Reflected XSS**: <details><summary>🤔 Click to reveal answer</summary>XSS is a web vulnerability where attackers inject malicious scripts into web pages. There are three main types: Stored XSS, Reflected XSS, and DOM-based XSS. In Stored XSS, the script is saved on the server and affects all users who view it. In Reflected XSS, the script executes immediately from user input without being stored.</details>

*Application*: Stored XSS allows attackers to persistently inject malicious scripts into a web page for all users. This can lead to data theft or session hijacking. Reflected XSS can be used in situations where the attacker wants to trick a user into clicking a harmful link, but the effects are temporary.

*Prevention*: To prevent XSS attacks, employ input validation/sanitization, output encoding, Content Security Policy (CSP), use secure frameworks, and HTTP-only cookies.

2. **SQL injection vs Cross-Site Scripting (XSS)**: <details><summary>🤔 Click to reveal answer</summary>SQL injection targets the database layer by manipulating SQL queries, whereas XSS targets users by injecting client-side scripts into web pages.</details>

*Application*: SQL injection can allow attackers to access, modify, or delete sensitive data from a database, potentially causing serious damage to a website or application. On the other hand, XSS attacks can steal user data, hijack sessions, and redirect users to malicious sites.

*Prevention*: To prevent SQL injection, use parameterized queries/prepared statements, input validation, the principle of least privilege for database accounts, stored procedures, and escape special characters.

3. **Defense in Depth for Web Security**: <details><summary>🤔 Click to reveal answer</summary>The principle of defense in depth is using multiple layers of security controls, such as input validation, output encoding, Content Security Policy (CSP), Web Application Firewall (WAF), and secure coding practices, instead of relying on a single protection mechanism to ensure comprehensive web application security.</details>

*Application*: Implementing the principle of defense in depth ensures that even if an attacker manages to bypass one layer of security, there are other layers in place to prevent them from compromising the system or accessing sensitive information.