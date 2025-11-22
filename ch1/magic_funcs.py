class Argent:
	def __init__(self , montant , devise="DH"):
		self.montant = montant
		self.devise = devise
	
	def __str__(self):
		return f"{self.montant} {self.devise}"
	
	def __repr__(self):
		return f"Argent({self.montant}, '{self.devise}')"
	
	def __add__(self, autre):
		if self.devise != autre.devise :
			raise ValueError("Devises differentes !")
		return Argent(self.montant + autre.montant, self.devise)
	
	def __sub__(self, autre):
		if self.devise != autre.devise :
			raise ValueError("Devises differentes !")
		return Argent(self.montant - autre.montant , self.devise)
	
	def __mul__(self, facteur):
		return Argent(self.montant * facteur , self.devise)
	
	def __eq__(self, autre):
		return self.montant == autre.montant and self.devise == autre.devise
	
	def __lt__(self ,autre):
			if self.devise != autre.devise :
				raise ValueError("Devises deifferents !")
			return self.montant < autre.montant
		
	
	def __gt__(self, autre):
			if self.devise != autre.devise:
				raise ValueError ("Devises deifferents !")
			return self.montant > autre.montant

prix1 = Argent(100, "DH")

prix2 = Argent(50 , "DH")

prix3  = Argent(10 , "EURO")


print(prix1)
print(prix2)



print(prix1 + prix2 )

print(prix1 + prix3)


