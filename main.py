from config import config as myconfig
import models.match as mymatch
import tabulate
import os
import sys
import inquirer
import csv
import keyboard
import cursor
import sysconfig
from datetime import datetime
from services.general_services import print_env_var
from services.db_service import lees_match_db as mydbserviceMatch
from services.db_service import lees_ploegen_in as mydbserviceClub
from services.db_service import pass_score_aan as mydbserviceScore
from services.db_service import lees_scheidsrechters_in as mydbserviceScheids
from services.db_service import lees_score_in as mydbserviceLeesScore
from services.object_to_dictionary import converteer_match_naar_tabel
from services.object_to_dictionary import converteer_club_naar_tabel
from services.object_to_dictionary import converteer_scheids_naar_tabel


def hoofdmenu():
	cursor.hide()
	os.system('cls')
	questions = [
	    inquirer.List(
	        "Keuze",
	        message="Welkom op de tool voor de database van Dames Volleybal West-Vlaanderen",
	        choices=["Geplande Wedstrijden", "Alle Wedstrijden", "Export Wedstrijden naar CSV", "Pas wedstrijdscore aan", "Verlaat applicatie"],
	    ),
	]
	answers = inquirer.prompt(questions)
	columns, rows, matchobjectlist =  mydbserviceMatch()
	columnnames = list(vars(matchobjectlist[0]).keys())
	if answers['Keuze'] == "Geplande Wedstrijden":
		vandaag = datetime.today()
		geplande_wedstrijden = [match for match in matchobjectlist if match.datum > vandaag]
		if geplande_wedstrijden:
			wedstrijdtabel(geplande_wedstrijden)
		else:
			print("Geen geplande wedstrijden gevonden.")
		submenu(geplande_wedstrijden, columnnames)
	elif answers['Keuze'] == "Alle Wedstrijden":
		wedstrijdtabel(matchobjectlist)
		submenu(matchobjectlist ,columnnames)
	elif answers['Keuze'] == "Export Wedstrijden naar CSV":
		filename = menukiesnaam("Kies een bestandsnaam voor de CSV export",matchobjectlist,columnnames)
		wedstrijd_CSV_Export(filename,matchobjectlist,columnnames)
	elif answers['Keuze'] == "Pas wedstrijdscore aan":
		menukiesploegen()
	elif answers['Keuze'] == "Verlaat applicatie":
		bevestiging = [
			inquirer.Confirm("Exit", message="Wil je de applicatie verlaten", default=False),
		]
		keuze = inquirer.prompt(bevestiging)
		if keuze['Exit']==True:
			os.system('cls')
			quit()
		else:
			hoofdmenu()
def submenu(matchobjectlist,columnnames):
	questions = [
	    inquirer.List(
	        "Keuze",
	        message="Terugkeren naar hoofdmenu",
	        choices=["Terug", "Export Wedstrijden naar CSV"],
	    ),
	]
	answers = inquirer.prompt(questions)
	if answers['Keuze'] == "Terug":
		hoofdmenu()
	elif answers['Keuze'] == "Export Wedstrijden naar CSV":
		os.system('cls')
		cursor.show()
		filename = input("Geef een gewenste bestandsnaam op voor de Export van data: ")
		cursor.hide()
		os.system('cls')
		wedstrijd_CSV_Export(filename,matchobjectlist,columnnames)
def wedstrijd_CSV_Export(naam, matchobjectlist, columnnames):
	try:
		#kijken of het bestand al bestaat

		#bestand bestaat al
		if os.path.isfile(naam + ".csv"):
			print("De bestandsnaam is al gebruikt!")
			bevestiging = [
				inquirer.Confirm("Confirm", message="Wil je het bestand overschrijven?", default=False),
			]
			keuze = inquirer.prompt(bevestiging)
			#overschrijven
			if keuze['Confirm']:
				with open(naam + ".csv", 'w', newline='') as csvfile:
					csvdata = csv.writer(csvfile, delimiter=';')
					csvdata.writerow(columnnames)
					rows = converteer_match_naar_tabel(matchobjectlist)
					for row in rows:
						#print(list(row.values())) #test voor de data te kunnen zien
						csvdata.writerow(list(row.values()))
					os.system('cls')
					print(f"{naam}.csv werd overschreven!\n\n Druk op spatie om terug te keren naar het hoofdmenu")
			#ander naam kiezen
			else:
				filename = menukiesnaam("Kies een andere bestandsnaam voor de CSV export!", matchobjectlist, columnnames)
				print(f"CSV file werd gemaakt met naam: {filename}.csv\n\n Druk op spatie om terug te keren naar het hoofdmenu")
		#bestand bestaat nog niet
		else:
			with open(naam + ".csv", 'w', newline='') as csvfile:
				csvdata = csv.writer(csvfile, delimiter=';')
				csvdata.writerow(columnnames)
				rows = converteer_match_naar_tabel(matchobjectlist)
				for row in rows:
					csvdata.writerow(list(row.values()))
				os.system('cls')
				print(f"CSV file werd gemaakt met naam: {naam}.csv\n\n Druk op spatie om terug te keren naar het hoofdmenu")
		keyboard.wait("space")  #wacht tot de gebruiker op spatie drukt om door te gaan
	except Exception as e:
		print(f"Er ging iets fout bij het creëren van de CSV file: {e}")
	finally:
		hoofdmenu()  #keer terug naar het hoofdmenu
