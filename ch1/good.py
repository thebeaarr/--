class Client:
	def __init__(self , nom , email):
		self.nom = nom
		self.email = email 
		self.points = 0
	
	def ajouter_points(self , points):
		self.points += points 
		print(f"{self.nom} a maintenant {self.points} points !")
	
	def peut_avoir_cafe_gratuit(self):
		return self.points >= 50 
	
	

client1 = Client("ahmed" , "ahmed@email.com")

client1.ajouter_points(10)

client2 = Client("fatima" , "fatima@gmail.com")

client2.ajouter_points(60)


if client2.peut_avoir_cafe_gratuit() :
	print(f"{client2.nom} mérite un café gratuit ! ☕")
