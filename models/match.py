from datetime import datetime
class match:
	def __init__(self,datum,thuis,bezoek,score,sporthal,adres,scheids,id_sporthal,score_thuis,score_bezoek):
		self.datum = datetime.strptime(datum, "%Y-%m-%d %H:%M")
		self.thuis = thuis
		self.bezoek = bezoek	
		self.score = score
		self.sporthal = sporthal
		self.adres = adres
		self.scheids = scheids
		self.id_sporthal = id_sporthal
		self.score_thuis = score_thuis
		self.score_bezoek = score_bezoek