from contact import Contact



class Carnet:
	i = 0
	def __init__(self):
		self.__contacts = []
	
	def ajouter(self, contact:Contact):
		self.__contacts.append(contact)
	
	def recherche(self, fragement: str):
		fragement = fragement.lower()
		resultats = []

		for contact in self.__contacts :
			if fragement == contact.nom.lower():
				resultats.append(contact)
		return resultats
	
	def afficher_tous(self):
		for contact in self.__contacts:
			print(f"nom : {contact.nom}, telephone : {contact.telephone}, email: {contact.email}")
