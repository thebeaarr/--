class CompteBancaire:
		banque = "Bank Al-Maghrib"
		taux_interet =  0.03
		nombre_comptes  = 0

		def __init__(self, titulaire , solde):
			self.titulaire = titulaire
			self.solde = solde 
			CompteBancaire.nombre_comptes += 1

		def afficher_info(self):
			print(f"Compte de {self.titulaire} : {self.solde} DH")
			print(f"Banque: {CompteBancaire.banque}")
		
#Test

compte1  = CompteBancaire("Ahmed" , 100)

compte2 = CompteBancaire("Fatima" , 20000)

print(f"Nombre total de comptes :{CompteBancaire.nombre_comptes}")

CompteBancaire.taux_interet = 0.05

print(compte1.taux_interet)
print(compte2.taux_interet)