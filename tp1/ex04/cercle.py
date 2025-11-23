from math import pi

class Cercle:
	def __init__(self, rayon: float):
		self.rayon = rayon

	@property
	def rayon(self):
		return self._rayon

	@rayon.setter
	def rayon(self, valeur):
		if valeur <= 0:
			raise ValueError("Le rayon doit être strictement positif")
		self._rayon = valeur

	@property
	def perimetre(self):
		return 2 * pi * self._rayon

	@property
	def surface(self):
		return pi * self._rayon ** 2

	def agrandir(self, pourcentage: float):
		if pourcentage <= 0:
			raise ValueError("Le pourcentage doit être strictement positif")
		self.rayon = self._rayon * (1 + pourcentage / 100)
