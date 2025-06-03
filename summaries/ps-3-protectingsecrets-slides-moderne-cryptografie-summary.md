# 🎯 Ps 3 Protectingsecrets Slides Moderne Cryptografie - Study Guide
*Generated from: PS_3_ProtectingSecrets_Slides_Moderne_Cryptografie.pdf*

**Q: What is modern cryptography and why is it more complex than classical encryption algorithms?**
A: Modern cryptography refers to the current state of encrypting data, which is much more complex than traditional methods due to its reliance on mathematical problems that are difficult for computers to solve. The security of these modern algorithms primarily depends on good key management rather than attacking the algorithm itself.

**Q: What is symmetric encryption and what are some examples?**
A: Symmetric encryption, also known as private-key encryption, focuses on quick encryption methods using the same key for both encrypting and decrypting data. Examples of symmetric encryption include DES, 3DES, AES, stream ciphers like RC4, Salsa20 (not covered in this material), and block ciphers.

**Q: Explain the XOR function used in symmetrical encryption.**
A: The XOR function is a binary operation that is often used in symmetric encryption because it's reversible. It returns 1 when one bit is different between the two inputs, otherwise it returns 0. This operation is carried out per bit.

**Q: What are stream ciphers and block ciphers?**
A: Stream ciphers work on a single bit at a time while block ciphers operate on blocks of data. Stream ciphers generally require less computation time but more code, whereas block ciphers require more time but less code and offer more diffusion.

**Q: What is the Data Encryption Standard (DES) and how does it work?**
A: The Data Encryption Standard (DES) is an older symmetric encryption algorithm that was widely used until newer alternatives were developed. It divides the plaintext into 64-bit input and produces 64-bit output, going through 16 stages or rounds where the key is modified at each stage.

**Q: What are the advantages of AES over DES?**
A: Advanced Encryption Standard (AES) is a more modern symmetric encryption algorithm that offers several improvements over DES. It has a larger block size (128 bits), uses three different keys with lengths of 128, 192 or 256 bits, and features both diffusion and confusion to make the relationship between key and ciphertext as complex as possible.

**Q: What is the difference between a plaintext, ciphertext, and key in symmetric encryption?**
A: The plaintext is the original, readable data before it has been encrypted. The ciphertext is the encrypted data that appears random and unreadable. The key is a secret value used to both encrypt and decrypt the data.

**Q: What is confusion and diffusion in symmetric encryption?**
A: Confusion refers to making the relationship between the key and the ciphertext as complex as possible, while diffusion means that when one bit in the plaintext changes, multiple parts of the ciphertext also change.

**Q: How many rounds does AES have for encryption?**
A: AES performs its encryption process in 10 rounds by operating on a 4x4 byte grid (128 bits).

**Q: What is 3DES and how is it different from DES?**
A: 3DES, or triple DES, is an improved version of the Data Encryption Standard (DES) that enhances security by encrypting data three times with three separate keys. Unlike traditional DES, which uses a single key throughout the encryption process, 3DES improves its security through using multiple keys.

**Q: What is the difference between AES and Rijndael?**
A: AES (Advanced Encryption Standard) is also known as Rijndael, named after its inventors Vincent Rijmen and Joan Daemen. It was chosen as the new encryption standard by the National Institute of Standards and Technology (NIST).

**Q: What is a practical application for symmetric encryption?**
A: Symmetric encryption has numerous applications in secure communication, such as encrypting sensitive data like passwords, financial transactions, or confidential emails.

**Q: What is an advantage of using AES over older encryption algorithms?**
A: One advantage of using AES over older encryption algorithms like DES is that it offers improved security through increased key size and more rounds of computation.

**Q: What is asymmetric encryption, and how does it differ from symmetric encryption?**
A: Asymmetric encryption, or public-key cryptography, uses two different keys for encrypting and decrypting data. It is less efficient in terms of computational time but offers advantages like key exchange without the need for a pre-existing shared secret. Examples include RSA and Elliptic Curve Cryptography (ECC).

**Q: How does public-key cryptography work?**
A: Public-key cryptography uses a pair of keys, one for encryption and one for decryption. Data encrypted with the recipient's public key can only be decrypted using their private key, ensuring secure communication between parties that do not share a pre-existing secret.