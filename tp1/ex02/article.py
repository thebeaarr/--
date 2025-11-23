class Article:
	reference: str
	designation: str
	prix_ht: float
	stock: int

	def __init__(self,  reference:str , designation :str , prix_ht : float,
			  stock : int):
		self.reference = reference
		self.prix_ht = prix_ht
		self.stock = stock 
		self.designation = designation

	def valeur_stock(self) -> float :
		return self.prix_ht * self.stock
	
	def __str__(self):
		return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} € HT"