def wedstrijdtabel(matchobjectlist):
	os.system('cls')
	rows = converteer_match_naar_tabel(matchobjectlist)
	print(tabulate.tabulate(rows, headers="keys", tablefmt="grid"))
def menukiesnaam(tekst,matchobjectlist,columnnames):
	os.system('cls')
	cursor.show()
	inputtext = [
		inquirer.Text("bestandsnaam", message=tekst),
	]
	enterdtext = inquirer.prompt(inputtext)
	filename = enterdtext['bestandsnaam']
	cursor.hide()
	os.system('cls')
	return filename
def menukiesploegen():
	os.system('cls')
	kolomnamen, tabeldata, clubobjectlist = mydbserviceClub()
	rows = converteer_club_naar_tabel(clubobjectlist)
	questions = [
	    inquirer.List(
	        "Thuisploeg",
	        message="Kies de bezoekersploeg",
	        choices=[row['Naam'] for row in rows],
	    ),
	]
	answers = inquirer.prompt(questions)
	thuisploeg = answers['Thuisploeg']

	questions = [
		inquirer.List(
			"Bezoekploeg",
			message="Kies de thuisploeg",
			choices=[row['Naam'] for row in rows if row['Naam'] != thuisploeg],
		),
	]
	answers = inquirer.prompt(questions)	
	bezoekploeg = answers['Bezoekploeg']

	os.system('cls')
	cursor.show()
	questions = [
		inquirer.Text(
			"score_thuis",
			message="Geef de score voor de thuisploeg",
			validate=score_validation,
		),
		inquirer.Text(
			"score_bezoek",
			message="Geef de score voor de bezoekersploeg",
			validate=score_validation,
		),
	]	
	answers = inquirer.prompt(questions)
	idThuis, idSporthal = find_ids(thuisploeg,rows)
	idBezoek, idSporthalBezoek = find_ids(bezoekploeg,rows) #sporthal bezoek wordt niet gebruikt want de match gaat thuis door
	scoreThuis = answers['score_thuis']
	scoreBezoek = answers['score_bezoek']

	os.system('cls')
	scheidsobjectlist = mydbserviceScheids()
	rows = converteer_scheids_naar_tabel(scheidsobjectlist)
	questions = [
	    inquirer.List(
	        "Scheidsrechter",
	        message="Kies scheidsrechter",
	        choices=[row['VolwaardigeNaam'] for row in rows],
	    ),
	]
	answers = inquirer.prompt(questions)
	scheids = answers['Scheidsrechter']
	idScheids = -1
	for row in rows:
		if row['VolwaardigeNaam']==answers['Scheidsrechter']:
			idScheids = row['Id']
	os.system('cls')
	kolomnamen, tabeldata, matchobjectlist = mydbserviceLeesScore(idThuis,idBezoek)
	rows = converteer_match_naar_tabel(matchobjectlist)
	print(matchobjectlist[0].datum)

	print("Aan te passen data:\n\nVan:")
	print(tabulate.tabulate(rows, headers="keys", tablefmt="grid"))
	aangepastMatch = [
		["Datum", "Thuis", "Bezoek", "Score", "Sporthal", "Adres", "Scheidsrechter"],
		[matchobjectlist[0].datum, thuisploeg, bezoekploeg, f"{scoreThuis} - {scoreBezoek}", matchobjectlist[0].sporthal, matchobjectlist[0].adres, scheids],
	]	
	print("\n\nNaar:")
	print(tabulate.tabulate(aangepastMatch, headers="firstrow", tablefmt="grid"))
	bevestiging = [
				inquirer.Confirm("Confirm", message="Wil je het de score wijzigen?"),
			]
	keuze = inquirer.prompt(bevestiging)
	if keuze['Confirm']:
		os.system('cls')
		mydbserviceScore(scoreThuis,scoreBezoek,idScheids,idSporthal,idThuis,idBezoek)
		print(f"De score werd aangepast!\n\n Druk op spatie om terug te keren naar het hoofdmenu")
		keyboard.wait("space")  #wacht tot de gebruiker op spatie drukt om door te gaan
		hoofdmenu()
	else:
		hoofdmenu()
def find_ids(ploegnaam,rows):
	for row in rows:
		if row['Naam']==ploegnaam:
			return row['Id'], row['Idsporthal']
def score_validation(answers, current):
	try:
		value = int(current)
		if value < 0 or value > 3:
			raise ValueError
	except ValueError:
		raise inquirer.errors.ValidationError("", reason="Gelieve enkel een waarde in te geven tussen 0 en 3")
	return True
if __name__ == "__main__":	
	hoofdmenu()