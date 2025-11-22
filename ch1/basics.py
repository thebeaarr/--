class Voiture:
	nombre_de_roues = 4
	#1 . attribut de class ( share for all instances ( or cars))

	# constructor (called for creating the instance car ( voirture))
	def __init__(self, marque , couleur):
		# attribut d'instancee (just for the object not shared lik the previous )
		self.marque = marque 
		self.couleur = couleur
		self.vitesse = 0
	
	# methode ( action que la voiture peut faire)

	def acceler (self , increment):
		self.vitesse += increment
		print(f"La {self.marque} roule a {self.vitesse} km/h")

	def freiner(self):
		self.vitesse = 0
		print("Arret complet")


# creer des objects (instances)
ma_voiture = Voiture("Toyota" , "rouge")

ta_voiture = Voiture("BMW", "noir")

ma_voiture.acceler(50)
ta_voiture.acceler(80)

print(ma_voiture.couleur)

print(Voiture.nombre_de_roues)