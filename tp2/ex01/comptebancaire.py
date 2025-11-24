class CompteBancaire:
	def __init__(self , titulaire:str , sole_initiale= 0):
		self._titulaire = titulaire
		self.__solde = sole_initiale
	
	def deposer(self , montant):
		if montant > 0:
			self.__solde += montant
		else :
			raise ValueError("Montant invalide")
		
	def retirer(self , montant):
			if  0 <  montant <= self.__solde:
				self.__solde -= montant
			else:
				raise ValueError("Montant invalide")
	@property
	def solde(self):
		return self.__solde
	
	def __str__(self):
		return f"Titulaire: {self._titulaire}, Solde: {self.__solde}"


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    # Tentative de modification directe
    compte._CompteBancaire__solde = 500  # Ne fonctionnera pas
    print(compte.solde)