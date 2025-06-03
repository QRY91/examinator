# Cryptography Steganography Exam Guide - Study Guide

## Cryptography & Encryption
- **RSA**: Most common public-key algorithm,
- **ECC (Elliptic Curve)**: More efficient than RSA, smaller key
- **Key P**: Public key (shareable) and private key (secret)
- **SHA-256**: Secure Hash Algorithm, produces 256-
- **HMAC**: Hash-based Message Authentication C
- **Key G**: Using cryptographically
- **Key S**: Hardware Security Modules (HSMs)
- **Key R**: Regular changing of
- **HTTPS/TLS**: Web traffic encryption using certificates
- **Brute F**: Trying all possible keys
- **Perfect Forward S**: Session keys not compromised if long-
- **Quantum Key D**: Using quantum mechanics for ultra-
- **- Key E**: - Afhankelijk van de lengte van de key worden er meerdere rounds gedaan - 128 => 10 rounds - 192 => 12 rounds - 256 => 14 rounds Chapter 3: Protecting Secrets - Moderne C
- **Asymmetrisch - RSA**: - RSA (ontworpen door Ron Rivest, Adi Shamir en Len Adleman) - Gebaseerd op de moeilijkheid van het factoriseren van een product van twee heel grote priemgetallen - Gebruikt voor public & private key encryption - RSA wordt gebruikt in TLS, openSSL, … Chapter 3: Protecting Secrets - Moderne C
- **Data in transit ⇒**: → use public key cryptography to
- **Bob decrypts using the**: After Bob obtains Alice’s public key, he uses it to decrypt the message and to
- **Key exchange - Diffie H**: = 15 = 315 mod 17 = 6 = 6 = 13 = 6 3 mod 17 3 mod 17 3 mod 17 = 313 mod 17 = 12 = 12 = 12 1215 mod 17 = 10 613 mod 17 = 10 Chapter 3: Protecting Secrets - Moderne C
- **- Als Omer**: deel (blauw + rood) signeert met zijn private key,
- **Omer kwam.**: - Bovendien kan Bram niet zijn bericht onderscheppen en aanpassen, aangezien Bram de private key niet heeft van O
- **- De S staat**: - Wanneer er een HTTPS connectie wordt opgezet tussen client en server, wordt er een protocol gevolgd waarmee beide partijen elkaar authenticeren en een key
- **- Encryptie (encryption):**: - Het versleutelen van de plaintext
- **- Key:**: - Sleutel die enkel gedeeld is
- **Encryption, hashing**: Involves encoding data so that it can only be accessed by those who have the key.
- **Involves calculations that cannot be reversed.**: Involves adding random data before it is put through a cryptographic hash function.
- **- Data anonymization:**: - Maak gebruik van blanking, hashing of masking van persoonlijke identifiers -> het doel is om de oorspronkelijke eigenaar niet meer te kunnen identificeren.
- **// Instellen van de primary key.**: // // Meerdere kolommen kunnen samen de primary key vormen // daarom werk je met een array.
- **WEP**: - WEP gebruikt een key voor encryptie (stream cipher: RC4)
- **De sleutel is statisch.**: WEP heeft ernstige problemen met de initialization vector (IV) die een belangrijke component is in cryptografische systemen (denk aan AES) - De IV-key is een 24-bit field (te klein)
- **Verbeterde protocols om WEP**: - Grotere keys die nieuwe keys kunnen genereren voor elk
- **No encryption for**: - Attacker only needs to know the victim'
- **Altijd**: gebruiken in plaats van enkel encryption -
- **De hacker kan credentials stelen via:**: - Toestaan van zwakke wachtwoorden (“Test123”, “Password1”, …) - Gebruik maken van zwakke credential recovery (op basis van vragen) - Zwakke wachtwoord hashes of plain text wachtwoorden -
- **- D**: - Hashes garanderen authenticatie in de vorm van certificaten en digitale handtekeningen.
- **Wat**: - Het doel van hashing is het bewijzen dat
- **- De waarde wordt een hash genoemd.**: - De hash garandeert
- **- Dezelfde input genereert altijd dezelfde hash.**: - Als de input verandert, dan
- **Hoe**: - Een hashfunctie werkt in blokken van een bepaalde grootte.
- **Encrypt**: private key van signer ⇒ signature -
- **Hash functies**: oneindige hoeveelheid inputs, maar een eindig aantal outputs ->
- **- W**: - Berekende hashes in de rainbow
- **Output: 160-**: - SHA-2 (2001, kwetsbaar voor offline brute-force aanvallen) - Verzameling van 6 hash algoritmes die verschillende groottes van hashes maken: -
- **Hashing algoritmes -**: - scrypt - Aanpasbaar algoritme: je kan de
- **Key Derivation Function:**: - Algoritme dat cryptografische key genereert uit password
- **Winnaar van 2015 Password Hashing Competition.**: - Vraagt nog meer RAM en VRAM (GPU) geheugen om te brute-
- **Activity tracker, zoekgeschiedenis, wachtwoorden,**: toetsaanslagen (keystrokes), etc.
- **- Afluisteren van keystrokes, wachtwoorden**: property - Spyware en Adware is meestal eenvoudig om te verwijderen:

## General Security
- **- Sleutelwoord: PXL**: - sleutel uitbreiden en opsplitsen ≈
- **- Encoding =/=**: - geeft aan hoe data moet worden uitgelezen - probeert
- **Encoding.Default.GetBytes(tekst);**: // returns byte[] // Test het omzetten van bytes

## Web Application Attacks
- **- De standaard encoding op het web.**: - Internet ontstaat -> Unicode Consortium heeft een standaard voor ieder bestaand karakter gemaakt ( > 143,859 karakters) - Probleem 1: Deze hoeveelheid karakters kan niet gemapt worden, zoals ASCII, want
