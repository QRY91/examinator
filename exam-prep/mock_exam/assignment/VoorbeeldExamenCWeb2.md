**C# Web2: Voorbeeldexamen.**

In de opgave zitten 2 projecten. Jullie moeten een solution maken met beide projecten.

- Visual Studio – **PxlFund.Mvc**
    o ASP .Net Core MVC applicatie voor het beheer van bankfondsen
    o PXLFund_Mvc.zip
- Visual Studio – **PxlFund.Shared**
    o PxlFund_Shared.zip

```
1) Nuget Packages
Zorg dat je de nodige nuget packages offline kan installeren in je solution
2) Maak een werkende Solution met de 2 projectjen in bijlage.
3) Zorg voor de juiste project reference.
4) Voeg externe authenticatie toe en zorg ervoor dat je ook via de Google middleware kan
inloggen.
```
```
5) Maak de SQL server connectie actief in de ApplicationDbContext volgens de connection
string in je Appsettings bestand.
6) In je Program class moeten de services uit het Shared project geladen worden.
7) Zorg ervoor dat je solution kan builden en dat je project correct is.
8) Maak nu de de Bank, Fund en UserFundController
9) Voeg een migration toe en maak je databank aan!
```

10) In je service SeedDataRepository mogen jullie volgende functies activeren.

- AddBankInfo()
    i. KBC
ii. Argenta
- AddFundInfo()
    iii. KBC Green – KBC – 100 euro
    iv. KBC Yellow – KBC – 125 euro
       v. ARG Brown – Argenta – 135 euro
    vi. ARG Black – Argenta – 140 euro
11) SeedDataRepository – Identity
- Gebruik de ProjectSettings – ProgramInfo class
- AddRoles()
i. Admin
       ii. Client
- AddAdminUser()
iii. Username: admin
iv. Email: admin@pxl.be
v. Password: Adm!n
12) Pas de UserLoginRepository aan.
a. External login
b. Normal login
13) Voeg een REST webapi functionaliteit toe aan je project
a. localhost:5000/api/FundInfo
i. HttpGet
1. BankName – FundName – FundValue
b. localhost:5000/api/Fund/KBC
i. HttpPost
1. Add Fund for bank KBC
14) Blazor
- Maak een blazor component voor een record toe te voegen in de userfund tabel.
- Maak een blazor component voor een overzicht te maken voor al de fondsen van de
gebruiker die is ingelogd.