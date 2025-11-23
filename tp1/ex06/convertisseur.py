class Convertisseur : 
	taux_eur_dh = 10.9

	@staticmethod # les method qui sont utiles ni self ni cls 
	def vers_dh(euros:float) -> float:
		return euros * Convertisseur.taux_eur_dh
	@classmethod #pour les methode qui sont utilse cls 
	def mettre_a_jour_taux(cls ,nv_taux: float ): 
		Convertisseur.taux_eur_dh = nv_taux
	@staticmethod
	def vers_eur(dirhams : float):
		return dirhams / Convertisseur.taux_eur_dh

