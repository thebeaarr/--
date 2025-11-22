class CompteBancaire:
	def __init__(self, titulaire , solde):
		self.titulaire = titulaire # public - tout le monde y acceder
		self._solde = solde # protected " ne touche pas sauf si tu sais ce que tu fais"
		self.__code_pin = "1234" # private - vraient cache
		self.__tentatives_resstances = 3 
	
	# interface public pour acceder au solde

	def consulter_solde(self):
		return self._solde
	
	#interface public pour retirer
	def retirer(self , montant , pin)-> False :
		if pin != self.__code_pin :
			print("pin incorrect")
			self.__tentatives_resstances -= 1
			if self.__tentatives_resstances == 0 :
				print("compte blocked")
			return False
		
		if montant > self._solde :
			print("solde insuffisant")

		self._solde -= montant
		print(f"retrait de {montant} DH effectie")
		return True
	def changer_pin(self, ancien_pin , nouvea_pin):
			if(ancien_pin == self.__code_pin) :
				self.__code_pin  = nouvea_pin
				self.__tentatives_resstances = 3
				print("Pin change avec succes")
				return true
			print("Ancien Pin incorrect")
			return false

compte = CompteBancaire("med" , 30)

print(compte.consulter_solde())

compte.retirer(10 , "1234")

print(compte.consulter_solde())
