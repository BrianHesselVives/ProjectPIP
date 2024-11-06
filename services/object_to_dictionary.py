from models.match import match
from models.club import club
from models.scheids import scheids

def converteer_match_naar_tabel(matchobjectlist):
	rows = [
		{
			"Datum": match.datum,
			"Thuis": match.thuis,
			"Bezoek": match.bezoek,
			"Score": match.score,
			"Sporthal": match.sporthal,			
			"Adres": match.adres,
			"Scheidsrechter": match.scheids
		}		
		for match in matchobjectlist
	]	
	return rows
def converteer_club_naar_tabel(clubobjectlist):
	rows = [
		{
			"Id": club.idClub,
			"Naam": club.naam,
			"Idsporthal": club.idSporthal
		}		
		for club in clubobjectlist
	]	
	return rows
def converteer_scheids_naar_tabel(scheidsobjectlist):
	rows = [
		{
			"Naam": scheids.naam,
			"Voornaam": scheids.voornaam,
			"Id": scheids.id,
			"VolwaardigeNaam": scheids.get_full_name()
		}		
		for scheids in scheidsobjectlist
	]	
	return rows