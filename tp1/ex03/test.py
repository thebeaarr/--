from carnet import Carnet
from contact import Contact

c = Carnet()

c.ajouter(Contact("Alice", "0600000001", "alice@mail.com"))
c.ajouter(Contact("Sabrina", "0600000002", "sab@mail.com"))
c.ajouter(Contact("Bob", "0600000003", "bob@mail.com"))

print("Tous les contacts :")
c.afficher_tous()

print("\nRésultats de recherche 'a' :")
resultat = c.recherche("sabrina")
for contact in resultat:
    print(contact.nom, contact.telephone)