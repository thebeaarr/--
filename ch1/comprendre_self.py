class Personne:
	def __init__(self , nom , age):
		self.nom = nom 
		self.age = age 
	
	def se_presenter(self):
			print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")

	def vieillir(self):
		self.age += 1
		print(f"C'est mon anniversaire ! J'ai maintenant {self.age} ans")
	
ahmed = Personne("Ahmed" , 25)

fatima = Personne("fatima" ,30 )

ahmed.se_presenter()

fatima.se_presenter()

ahmed.vieillir()
# fatima not in mood this year hhhh
