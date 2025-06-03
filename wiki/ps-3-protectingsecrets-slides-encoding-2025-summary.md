# PS 3 Protectingsecrets Slides Encoding 2025 Summary

## 📚 Study Questions & Answers

### 1. What is the main focus of Chapter 3: Confidentiality - Encoding?

<details>
<summary>🤔 Click to reveal answer</summary>

The main focus of Chapter 3 is to explain different methods of encoding data, specifically binary, hexadecimal, Base64, and text encodings such as ASCII and UTF-8.

</details>

### 2. What is binary in the context of computing?

<details>
<summary>🤔 Click to reveal answer</summary>

Binary refers to the base-2 number system that computers use, consisting only of 0s and 1s.

</details>

### 3. What is a hexadecimal digit and what are its values?

<details>
<summary>🤔 Click to reveal answer</summary>

A hexadecimal digit is one of the digits used in the base-16 numeral system. The digits include 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. In hexadecimal, A = 10, B = 11, C = 12, D = 13, E = 14, and F = 15.

</details>

### 4. How do we represent a hexadecimal number in code?

<details>
<summary>🤔 Click to reveal answer</summary>

In code, we use the prefix "0x" to denote a hexadecimal number. For example, 0xC0DE is represented as a hexadecimal number.

</details>

### 5. Explain how to convert a hexadecimal number into decimal.

<details>
<summary>🤔 Click to reveal answer</summary>

To convert a hexadecimal number into decimal, we multiply each digit by its power of 16 (from the right) and sum up the results. For example, 0xC0DE = (12 * 16^3) + (0 * 16^2) + (13 * 16^1) + (14 * 16^0) = 49152 + 0 + 208 + 14 = 49374.

</details>

### 6. What is Base64 and what is it used for?

<details>
<summary>🤔 Click to reveal answer</summary>

Base64 is a binary-to-text encoding scheme that allows for the representation of binary data in ASCII characters. It is commonly used to encode binaire data within web pages, store images and sounds as text, and encrypt messages using digital keys.

</details>

### 7. What are the 64 characters used in Base64?

<details>
<summary>🤔 Click to reveal answer</summary>

The 64 characters used in Base64 are a combination of alphabetical letters (both lowercase and uppercase), numbers, and special characters such as + and /. These characters are commonly found in most character sets, allowing data to be transmitted without corruption.

</details>

### 8. How do we convert binary data into Base64?

<details>
<summary>🤔 Click to reveal answer</summary>

Converting binary data into Base64 involves breaking the binary data into 24-bit segments (or 3 bytes), and then converting each segment into a Base64 character using a lookup table. The resulting output consists of 4 encoded characters per 3 input bytes.

</details>

### 9. What is ASCII and why is it significant?

<details>
<summary>🤔 Click to reveal answer</summary>

ASCII stands for the American Standard Code for Information Interchange. It is a character encoding standard that assigns a unique 7-bit code to each character. Although originally designed to transmit data using 7-bit bytes, it is now most commonly transmitted as 8-bit bytes due to modern standards.

</details>

### 10. What are some practical uses of ASCII?

<details>
<summary>🤔 Click to reveal answer</summary>

ASCII is widely used in computer systems for text representation and communication. It is used by virtually all modern computing systems and the Internet for the representation of text.

</details>

### 11. What is UTF-8 and how does it differ from ASCII?

<details>
<summary>🤔 Click to reveal answer</summary>

UTF-8 stands for Unicode Transformation Format - 8 bits. It is a character encoding that supports most languages in the world, extending the range of characters beyond the 128 ASCII codes. UTF-8 allows text files to be compatible with both ASCII and other character sets without needing to specify the character set in advance.

</details>

### 12. How does IPv6 address use hexadecimal?

<details>
<summary>🤔 Click to reveal answer</summary>

IPv6 addresses consist of 128 bits and are often represented using hexadecimal format (0xABCD:EF01:2345:6789:1122:3344:5566:7777). Each pair of 4 hexadecimal digits represents 16 bits, or 2 bytes.

</details>

### 13. What is the purpose of converting decimal numbers to hexadecimal?

<details>
<summary>🤔 Click to reveal answer</summary>

Converting decimal numbers to hexadecimal makes it easier for humans to read and understand binaire data, particularly when dealing with large or complex values in a compact format. It is also useful for working with IPv6 addresses and other technologies that use hexadecimal notation.

</details>

### 14. Provide an example of a Base64 encoded string.

<details>
<summary>🤔 Click to reveal answer</summary>

Here's an example of a Base64 encoded string: "SGVsbG8sIHdvcmxkLg==" corresponds to the binary data 01010101 01101111 01111010 01100101, which in ASCII represents the text "Hello World".

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**