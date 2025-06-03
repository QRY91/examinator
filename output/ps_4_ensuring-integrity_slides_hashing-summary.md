# Ps 4 Ensuring Integrity Slides Hashing - Study Guide

## Cryptography & Encryption
- **- Data**: - Hashes garanderen authenticatie in de vorm van certificaten en digitale handtekeningen.
- **Wat is**: - Het doel van hashing is het bewijzen dat data niet
- **- De waarde wordt een hash genoemd.**: - De hash garandeert integriteit van
- **- Dezelfde input genereert altijd dezelfde hash.**: - Als de input verandert, dan verandert de
- **Hoe werkt**: - Een hashfunctie werkt in blokken van een bepaalde grootte.
- **- Verschillende gebruikers hetzelfde wachtwoord (=**: hash) gebruikt en de database
- **Encrypt hash**: private key van signer ⇒ signature -
- **Hashing**: - HMAC / KHMAC (Keyed-Hash Message Authentication Code) - Niet enkel message door hash
- **Hash functies hebben**: oneindige hoeveelheid inputs, maar een eindig aantal outputs -> oneindig
- **- Werkt**: - Berekende hashes in de rainbow table kunnen
- **Output: 160-bit**: - SHA-2 (2001, kwetsbaar voor offline brute-force aanvallen) - Verzameling van 6 hash algoritmes die verschillende groottes van hashes maken: -
- **Gebaseerd op Blowfish algoritme (symmetrische encryptie)**: - Voordeel: moeilijker en trager parallel
- **Hashing algoritmes -**: - scrypt - Aanpasbaar algoritme: je kan de key derivation
- **Key Derivation Function:**: - Algoritme dat cryptografische key genereert uit password of een
- **Winnaar van 2015 Password Hashing Competition.**: - Vraagt nog meer RAM en VRAM (GPU) geheugen om te brute-

## General Security
- **= Message + H(k | m)**: = niet veilig voor Length
- **- File sharing**: gebruiken message digest om duplicate files
- **- Bruikbaarheid:**: - Integrity checks op bestanden of message digests!
- **Salt.**: - Cost: aantal iteraties, hoe meer -> hoe trager en
