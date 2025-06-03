# Web Security Xss Exam Guide - Flashcards

- **Cross-Site Scripting (XSS)**: A web vulnerability where attackers inject malicious scripts into web pages viewed by other users, potentially stealing data, hijacking sessions, or redirecting users.
- **the three main types of XSS**: 1) Reflected XSS (non-persistent), 2) Stored XSS (persistent), 3) DOM-based XSS (client-side).
- **the difference between Stored XSS and Reflected XSS**: Stored XSS saves malicious script on the server (in database/files) and affects all users who view it. Reflected XSS executes immediately from user input without being stored.
- **DOM-based XSS**: XSS that occurs entirely in the client-side JavaScript when the page's DOM is modified with user-controlled data, without sending data to the server.
- **How can you prevent XSS attacks**: 1) Input validation/sanitization, 2) Output encoding, 3) Content Security Policy (CSP), 4) Use secure frameworks, 5) HTTP-only cookies.
- **SQL injection**: An attack where malicious SQL code is inserted into application queries, potentially allowing attackers to access, modify, or delete database data.
- **How can you prevent SQL injection**: 1) Use parameterized queries/prepared statements, 2) Input validation, 3) Principle of least privilege for database accounts, 4) Stored procedures, 5) Escape special characters.
- **the difference between SQL injection and XSS**: SQL injection targets the database layer by manipulating SQL queries, while XSS targets users by injecting client-side scripts into web pages.
- **input validation**: The process of checking that user input meets expected criteria (format, length, type) before processing it in the application.
- **output encoding**: Converting potentially dangerous characters into safe representations before displaying them to users (e.g., converting < to &lt;).
- **Content Security Policy (CSP)**: A security header that helps prevent XSS by controlling which resources the browser is allowed to load for a web page.
- **CSRF (Cross-Site Request Forgery)**: An attack that tricks users into performing unwanted actions on a web application where they're authenticated, by exploiting their existing session.
- **How do you prevent CSRF attacks**: 1) CSRF tokens, 2) SameSite cookie attribute, 3) Verify referer headers, 4) Double-submit cookies, 5) Custom headers for AJAX requests.
- **the principle of defense in depth for web security**: Using multiple layers of security controls (input validation, output encoding, CSP, WAF, secure coding) rather than relying on a single protection mechanism.
- **a Web Application Firewall (WAF)**: A security appliance that filters HTTP traffic to protect web applications from attacks like XSS, SQL injection, and other web exploits.
- **HTTP security headers**: Special headers that enhance web security: Content-Security-Policy, X-Frame-Options, X-XSS-Protection, Strict-Transport-Security, etc.