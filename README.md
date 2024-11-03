# Voorbereiding van de opdracht

Bestudeer eerste de eerste acht hoofdstukken hoofdstukken. Je hebt de skills van de eerste acht
hoofdstukken nodig om de opdracht te maken.

Bedenkt een situatie in je eigen leven of werk waar je een handige tooltje zou kunnen gebruiken waarbij
gegevens in een database bewaard worden. Het tooltje presenteert de gegevens op een handige wijze en
staat je toe op een eenvoudige wijze de gegevens aan te passen.

# De opdracht zelf

Ontwikkel een command line applicatie met een eenvoudige database die enkele opzoekingen en enkele
manipulaties doet. Database mag uit beperkt aantal tabellen bestaan (twee is voldoende). De applicatie
hoeft ook niet volledig te zijn. Als bepaalde aspecten niet geïmplementeerd zijn, dan is dat OK. De applicatie
moet gebruik maken van een sqlite-database, en van klassen. Het bepalen van de commando's van de
gebruiker mag via het opvragen van gegevens of via argumenten.

Wat zijn de minimale voorwaarden voor je project:

```
Je gebruikt git tijdens het ontwikkelen.
Meerdere commits moeten in de geschiedenis van je gitrepo zichtbaar zijn.
Je hebt correct een .gitignore gebruikt.
Je gitrepo bevat een README.md-bestand met duidelijke uitleg over het doel van de applicatie, de
gerealiseerde functionaliteiten, en hoe de applicatie in productie genomen moet worden (locatie
van de database, opbouw van het instellingenbestand, ...).
Je remote repo zit in Github.
De locatie van de database en eventuele andere gevoelige data zitten in een instellingenbestand. Deze
zit niet in je gitrepository. In de gitrepository zit er wel een voorbeeld zodat het duidelijk is hoe het
instellingenbestand opgebouwd moet zijn.
De applicatie gebruikt een SQLite-database met minstens twee tabellen.
Er worden rijen gewijzigd in de database of aan de database toegevoegd.
De gebruiker kan een rapport in csv of Excel opvragen.
Er wordt gebruik gemaakt van minstens één klasse waarvan ook objecten geïnstantieerd worden.
Er is interactie met gebruiker via de terminal.
De applicatie is goed gestructureerd in diverse mappen en bestanden. Je gebruikt dus modules en
packages.
Je hebt bij het ontwikkelen gebruik gemaakt van een virtual enviroment (venv). Deze zit niet in je
gitrepo en wordt dus niet meegeleverd.
Misschien heb je packages geïnstalleerd (misschien ook niet). Je hebt met pip freeze >
requirements.txt een bestand requirements.txt gemaakt en dat zit ook in je gitrepo.
```
## Inleveren van de opdracht


Je levert via de Toledoopdracht het volgende in:

```
De url van je gitrepository die ik kan klonen. Dit betekent dat de repo publiek is of dat ik leesrechten
heb. MIjn Githubaccount is arnevdbvives (e-mail: arne.vandenbussche@vives.be).
Een voorbeelddatabase met voorbeeldgegevens.
```
Mijn flow zal de volgende zijn:

```
Ik kloon je githubrepo.
Ik creëer een virtuele omgeving.
Ik installeer in de virtuele omgeving de nodige packages van je requirement.txt, met het command
pip install -r requirements.txt.
Ik bestudeer je README.md om te zien waar ik de database plaats en hoe ik het instelingenbestand
moet invullen.
Ik run het project en bestudeer de code.
```

