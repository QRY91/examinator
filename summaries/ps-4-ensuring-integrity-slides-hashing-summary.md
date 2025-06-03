# 🎯 Ps 4 Ensuring Integrity Slides Hashing - Study Guide
*Generated from: PS_4_Ensuring Integrity_Slides_Hashing.pdf*

**Q: What is hashing and what is its purpose?**
A: Hashing is a process that generates a unique digital fingerprint (hash) for data, with the primary purpose of proving that the data hasn't been altered. It plays a crucial role in information assurance by ensuring the integrity of communication and data storage.

**Q: How does a hash function work?**
A: A hash function works by processing data in blocks of a specific size (e.g., SHA-1 works in 512-bit blocks). If the data is not a multiple of this size, it is padded to meet the requirement. Each block is then processed through the hash function, and the resulting hash of each block becomes an input for the next block until the entire data is hashed.

**Q: What is the avalanche effect in hashing?**
A: The avalanche effect refers to the fact that even small changes in the input can result in significant differences (a "avalanche") in the resulting hash value. This property ensures that any modifications to the data will be detected as changes in the hash value.

**Q: What is the difference between hashing and encryption?**
A: Hashing and encryption are not the same. In hashing, the process is one-way, meaning it can only be done in one direction (from input to output). Encryption, on the other hand, allows data to be encrypted for secure transmission and then decrypted upon receipt.

**Q: What is salting in hashing?**
A: Salting is a method used to add a random string (salt) to the original data before generating the hash. This ensures that each user's stored hash is unique, making it more difficult for attackers to crack hashed passwords if a database leak occurs.

**Q: What are some common applications of hashing?**
A: Hashing is commonly used in communication protocols, data storage systems, and for storing passwords securely. It is also used in cryptographic algorithms and digital signatures.

**Q: Why is it important to use a unique salt for each user's data during salting?**
A: Using a unique salt for each user ensures that even if the same password is used by multiple users, their stored hashes will still be different due to the addition of the unique salt. This makes it more difficult for attackers to crack stored passwords.

**Q: What are some possible attacks against hashed data?**
A: Possible attacks against hashed data include dictionary attacks (attempting common words or patterns as passwords) and brute-force attacks (trying all possible combinations of characters). Salting can help mitigate these types of attacks by making it more difficult for attackers to find matching plaintext and hash pairs.

**Q: What is padding in hashing?**
A: Padding is the additional data added to the input when the data size is not a multiple of the hash function's block size. This ensures that all inputs are processed consistently, regardless of their original size.

**Q: How does an attacker crack a salted password hash?**
A: An attacker would need to determine both the plaintext (password) and the salt used in hashing the password to crack a salted password hash. This can be done through various methods, such as brute-force attacks or dictionary attacks, but the added complexity of the unique salt makes it more difficult for an attacker to successfully crack the stored passwords.

**Q: Why is it important to use strong and unique passwords?**
A: Using strong and unique passwords helps protect against various types of attacks, such as brute-force and dictionary attacks. By having a strong and unique password, the chances of an attacker successfully cracking your password are greatly reduced.

**Q: What is the impact of using weak passwords in hashed data?**
A: Using weak passwords can make it easier for attackers to crack stored password hashes. If multiple users use the same weak password, a single compromised hash could potentially reveal all matching plaintext passwords, posing a security risk for all affected users.

**Q: What is the purpose of storing both the salt and the resulting hash?**
A: Storing both the salt and the resulting hash allows the system to verify the correctness of the user's input during login attempts by regenerating the stored hash using the provided password and the salt. This way, even if the original password is unknown, the system can still confirm whether the entered password is correct by comparing the generated hash with the stored one.

**Q: How does salting help in the event of a database leak?**
A: In the event of a database leak, salting makes it more difficult for attackers to crack passwords as they would need to obtain both the salt and the stored hashes for each user. This added complexity increases the time and resources required to crack the passwords, potentially delaying or preventing an attacker from gaining unauthorized access to user accounts.

**Q: Why is it important to focus on exam-relevant material when studying for a security exam?**
A: Focusing on exam-relevant material ensures that you are studying topics that will likely appear on the exam, maximizing your chances of success. By understanding the key concepts and procedures related to hashing, salting, and password storage, you can improve your knowledge and skills in the area of computer security and be better prepared for a security exam.