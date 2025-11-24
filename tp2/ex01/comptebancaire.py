class CompteBancaire:
	def __init__(self , titulaire:str , sole_initiale= 0):
		super().__setattr__("_titulaire" , titulaire)
		super().__setattr__("_CompteBancaire__solde" , sole_initiale)
		super().__setattr__("_operations" , [])


	def deposer(self , montant):
		if montant > 0:
			self.__solde += montant
			self._operations.append(f"Depot : +{montant}")
		else :
			raise ValueError("Montant invalide")
		
	def retirer(self , montant):
			if  0 <  montant <= self.__solde:
				self.__solde -= montant
				self._operations.append(f"Retrait : -{montant}")
			else:
				raise ValueError("Montant invalide")
	@property
	def solde(self):
		return self.__solde

	@solde.setter
	def solde(self , valeur):
		raise ValueError("AttributeError: can't set attribute 'solde'")
	
	@property
	def operations(self):
			return self._operations

	def __str__(self):
		return f"Titulaire: {self._titulaire}, Solde: {self.__solde}"
	

	def __setattr__(self, name, value):
		super().__setattr__(name, value)

if __name__ == "__main__":
	compte = CompteBancaire("Ali", 1000)
	compte.deposer(200)
	compte.retirer(150)
	print(compte)
	print("Solde accessible (lecture) :", compte.solde)

	# Tentative de modification directe
	compte.solde = 500  # Ne fonctionnera pas