class Contact:
	nom : str
	telephone : str
	email : str
	def __init__(self, nom : str , telephone : str , email : str):
		self.nom = nom
		self.telephone = telephone
		self.email = email 
	
	def initiale(self):
		return self.nom[0].upper()
