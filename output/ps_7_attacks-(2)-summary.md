# Ps 7 Attacks (2) - Study Guide

## Cryptography & Encryption
- **VPN**: Bijvoorbeeld HTTP en FTP is niet ge-encrypteerd.
- **WEP**: - WEP gebruikt een key voor encryptie (stream cipher: RC4)
- **De sleutel is statisch.**: WEP heeft ernstige problemen met de initialization vector (IV) die een belangrijke component is in cryptografische systemen (denk aan AES) - De IV-key is een 24-bit field (te klein)
- **Verbeterde protocols om WEP te**: - Grotere keys die nieuwe keys kunnen genereren voor elk pakket dat
- **WPA2**: - WPA2 gebruikt de sterkste encryptie methode: AES - Is kwetsbaar aan cyber attacks via oude wireless protocols: (WPA en WEP), omdat de meeste routers ook connectie voorzien via “oude” protocols.
- **No encryption for this**: - Attacker only needs to know the victim'
- **Verouderde versleutel algoritmes gebruiken, zoals DES**: - Het gebrek van een versleutel algoritme gebruiken, geen encryptie -
- **Altijd authenticated**: gebruiken in plaats van enkel encryption -
- **Encrypteer de gevoelige**: - Argon2, scrypt, bcrypt or PBKDF2 voor wachtwoorden,
- **De hacker kan credentials stelen via:**: - Toestaan van zwakke wachtwoorden (“Test123”, “Password1”, …) - Gebruik maken van zwakke credential recovery (op basis van vragen) - Zwakke wachtwoord hashes of plain text wachtwoorden -
- **Directory T**: Met Directory Traversal kunnen hackers toegang krijgen tot privé files van de website waar gevoelige data in wordt bewaard.
- **Unencrypted C**: - Wanneer data niet geëncrypteerd verstuurd wordt, dan kan alle data ge-sniffed worden door hackers (inclusief logingegevens)
- **Limiteer resources, rekenkracht,**: aantal request per gebruiker - Verwerk security checks in het design op verschillende niveaus, zowel front-
- **Tools used in (web)**: Every modern web browser includes a powerful suite of
- **Browser development console (F12)**: Elements/Inspector: Provides the ability to inspect CSS and HTML code as well as edit CSS on-the-fly, seeing the effects of your changes in

## Network Attacks
- **Distributed Denial of S**: - Denial-of-Service (DoS) attacks zijn een soort
- **Hoe wordt een DDos attack**: - Gebruik van een Botnet (zie vorige les)
- **Attack tools.**: In DDos aanvallen worden Bots gebruikt om op hetzelfde moment aan
- **- Spoofing is een impersonation attack.**: - Spoofing exploits de vertrouwde relatie tussen twee systemen.
- **Replay**: Een replay attack doet zich voor wanneer de aanvaller een deel van de communicatie tussen twee partijen onderschept en de opgevangen boodschap opnieuw doorstuurt.
- **Page 51**: - Maak gebruik van de security protocols die er bestaan Ook al zijn WEP en WPA niet perfect: slechte bescherming is nog steeds beter dan
- **- MAC adres identificeert het toestel.**: - Systemen bewaren een ARP tabel waarin IP adressen aan MAC adressen zijn gekoppeld in de ARP Tabel.
- **- Communiceren naar IP 10.0.0.4:**: Systeem checkt ARP tabel voor MAC van IP a.
- **Hoe werkt DNS?**: Vraag aan ISP of die de URL

## General Security
- **- Amplification attack:**: - Een aanval waarbij de aanvaller een kleine hoeveelheid resources gebruikt om een grote hoeveelheid resources
- **Slachtoffer klikt op kwaadaardige link**: voert acties uit voor de attacker -
- **Altijd API endpoints**: - controle moet altijd (ook) server-side gebeuren -
- **Do’s:**: - Verwijder alle ongebruikte dependencies, features, componenten, files - Controleer de versies van alle componenten en log wanneer componenten out of date zijn -
- **Veilige code schrijven:**: - alle input van users als
- **Kan eenvoudig geblokkeerd worden,**: er maar één aanvallend
- **- Wanneer twee systemen communiceren over**: lokale netwerk, dan delen ze het MAC adres met elkaar
- **De query heeft een id.**: - Antwoord op de query heeft
- **Aanvaller luistert query id’s af.**: - Aanvaller incrementeert afgeluisterde query id’s en spamt neppe antwoorden.
- **- Timestamps:**: Een boodschap wordt bestempeld met een timestamp die aangeeft wanneer de ontvanger het bericht
- **MAC**: - Can be used to Deny Service (Jamming) - Force client to handshake again to the REAL
- **Access Point to capture**: - Force client to handshake against a ROGUE
- **Limiteer het plaatsen van access**: De access points zouden buiten het beschermde netwerk
- **SQL**: - XPath queries (selectie in een XML document) -
- **Mixed mode testing:**: - automatische bulk testen op generische kenmerken -
- **Onnodige extra features**: ingeschakeld zijn (open poorten, services, pages, accounts, …) - Default accounts en wachtwoorden zijn nog actief
- **Thresholds en escalatie goed**: - Regelmatige (security) testen die ook de alerting testen -
- **Executing and debugging JavaScript**: - Showing which assets the page has requested and how long they took to load.
- **- Can see sent headers, params, …**: - contains information/data stored in
- **Bv: <img src="/loadImage?filename=218.png">**: - In het bovenstaande voorbeeld neemt de loadImage pagina
- **Geïnjecteerd script**: naar server, maar uitgevoerd in browser.
- **Geïnjecteerd**: opgeslagen op database van server.
- **Hello, John!**: - De PHP code op de server ziet er bijvoorbeeld zo uit: -
- **Code I**: - SQL of XML statements ingeven in tekstvelden
- **Input valideren, SQL**: - Programmeurs moeten SQL parameters gebruiken of
- **Prepared Statements gebruiken Parameterized Q**: Als een aanvaller de gebruikersnaam bob' or '1'='1 zou ingeven, dan zou de parameterized query niet kwetsbaar zijn en zoeken naar een gebruikersnaam die letterlijk overeenkomt met de tekst bob' or '1'='1.
- **SQL parameters/prepared statements,...**: - Alle software (OS, applicaties) up to

## Web Application Attacks
- **Disable web server directory**: - Log access control failures, op tijd alarm slaan!
- **Highjacking van user**: - Websites te beschadigen of aan te passen - Gebruikers misleiden naar andere sites en ongewenste acties uit te voeren.
- **Normaal gebruik:**: - Stel je surft naar http://mydomain.com/hello.php?user=John en je krijgt de tekst: -
- **Of gebruikt de volgende URL:**: - http://mydomain.com/hello.php?user=<script>alert(1)</script> -
- **van websites naar IP adressen.**: - Proces dat van achter naar voor werkt door de URL
- **Hacker valt aan door middel**: - forced browsing, url tampering - brute force techniek naar unlinked content - de inhoud van body in http request aan te passen - parameter mining/discovery - Het ontdekken van (debug/develop) parameters in requests die verborgen zijn, maar wel geaccepteerd worden door de server en het gedrag van de applicatie
- **(Web)Server**: - https://securityheaders.io - ...
- **Cross-Site Scripting (XSS)**: Cross-site scripting laat een hacker toe om: -
- **libraries van .NET, PHP,...)**: https://www.w3schools.com/sql/sql_injection.
- **https://www.w3schools.com/code/tryit.asp?filename=G1UDZXAOMKYS**: https://www.hacksplaining.com/exercises/sql-
