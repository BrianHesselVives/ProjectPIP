from config import config as myconfig
import sysconfig
from services.general_services import print_env_var
from services.db_service import lees_match_db as mydbservice
from services.object_to_dictionary import converteer_match_naar_tabel
import models.match as mymatch
import tabulate
import os
import sys
import inquirer
import csv
import keyboard
import cursor
import datetime

def hoofdmenu():
	cursor.hide()
	os.system('cls')
	questions = [
	    inquirer.List(
	        "Keuze",
	        message="Welkom op de tool voor de database van Dames Volleybal West-Vlaanderen",
	        choices=["Geplande Wedstrijden", "Alle Wedstrijden", "Export Wedstrijden naar CSV", "Voeg wedstrijdscore toe", "Pas wedstrijdscore aan", "Verlaat applicatie"],
	    ),
	]
	answers = inquirer.prompt(questions)
	columns, rows, matchobjectlist =  mydbservice()
	columnnames = list(vars(matchobjectlist[0]).keys())
	if answers['Keuze'] == "Alle Wedstrijden":
		wedstrijdtabel(matchobjectlist)
		submenu(matchobjectlist)
	elif answers['Keuze'] == "Export Wedstrijden naar CSV":
		menukiesnaam("Kies een bestandsnaam voor de CSV export",rows,columns)
		wedstrijd_CSV_Export(filename,rows,columns)
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
def submenu(matchobjectlist):
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
		wedstrijd_CSV_Export(filename,rows,columns)
def wedstrijd_CSV_Export(naam, rijen, kolomnamen):
	try:
		if os.path.isfile(naam + ".csv"):
			print("de bestandsnaam is al gebruikt!")
			bevestiging = [
				inquirer.Confirm("Confirm", message="Wil je het bestand overschrijven", default=False),
			]
			keuze = inquirer.prompt(bevestiging)
			if keuze['Confirm']==False:
				menukiesnaam("Kies een andere bestandsnaam voor de CSV export!",rijen,kolomnamen)
			else:
				with open(naam + ".csv", 'w', newline='') as csvfile:
					csvdata = csv.writer(csvfile, delimiter=';')
					csvdata.writerow(kolomnamen)
					for rij in rijen:
						csvdata.writerow(rij)
				os.system('cls')
				print(f"{naam}.csv werd overschreven!\n\n druk spatie terug te keren naar het hoofdmenu")
		else:
			with open(naam + ".csv", 'w', newline='') as csvfile:
					csvdata = csv.writer(csvfile, delimiter=';')
					csvdata.writerow(kolomnamen)
					for rij in rijen:
						csvdata.writerow(rij)
					print(f"CSV file werd gemaakt met naam: {naam}.csv\n\n druk spatie terug te keren naar het hoofdmenu")
		#onderstaande remap wordt toegepast omdat er een probleem voordoet bij het drukken op enter
		#remap de enter toets naar space
		keyboard.remap_key("enter", "space")
		#wacht op een toetsdruk
		keyboard.read_event()
		#deactiveer de keymap
		keyboard.unremap_key("enter")
		#terug naar hoofdmenu
		hoofdmenu()
	except Exception as e:
		print(f"Er ging iets fout bij het creëren van de CSV file \n {e}")
def wedstrijdtabel(matchobjectlist):
	os.system('cls')
	rows = converteer_match_naar_tabel(matchobjectlist)
	print(tabulate.tabulate(rows, headers="keys", tablefmt="grid"))
def menukiesnaam(tekst,rows,columns):
	os.system('cls')
	cursor.show()
	inputtext = [
		inquirer.Text("bestandsnaam", message=tekst),
	]
	enterdtext = inquirer.prompt(inputtext)
	filename = enterdtext['bestandsnaam']
	cursor.hide()
	os.system('cls')
	wedstrijd_CSV_Export(filename,rows,columns)
if __name__ == "__main__":	
	hoofdmenu()