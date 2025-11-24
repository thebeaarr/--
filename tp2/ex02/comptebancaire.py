from datetime import datetime

class CompteBancaire:
    _compteur_id = 1

    def __init__(self, solde_initial=0.0):
        self.__id = CompteBancaire._compteur_id
        CompteBancaire._compteur_id += 1

        self.__solde = solde_initial
        self.__operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self.__operations.append(
                f"{datetime.now().isoformat()} - Dépôt : +{montant}€"
            )
        else:
            raise ValueError("Montant invalide")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self.__operations.append(
                f"{datetime.now().isoformat()} - Retrait : -{montant}€"
            )
        else:
            raise ValueError("Montant invalide")

    def get_solde(self):
        return self.__solde

    def get_id(self):
        return self.__id

    def releve(self):
        return "\n".join(self.__operations)

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []

    def ajouter_compte(self, compte: CompteBancaire):
        self.comptes.append(compte)

    def afficher(self):
        print(f"Client : {self.nom}")
        for compte in self.comptes:
            print(f"  Compte {compte.get_id()} - Solde : {compte.get_solde()}€")

    def releve_comptes(self):
        for compte in self.comptes:
            print(f"Relevé du compte {compte.get_id()} :")
            print(compte.releve())
            print("-" * 30)

cli = Client("Yassir")
cli.compte.deposer(300)
cli.compte.retirer(50)
cli.afficher()