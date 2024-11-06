# Gegevensbeheer / Database Tool voor Damesvolleybal Promo 2
Deze tool is ontworpen om gegevens weer te geven uit de fictieve database van Damesvolleybal in Promo 2. Naast het tonen van de gegevens biedt de tool ook de mogelijkheid om gegevens naar een CSV-bestand te exporteren, toekomstige datums te filteren en scores aan te passen.
## Installatie van tool
### Database
Om de database correct te laten werken, moet de naam van het databasebestand worden opgegeven via een .env-bestand dat je zelf aanmaakt. Dit bestand moet in de config folder komen te staan. 
```md
.
└── config/
    ├── __pycache__
    ├── .env
    ├── config.py
    └── __init__.py
```
In dit bestand voeg je de onderstaande variabele toe (.env bestand):    
```python
DB_PATH="jouw_database_bestand.db"
```
Plaats de database in de hoofdmap, dezelfde map waarin main.py zich bevindt.

### Vereiste packages
Alle benodigde packages zijn te vinden in requirements.txt.

## Weergeven van Alle wedstrijden / geplande wedstrijden
Vanuit het hoofdmenu kan je kiezen om alle matchen of enkel de toekomstige matchen te weergeven.
Bij het weergeven is het mogelijk om een export te doen naar een CSV-bestand. Het bestand is afhankelijk van de gekozen optie vanuit het hoofdmenu.

![readme5](https://github.com/user-attachments/assets/3e34799f-b8b6-481f-9bad-d8ad5a082fb3)



## CSV Bestanden
De CSV-bestanden worden opgeslagen in dezelfde map als het bestand main.py. Tijdens het opslaan wordt er gecontroleerd of het bestand al bestaat. In dat geval wordt er gevraagd of je het bestand wilt overschrijven.

![readme4](https://github.com/user-attachments/assets/93b59692-e4e4-477b-8cdf-cf8e3fbcc4db)


## Aanpassen van score
Het aanpassen van de scores is geïntegreerd in de functionaliteit en kan gedaan worden door de menu’s te doorlopen en de gewenste gegevens in te voeren.

![readme](https://github.com/user-attachments/assets/63fbaa4e-6957-4e7a-9d62-7ee1a6048189)
