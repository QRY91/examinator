# PS 3 Protectingsecrets Slides Klassieke Encryptie 2025 Summary

## 📚 Study Questions & Answers

### 1. What is the purpose of studying classical cryptography?

<details>
<summary>🤔 Click to reveal answer</summary>

The study of classical cryptography provides a better understanding of how modern cryptosystems are constructed. It is not secure to encrypt text today with these methods, but they offer an ideal way to practice programming skills and use letters instead of bits. Substitution and Transposition techniques used in modern encryption are also included in this topic.

</details>

### 2. Explain the concept of simple substitution in cryptography.

<details>
<summary>🤔 Click to reveal answer</summary>

Simple substitution is a process where each character in the plaintext is replaced with another predefined substitute (replacement). For example, the Caesar Cipher falls under this category. In this method, every letter in the plaintext is shifted a certain number of places down or up the alphabet.

</details>

### 3. What is ROT13 and how does it work?

<details>
<summary>🤔 Click to reveal answer</summary>

ROT13 stands for a Caesar rotation with a shift of 13 letters. In ROT13, every letter in the plaintext is shifted 13 places down the alphabet (wraparound occurs at both ends). For example, 'hello' becomes 'ubfgyhq'.

</details>

### 4. Describe monoalphabetic substitution with a random alphabet.

<details>
<summary>🤔 Click to reveal answer</summary>

In a monoalphabetic substitution with a random alphabet, there is a complete random mapping between letters of the original alphabet and the replacement alphabet. This creates an entirely new encryption system that changes every time it's used. The key to decrypting this message would be knowing the specific correspondence between the two alphabets.

</details>

### 5. What is the Playfair cipher and how does it work?

<details>
<summary>🤔 Click to reveal answer</summary>

The Playfir cipher is a polyalphabetic substitution method that involves splitting the plaintext into bigrams (pairs of letters) and creating a 5x5 grid with no identical letters. Encryption is done by replacing each pair in the plaintext according to the rules defined for the grid, such as pairing letters on the same row, column, or diagonal.

</details>

### 6. How do you fill out the Playfair cipher grid?

<details>
<summary>🤔 Click to reveal answer</summary>

To create the Playfair cipher grid, first, write the alphabet horizontally and vertically with no repetitions. If there are fewer than 26 unique letters in the plaintext, add 'X' or 'Y' to make a full 5x5 matrix. Fill any remaining spaces with the most common letter that hasn't already been used.

</details>

### 7. Describe how to encrypt using the Playfair cipher.

<details>
<summary>🤔 Click to reveal answer</summary>

To encrypt using the Playfair cipher, first split the plaintext into bigrams and create the grid if necessary. Then, apply the following three rules when replacing the pairs: (1) If letters are on the same row, replace them with the corresponding letters in the same column. (2) If letters are on the same column, replace them with the corresponding letters in the same row. (3) If letters form a diagonal pair, replace each letter with the opposite corner letter of the grid.

</details>

### 8. Explain the concept of Transposition ciphers.

<details>
<summary>🤔 Click to reveal answer</summary>

Transposition ciphers involve rearranging the letters within the plaintext while preserving the individual characters themselves. This method doesn't change the original characters but changes their relative positions to create a new message that only the intended receiver can decipher using the key.

</details>

### 9. What is the difference between classical and modern cryptography?

<details>
<summary>🤔 Click to reveal answer</summary>

The main differences between classical and modern cryptography are the use of letters instead of bits, a lack of computational complexity in classical methods, and the reliance on simpler, easily breakable techniques such as Caesar rotation and transposition. Modern encryption algorithms are more complex and computationally intensive, making them significantly harder to crack without proper knowledge or tools.

</details>

### 10. Why is padding necessary in cryptography?

<details>
<summary>🤔 Click to reveal answer</summary>

Padding is used to ensure the correct size for an encrypted message when it doesn't have a specific length requirement. It prevents issues with encryption algorithms that may not process messages of varying lengths correctly, leading to errors or unintended results.

</details>

### 11. What are some advantages of using classical cryptography over modern methods?

<details>
<summary>🤔 Click to reveal answer</summary>

Classical cryptography provides a solid foundation for understanding more complex encryption systems and techniques. Additionally, it can be used as an introductory exercise for beginners in the field of cryptography to develop fundamental concepts and skills related to encryption, decryption, and key management.

</details>

### 12. What are some disadvantages of using classical cryptography?

<details>
<summary>🤔 Click to reveal answer</summary>

The main disadvantage of using classical cryptography is its lack of security against modern attack methods. These methods were designed to protect communication at a time when computation was limited, making them vulnerable to current computing capabilities. Another disadvantage is that classical encryption can be easily broken with brute force or frequency analysis techniques.

</details>

### 13. How does frequency analysis work in cryptanalysis?

<details>
<summary>🤔 Click to reveal answer</summary>

Frequency analysis involves examining the distribution of characters and patterns within a ciphertext to deduce the underlying plaintext. The assumption is that common letters in the original language will have higher frequencies in the ciphertext as well, making it easier to decrypt or guess the key used for encryption.

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**