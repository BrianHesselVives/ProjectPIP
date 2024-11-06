import sqlite3
import config.config as myconfig
from models.match import match
from models.club import club
from models.scheids import scheids
from datetime import datetime

def lees_match_db():
	try:
		with sqlite3.connect(myconfig.db_path) as dbconnectie:
			mijncursor = dbconnectie.cursor()
			query = '''
			SELECT * FROM LeesbareData;
			'''
			tabel = mijncursor.execute(query)
			tabeldata = tabel.fetchall()
			kolomnamen = [description[0] for description in mijncursor.description]
			matchobjectlist = []
			for row in tabeldata:
				mymatch = match(
					datum = row[0],
					thuis = row[1],
					bezoek = row[2],
					score = row[3],
					sporthal = row[4],
					adres = row[5],
					scheids = row[6],
					id_sporthal=0,
					score_thuis=0,
					score_bezoek=0
				)
				matchobjectlist.append(mymatch)
			return kolomnamen, tabeldata, matchobjectlist
	except Exception as e:
		print(f"Er ging iets fout bij het inlezen van de wedstrijden \n {e}")
def lees_score_in(idThuis,idBezoek):
	try:
		with sqlite3.connect(myconfig.db_path) as dbconnectie:
			mijncursor = dbconnectie.cursor()
			query = '''
				SELECT Datum,thuisClubNaam, bezoekClubNaam, 
			       scoreThuis || ' - ' || scoreBezoek AS score,
				   naam, adres,scheidsNaam
				FROM AlleData
				WHERE idThuis = ? and idBezoek = ?;
			'''
			parameters=(idThuis,idBezoek)
			tabel = mijncursor.execute(query,parameters)
			tabeldata = tabel.fetchall()
			kolomnamen = [description[0] for description in mijncursor.description]
			matchobjectlist = []
			for row in tabeldata:
				mymatch = match(
					datum = row[0],
					thuis = row[1],
					bezoek = row[2],
					score = row[3],
					sporthal = row[4],
					adres = row[5],
					scheids = row[6],
					id_sporthal=0,
					score_thuis=0,
					score_bezoek=0
				)
				matchobjectlist.append(mymatch)
			return kolomnamen, tabeldata, matchobjectlist
	except Exception as e:
		print(f"Er ging iets fout bij het inlezen van de score\n {e}")
def pass_score_aan(scoreThuis,scoreBezoek,idscheids,idSporthal,idThuis,idBezoek):
	try:
		with sqlite3.connect(myconfig.db_path) as dbconnectie:
			mijncursor = dbconnectie.cursor()
			query = '''
				UPDATE match
				SET scoreThuis = ?, scoreBezoek = ?,idScheids = ?,idSporthal=?
				WHERE match.idThuis = ? and match.idBezoek = ?;
			'''
			parameters=(scoreThuis,scoreBezoek,idscheids,idSporthal,idThuis,idBezoek)
			mijncursor.execute(query,parameters)
			dbconnectie.commit()
	except Exception as e:
		print(f"Er ging iets fout bij het wegschrijven van de score\n {e}")
def lees_ploegen_in():
	try:
		with sqlite3.connect(myconfig.db_path) as dbconnectie:
			mijncursor = dbconnectie.cursor()
			query = '''
			SELECT * FROM club;
			'''
			tabel = mijncursor.execute(query)
			tabeldata = tabel.fetchall()
			kolomnamen = [description[0] for description in mijncursor.description]
			clubobjectlist = []
			for row in tabeldata:
				myclub = club(
					idClub = row[0],
					naam = row[1],
					idSporthal = row[2],
				)
				clubobjectlist.append(myclub)
			return kolomnamen, tabeldata, clubobjectlist
	except Exception as e:
		print(f"Er ging iets fout bij het inlezen van de clubs \n {e}")
def lees_scheidsrechters_in():
	try:
		with sqlite3.connect(myconfig.db_path) as dbconnectie:
			mijncursor = dbconnectie.cursor()
			query = '''
			SELECT * FROM scheids;
			'''
			tabel = mijncursor.execute(query)
			tabeldata = tabel.fetchall()
			scheidsobjectlist = []
			for row in tabeldata:
				myscheids = scheids(
					id = row[0],
					naam = row[1],
					voornaam = row[2],
				)
				scheidsobjectlist.append(myscheids)
			return scheidsobjectlist
	except Exception as e:
		print(f"Er ging iets fout bij het inlezen van de scheidsrechters \n {e}")
if __name__ == "__main__":
	pass