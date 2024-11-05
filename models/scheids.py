class scheids:
	def __init__(self,id,naam,voornaam):
		self.id = id
		self.naam = naam
		self.voornaam = voornaam
	def get_full_name(self):
		fullname = self.voornaam + " " + self.naam
		return fullname