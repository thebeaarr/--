class Chronometre:
	def __enter__(self):
		"""called at the start of the programm"""
		print("Chronometre started")
		self.debut = time.time()
		return self
	
	def __exit__(self , exc_type , exec_value , traceback):
		self.fin = time.time()
		duree  = self.fin - self.debut
		print(f"Temps ecoule : {duree:.2f} secondes")
		
		if exc_type is not None:
			print(f"Erreur detecter: {exc_value}")

		return False

import time 

with Chronometre() :
	time.sleep(2)