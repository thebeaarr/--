from dataclasses import dataclass , field 

from typing import List 
from datetime import datetime


@dataclass
class Produit:
		nom : str 
		prix: float
		quantite : int = 0
		categories: List[str] = field(default_factory=list) #list vide par defaut

		def __post_init__(self):
			"""appele apres __init__ pour validation"""
			if self.prix < 0 :
				raise ValueError("le prix est negatif !!!")
			if self.quantite < 0:
				raise ValueError("valeur est negative ? ")
			
			@property
			def valeur_stock(self):
				return self.prix * self.quantite
			
			def est_disponible(self):
				return self.quantite > 0

produit = Produit(nom="Ordinateur" , 
	prix=5000,
	quantite=10,
	categories=["Electronique" , "Informatique"])

print(produit)


produit2 =Produit(nom="Ordinateur" , 
	prix=5000,
	quantite=10,
	categories=["Electronique" , "Informatique"])

print(produit == produit2)