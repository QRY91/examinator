# Proefexamen Privacyensecurity Summary

## 📚 Study Questions & Answers

### 1. What is the advantage of an attacker over a defender in cybersecurity?

<details>
<summary>🤔 Click to reveal answer</summary>

In cybersecurity, the attacker has several advantages over the defender. Firstly, the attacker only needs to find one weakness to exploit, while the defender must secure all potential vulnerabilities. Secondly, the attacker has the element of surprise, as they can plan their attack without being detected until it's too late. Lastly, the attacker can often move quickly and adapt their tactics in response to defensive measures, making it challenging for defenders to keep up.

</details>

### 2. Give three examples of things that can threaten the availability of a system.

<details>
<summary>🤔 Click to reveal answer</summary>

Three examples of things that can threaten the availability of a system include Denial-of-Service (DoS) attacks, hardware failures, and ransomware infections. In a DoS attack, an attacker floods a network or server with traffic to make it unavailable to legitimate users. Hardware failures can occur due to aging equipment, power outages, or other technical issues. Ransomware is malicious software that encrypts a system's files and demands a ransom to decrypt them, effectively making the system unavailable until the ransom is paid.

</details>

### 3. What is the Bell LaPadula Model and how does it work?

<details>
<summary>🤔 Click to reveal answer</summary>

The Bell LaPadula Model is a security model used for enforcing the confidentiality of information in multi-level computer systems. It operates based on two principles: the simple integrity property, which states that no information may be replaced with lower-level information, and the stronger integrity property, which states that information cannot flow up to higher-level categories. The model includes three interacting layers: the subject (user), object (data or system), and security kernel (system software responsible for enforcing the rules).

</details>

### 4. How can you perform an XSS attack using simple HTML formatting on a blog website?

<details>
<summary>🤔 Click to reveal answer</summary>

To perform an XSS attack on a blog website, you could use HTML formatting to inject malicious scripts into comments. By doing so, you exploit vulnerabilities in the website's handling of user input, causing the site to execute your code instead of displaying the intended content. Your attempt might appear as unusual or unexpected behavior within the comment section, such as pop-ups, redirects, or stealing user data.

</details>

### 5. How would you protect a blog website against an XSS attack?

<details>
<summary>🤔 Click to reveal answer</summary>

To protect a blog website against an XSS attack, one approach is to sanitize and validate all user input before displaying it on the site. This can be achieved using techniques such as encoding special characters, escaping user-supplied JavaScript, and whitelisting allowed HTML tags and attributes. Additionally, ensuring the backend code properly handles user input and separates data from logic helps prevent potential XSS vulnerabilities.

</details>

### 6. What type of XSS attack is used in the given scenario?

<details>
<summary>🤔 Click to reveal answer</summary>

In the given scenario, the type of XSS attack being used is a Stored or Persistent Cross-Site Scripting (XSS) attack. This occurs when malicious code is inserted into the web application and stored for later use against unsuspecting victims. The attacker's script will execute every time someone views the compromised page, making it persistent until it is removed by an administrator or patch.

</details>

### 7. What is k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

K-anonymity is a method of data privacy protection that aims to ensure that individual records cannot be directly identified in a dataset. It achieves this by grouping similar records together so that each group contains at least k individuals with identical or nearly identical characteristics. The specific values of these characteristics are then replaced with generalized representations, such as age ranges or broad geographic locations, while maintaining enough information for analysis purposes.

</details>

### 8. How would you pseudonymize the given dataset to achieve a k-anonymity level of 3?

<details>
<summary>🤔 Click to reveal answer</summary>

To achieve a k-anonymity level of 3 in the given dataset, we would replace any sensitive data with generalized representations while ensuring that at least 3 similar records are grouped together. Here's an example of how the dataset might look after pseudonimization:
| Leeftijd | Zip-code   | Geslacht | Diagnose   |
|----------|-----------|---------|------------|
| [20-30]  | 35*       | f       | Darmkanker |
| [20-30]  | 36*       | m       | Griep      |
| [31-40]  | 36*       | m       | Tuberculosis|
| [31-40]  | 35*       | f       | AIDS       |
| [29-39]  | 3620     | m       | Bronchitis  |
* The zip code has been replaced with a generalized representation to protect privacy.

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**