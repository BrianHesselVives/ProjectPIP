# Gegevensbeheer / Database Tool voor Damesvolleybal Promo 2
Deze tool is ontworpen om gegevens weer te geven uit de fictieve database van Damesvolleybal in Promo 2. Naast het tonen van de data, biedt de tool ook de mogelijkheid om alle gegevens te exporteren naar een CSV-bestand. Daarnaast kun je eenvoudig toekomstige datums filteren en deze exporteren.
## CSV Bestanden
De CSV-bestanden worden opgeslagen in dezelfde map als het bestand main.py. Tijdens het opslaan wordt er gecontroleerd of het bestand al bestaat. In dat geval wordt er gevraagd of je het bestand wilt overschrijven.
![readme3](https://github.com/user-attachments/assets/b410b71e-0e67-49c8-878b-53012218fd4b)

## Aanpassen van score
Het aanpassen van de score kan gedaan worden door de menu's te doorlopen en de gewenste data in te geven.
![readme](https://github.com/user-attachments/assets/63fbaa4e-6957-4e7a-9d62-7ee1a6048189)

## Installatie van tool
### Database
Om de database correct te laten werken, moet de naam van het databasebestand worden opgegeven via een .env-bestand dat je zelf aanmaakt. Dit bestand moet in de config folder komen te staan. In dit bestand voeg je de volgende variabele toe:

├── config
│   ├── __pycache__
│   ├── .env
│   ├── __init__.py
│   ├── config.py

```python
DB_PATH="jouw_database_bestand"
```
Plaats de database in de hoofdmap, dezelfde map waarin main.py zich bevindt.

### Vereiste packages
Alle benodigde packages zijn te vinden in requirements.txt.
