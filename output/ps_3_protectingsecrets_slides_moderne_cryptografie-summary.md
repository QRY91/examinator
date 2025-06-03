# Ps 3 Protectingsecrets Slides Moderne Cryptografie - Study Guide

## Cryptography & Encryption
- **Symmetrisch - XOR**: - Bij symmetrische encryptie wordt vaak de XOR functie gebruikt, omdat deze
- **- AES wordt ook Rijndael**: - Uitgekozen als winnaar door National Institute of Standards and Technology om de nieuwe encryptie standaard te worden.
- **Symmetrisch - AES**: - Het proces verloopt in het 4*4 byte grid = 128 bits Chapter 3: Protecting Secrets - Moderne C
- **- Key E**: - Afhankelijk van de lengte van de key worden er meerdere rounds gedaan - 128 => 10 rounds - 192 => 12 rounds - 256 => 14 rounds Chapter 3: Protecting Secrets - Moderne C
- **Asymmetrische**: - Private, public key vergelijking: Je adresseert brieven door ze te versleutelen met de public key, enkel de private key kan
- **- Bijvoorbeeld:**: Chapter 3: Protecting Secrets - Moderne Cryptografie 3 (mod 17) ☰ 3 9 (mod 17) ☰ 9 27(mod 17) ☰ 3 81 (mod 17) ☰ 13 243 (mod 17) ☰ 5 729 (mod 17) ☰ 15
- **Asymmetrisch - RSA**: - RSA (ontworpen door Ron Rivest, Adi Shamir en Len Adleman) - Gebaseerd op de moeilijkheid van het factoriseren van een product van twee heel grote priemgetallen - Gebruikt voor public & private key encryption - RSA wordt gebruikt in TLS, openSSL, … Chapter 3: Protecting Secrets - Moderne C
- **Elliptic-curve cryptography (ECC)**: - Als een rechte lijn door twee punten gaat, dan zal het een derde punt kruisen.
- **Data in transit ⇒**: → use public key cryptography to exchange the
- **Bob decrypts using the public**: After Bob obtains Alice’s public key, he uses it to decrypt the message and to authenticate that
- **Key exchange - Diffie H**: = 15 = 315 mod 17 = 6 = 6 = 13 = 6 3 mod 17 3 mod 17 3 mod 17 = 313 mod 17 = 12 = 12 = 12 1215 mod 17 = 10 613 mod 17 = 10 Chapter 3: Protecting Secrets - Moderne C
- **- Als Omer zijn**: deel (blauw + rood) signeert met zijn private key, dan
- **Omer kwam.**: - Bovendien kan Bram niet zijn bericht onderscheppen en aanpassen, aangezien Bram de private key niet heeft van O
- **- De S staat voor**: - Wanneer er een HTTPS connectie wordt opgezet tussen client en server, wordt er een protocol gevolgd waarmee beide partijen elkaar authenticeren en een key afspreken voor

## General Security
- **- De operatie wordt uitgevoerd per bit.**: Chapter 3: Protecting Secrets - Moderne C
- **- Block**: - Plaintext wordt opgedeeld in 64 bit input => 64 bit output - 16 stages/rounds waarbij elke keer de sleutel
- **- Modulair rekenen: Rekenen met een bovengrens.**: (15 mod 12 = 3) Chapter 3: Protecting Secrets - Moderne C
- **Voorbeelden:**: 26 (mod 12) ☰ 2 10 (mod 12) ☰ 10 50 (mod 12) ☰ 2 26 (mod 8) ☰ 2 13 (mod 8) ☰ 5 257 (mod 8) ☰ 1
- **(Decrypt) = C**: Example: Data exchange between Bob and A
