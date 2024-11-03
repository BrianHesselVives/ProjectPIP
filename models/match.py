class match:
	def __init__(self,score_thuis,score_bezoek,id_thuis,id_bezoek,datum,id_scheids,id_sporthal):
		self.score_thuis = score_thuis
		self.score_bezoek = score_bezoek
		self.id_thuis = id_thuis
		self.id_bezoek = id_bezoek
		self.datum= datum
		self.id_scheids = id_scheids
		self.id_sporthal = id_sporthal

if __name__ =="__main__":
	#test code om het object te kunnen bekijken
	mymatch = match(1,2,1,2,"2024-11-3 20:33",5,3)
	print(vars(mymatch))