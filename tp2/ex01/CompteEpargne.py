from comptebancaire import CompteBancaire


class CompteEpargne(CompteBancaire):
	def __init__(self, titulaire, solde_initial=0, taux_interet=0.03):
		super().__init__(titulaire, solde_initial)
		self._taux_interet = taux_interet

	@property
	def calculer_interet(self):
		interet = self.solde * self._taux_interet
		self.deposer(interet)  # on ajoute l'intérêt au solde
		self._operations.append(f"Intérêt ajouté : +{interet}")
		return interet

	def __str__(self):
		return f"[Épargne] {super().__str__()}, Taux: {self._taux_interet * 100}%"
