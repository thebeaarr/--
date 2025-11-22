# 🎯 Guide Complet de la Programmation Orientée Objet en Python

> **Pour enfin comprendre la POO sans se prendre la tête**

## 📚 Table des matières
1. [C'est quoi la POO et pourquoi ça existe ?](#quest-ce-que-la-poo)
2. [Les bases : Classes et Objets](#les-bases)
3. [Le mystérieux `self` expliqué simplement](#comprendre-self)
4. [Attributs : de classe vs d'instance](#attributs)
5. [Encapsulation : protéger ses données](#encapsulation)
6. [Properties : des attributs intelligents](#properties)
7. [Méthodes magiques : rendre vos objets cool](#méthodes-magiques)
8. [Méthodes statiques et de classe](#méthodes-spéciales)
9. [Dataclasses : moins de code, plus d'efficacité](#dataclasses)
10. [Gestionnaire de contexte (`with`)](#gestionnaire-de-contexte)
11. [Exemples pratiques réels](#exemples-pratiques)

---

## 🤔 Qu'est-ce que la POO ?

### Le problème sans POO

Imagine que tu gères un café et tu veux suivre tes clients :

```python
# Sans POO - C'est le bordel
client1_nom = "Ahmed"
client1_points = 10
client1_email = "ahmed@email.com"

client2_nom = "Fatima"
client2_points = 25
client2_email = "fatima@email.com"

# Pour ajouter des points, tu dois faire ça à chaque fois :
client1_points += 5
client2_points += 5

# Si tu as 100 clients ? Bonne chance...
```

**Problèmes :**
- Code répétitif
- Difficile à maintenir
- Risque d'erreurs
- Impossible à étendre

### La solution avec POO

```python
class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.points = 0
    
    def ajouter_points(self, points):
        self.points += points
        print(f"{self.nom} a maintenant {self.points} points !")
    
    def peut_avoir_cafe_gratuit(self):
        return self.points >= 50

# Utilisation - BEAUCOUP plus simple
client1 = Client("Ahmed", "ahmed@email.com")
client2 = Client("Fatima", "fatima@email.com")

client1.ajouter_points(5)
client2.ajouter_points(30)

if client2.peut_avoir_cafe_gratuit():
    print(f"{client2.nom} mérite un café gratuit ! ☕")
```

**Avantages :**
- ✅ Code organisé et réutilisable
- ✅ Facile à maintenir
- ✅ Moins de bugs
- ✅ 1000 clients ? Aucun problème !

---

## 🏗️ Les Bases

### Anatomie d'une classe

```python
class Voiture:
    # 1. Attribut de CLASSE (partagé par TOUTES les voitures)
    nombre_de_roues = 4
    
    # 2. Constructeur (appelé quand tu crées une voiture)
    def __init__(self, marque, couleur):
        # 3. Attributs d'INSTANCE (propres à CETTE voiture)
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0
    
    # 4. Méthode (action que la voiture peut faire)
    def accelerer(self, increment):
        self.vitesse += increment
        print(f"La {self.marque} roule à {self.vitesse} km/h")
    
    def freiner(self):
        self.vitesse = 0
        print("Arrêt complet")

# Créer des objets (instances)
ma_voiture = Voiture("Toyota", "rouge")
ta_voiture = Voiture("BMW", "noir")

# Utiliser les méthodes
ma_voiture.accelerer(50)  # La Toyota roule à 50 km/h
ta_voiture.accelerer(80)  # La BMW roule à 80 km/h

# Accéder aux attributs
print(ma_voiture.couleur)      # rouge
print(Voiture.nombre_de_roues) # 4 (attribut de classe)
```

### 🔑 Points clés

| Concept | Description | Exemple |
|---------|-------------|---------|
| **Classe** | Le moule, le blueprint | `class Voiture:` |
| **Objet/Instance** | Une voiture spécifique créée | `ma_voiture = Voiture(...)` |
| **Attribut** | Caractéristique | `self.marque`, `self.couleur` |
| **Méthode** | Action que l'objet peut faire | `def accelerer(...)` |
| **`self`** | Référence à l'objet lui-même | Le premier paramètre |

---

## 🧠 Comprendre `self`

`self` = "moi-même" en anglais. C'est comme si l'objet se parlait à lui-même.

### Exemple concret

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom      # "MON nom est..."
        self.age = age      # "MON âge est..."
    
    def se_presenter(self):
        # "JE m'appelle... et J'ai..."
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans")
    
    def vieillir(self):
        self.age += 1       # "JE vieillis"
        print(f"C'est mon anniversaire ! J'ai maintenant {self.age} ans")

# Création
ahmed = Personne("Ahmed", 25)
fatima = Personne("Fatima", 30)

# Quand tu appelles ahmed.se_presenter()
# Python fait automatiquement : Personne.se_presenter(ahmed)
# Donc self = ahmed dans cette méthode

ahmed.se_presenter()   # self = ahmed
fatima.se_presenter()  # self = fatima (différent!)
```

**Règle d'or :** `self` est TOUJOURS le premier paramètre des méthodes d'instance, mais tu ne le passes JAMAIS quand tu appelles la méthode (Python le fait pour toi).

---

## 📦 Attributs

### Attribut de classe vs Attribut d'instance

```python
class CompteBancaire:
    # Attribut de CLASSE (partagé par TOUS les comptes)
    banque = "Bank Al-Maghrib"
    taux_interet = 0.03
    nombre_comptes = 0  # Compteur global
    
    def __init__(self, titulaire, solde):
        # Attributs d'INSTANCE (propres à CE compte)
        self.titulaire = titulaire
        self.solde = solde
        CompteBancaire.nombre_comptes += 1  # Incrémenter le compteur
    
    def afficher_info(self):
        print(f"Compte de {self.titulaire}: {self.solde} DH")
        print(f"Banque: {CompteBancaire.banque}")

# Test
compte1 = CompteBancaire("Ahmed", 1000)
compte2 = CompteBancaire("Fatima", 2000)

print(f"Nombre total de comptes: {CompteBancaire.nombre_comptes}")  # 2

# Changer l'attribut de classe affecte TOUS les comptes
CompteBancaire.taux_interet = 0.05
print(compte1.taux_interet)  # 0.05
print(compte2.taux_interet)  # 0.05
```

### 📊 Comparaison

| Type | Définition | Accès | Utilisation |
|------|------------|-------|-------------|
| **Classe** | Hors de `__init__` | `Classe.attribut` | Constantes, compteurs, config partagée |
| **Instance** | Dans `__init__` avec `self` | `objet.attribut` | Données spécifiques à chaque objet |

---

## 🔒 Encapsulation

L'encapsulation = cacher les détails internes et ne montrer que ce qui est nécessaire.

### Les conventions Python

```python
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire           # Public - tout le monde peut y accéder
        self._solde = solde                  # Protected - "ne touche pas sauf si tu sais ce que tu fais"
        self.__code_pin = "1234"             # Private - vraiment caché
        self.__tentatives_restantes = 3
    
    # Interface publique pour accéder au solde
    def consulter_solde(self):
        return self._solde
    
    # Interface publique pour retirer
    def retirer(self, montant, pin):
        # Vérifier le PIN
        if pin != self.__code_pin:
            self.__tentatives_restantes -= 1
            print(f"❌ PIN incorrect. {self.__tentatives_restantes} tentatives restantes")
            
            if self.__tentatives_restantes == 0:
                print("🚨 Compte bloqué !")
            return False
        
        # Vérifier le solde
        if montant > self._solde:
            print("❌ Solde insuffisant")
            return False
        
        # Effectuer le retrait
        self._solde -= montant
        print(f"✅ Retrait de {montant} DH effectué")
        return True
    
    def changer_pin(self, ancien_pin, nouveau_pin):
        if ancien_pin == self.__code_pin:
            self.__code_pin = nouveau_pin
            self.__tentatives_restantes = 3  # Reset des tentatives
            print("✅ PIN changé avec succès")
            return True
        print("❌ Ancien PIN incorrect")
        return False

# Utilisation
compte = CompteBancaire("Hassan", 5000)

# ✅ Accès via l'interface publique (recommandé)
print(compte.consulter_solde())  # 5000
compte.retirer(1000, "1234")     # Succès

# ⚠️ Accès direct au solde (possible mais déconseillé)
print(compte._solde)  # 4000 - fonctionne mais c'est malpoli

# ❌ Accès au PIN (très difficile à cause du name mangling)
# print(compte.__code_pin)  # AttributeError
# Tu DOIS passer par les méthodes publiques
```

### 🎯 Pourquoi c'est important ?

```python
# Sans encapsulation - DANGER
compte._solde = -10000  # Oups, solde négatif impossible !

# Avec encapsulation - SÉCURISÉ
class CompteBancaireSecurise:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.__solde = solde
    
    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if montant > self.__solde:
            raise ValueError("Solde insuffisant")
        self.__solde -= montant
    
    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.__solde += montant
    
    @property
    def solde(self):
        return self.__solde

# Maintenant, impossible de faire n'importe quoi
compte = CompteBancaireSecurise("Ali", 1000)
# compte.solde = -5000  # ❌ AttributeError
compte.deposer(500)     # ✅ La seule façon correcte
```

---

## ⚡ Properties

Les properties = attributs avec des super-pouvoirs

### Exemple simple

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    # Getter - pour LIRE la valeur
    @property
    def celsius(self):
        print("📖 Lecture de la température")
        return self._celsius
    
    # Setter - pour MODIFIER la valeur
    @celsius.setter
    def celsius(self, valeur):
        print(f"✍️ Changement de température à {valeur}°C")
        if valeur < -273.15:
            raise ValueError("Température en dessous du zéro absolu !")
        self._celsius = valeur
    
    # Property calculée (pas de setter)
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

# Utilisation - syntaxe naturelle
temp = Temperature(25)

# Lecture (appelle le getter)
print(temp.celsius)      # 📖 Lecture... → 25

# Modification (appelle le setter)
temp.celsius = 30        # ✍️ Changement... → 30

# Properties calculées
print(f"{temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

# Validation automatique
try:
    temp.celsius = -300  # ❌ ValueError !
except ValueError as e:
    print(f"Erreur : {e}")
```

### 🎬 Cas d'usage réel : Rectangle

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self._largeur = largeur
        self._hauteur = hauteur
    
    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self, valeur):
        if valeur <= 0:
            raise ValueError("La largeur doit être positive")
        self._largeur = valeur
    
    @property
    def hauteur(self):
        return self._hauteur
    
    @hauteur.setter
    def hauteur(self, valeur):
        if valeur <= 0:
            raise ValueError("La hauteur doit être positive")
        self._hauteur = valeur
    
    # Properties calculées automatiquement
    @property
    def surface(self):
        return self._largeur * self._hauteur
    
    @property
    def perimetre(self):
        return 2 * (self._largeur + self._hauteur)
    
    @property
    def est_carre(self):
        return self._largeur == self._hauteur

# Magie en action
rect = Rectangle(10, 5)

print(f"Surface : {rect.surface} m²")        # 50 (calculé automatiquement)
print(f"Périmètre : {rect.perimetre} m")     # 30 (calculé automatiquement)
print(f"Est un carré ? {rect.est_carre}")    # False

# Change la largeur → surface et périmètre se recalculent automatiquement
rect.largeur = 20
print(f"Nouvelle surface : {rect.surface} m²")  # 100 !
```

**Quand utiliser @property ?**
- ✅ Pour valider les données avant de les stocker
- ✅ Pour calculer des valeurs à la volée
- ✅ Pour garder une syntaxe simple (`objet.attribut` au lieu de `objet.get_attribut()`)
- ✅ Pour rendre un attribut en lecture seule (pas de setter)

---

## 🎩 Méthodes Magiques

Les méthodes magiques commencent et finissent par `__` (double underscore). Elles permettent à tes objets d'utiliser les opérateurs Python.

### Les plus importantes

```python
class Argent:
    def __init__(self, montant, devise="DH"):
        self.montant = montant
        self.devise = devise
    
    # Affichage avec print()
    def __str__(self):
        return f"{self.montant} {self.devise}"
    
    # Représentation technique (debug)
    def __repr__(self):
        return f"Argent({self.montant}, '{self.devise}')"
    
    # Addition : a + b
    def __add__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Devises différentes !")
        return Argent(self.montant + autre.montant, self.devise)
    
    # Soustraction : a - b
    def __sub__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Devises différentes !")
        return Argent(self.montant - autre.montant, self.devise)
    
    # Multiplication : a * 2
    def __mul__(self, facteur):
        return Argent(self.montant * facteur, self.devise)
    
    # Égalité : a == b
    def __eq__(self, autre):
        return self.montant == autre.montant and self.devise == autre.devise
    
    # Inférieur : a < b
    def __lt__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Devises différentes !")
        return self.montant < autre.montant
    
    # Supérieur : a > b
    def __gt__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Devises différentes !")
        return self.montant > autre.montant

# Utilisation NATURELLE
prix1 = Argent(100, "DH")
prix2 = Argent(50, "DH")

print(prix1)                    # 100 DH
print(prix1 + prix2)            # 150 DH
print(prix1 - prix2)            # 50 DH
print(prix1 * 2)                # 200 DH
print(prix1 == Argent(100, "DH"))  # True
print(prix1 > prix2)            # True

# Comme des nombres normaux !
total = prix1 + prix2 + Argent(25, "DH")
print(total)  # 175 DH
```

### 📋 Liste complète des méthodes magiques utiles

| Méthode | Utilisation | Exemple |
|---------|-------------|---------|
| `__init__` | Constructeur | `obj = Classe()` |
| `__str__` | Affichage lisible | `print(obj)` |
| `__repr__` | Représentation technique | `repr(obj)` |
| `__len__` | Longueur | `len(obj)` |
| `__getitem__` | Accès par index | `obj[0]` |
| `__setitem__` | Modification par index | `obj[0] = val` |
| `__iter__` | Itération | `for x in obj` |
| `__add__` | Addition | `a + b` |
| `__sub__` | Soustraction | `a - b` |
| `__mul__` | Multiplication | `a * b` |
| `__eq__` | Égalité | `a == b` |
| `__lt__` | Inférieur | `a < b` |
| `__gt__` | Supérieur | `a > b` |
| `__contains__` | Appartenance | `x in obj` |
| `__call__` | Appel comme fonction | `obj()` |

### 🎬 Exemple avancé : Liste personnalisée

```python
class MaListe:
    def __init__(self):
        self._items = []
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, valeur):
        self._items[index] = valeur
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __str__(self):
        return f"MaListe({self._items})"
    
    def ajouter(self, item):
        self._items.append(item)

# Utilisation comme une vraie liste
ma_liste = MaListe()
ma_liste.ajouter("Python")
ma_liste.ajouter("Java")
ma_liste.ajouter("C++")

print(len(ma_liste))          # 3
print(ma_liste[0])            # Python
ma_liste[1] = "JavaScript"    # Modification
print("Python" in ma_liste)   # True

# Itération
for langage in ma_liste:
    print(f"- {langage}")
```

---

## 🔧 Méthodes Statiques et de Classe

### Comparaison rapide

```python
class MaClasse:
    compteur = 0
    
    def __init__(self, nom):
        self.nom = nom
        MaClasse.compteur += 1
    
    # Méthode normale (besoin d'une instance)
    def methode_instance(self):
        return f"Je suis {self.nom}"
    
    # Méthode de classe (accède à la classe, pas à l'instance)
    @classmethod
    def methode_classe(cls):
        return f"Il y a {cls.compteur} instances"
    
    # Méthode statique (ni instance, ni classe nécessaire)
    @staticmethod
    def methode_statique():
        return "Je suis indépendante"

# Utilisation
obj = MaClasse("Test")

print(obj.methode_instance())           # Je suis Test
print(MaClasse.methode_classe())        # Il y a 1 instances
print(MaClasse.methode_statique())      # Je suis indépendante
```

### 🎯 Cas d'usage réels

```python
from datetime import datetime

class Personne:
    def __init__(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance
    
    @property
    def age(self):
        return datetime.now().year - self.annee_naissance
    
    # Constructeur alternatif
    @classmethod
    def depuis_age(cls, nom, age):
        """Créer une personne à partir de son âge"""
        annee = datetime.now().year - age
        return cls(nom, annee)
    
    # Validation
    @staticmethod
    def est_nom_valide(nom):
        """Vérifier si un nom est valide"""
        return len(nom) > 0 and nom.replace(" ", "").isalpha()
    
    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

# Méthode normale (besoin d'un objet)
p1 = Personne("Ahmed", 1990)
print(p1.se_presenter())

# Méthode de classe (constructeur alternatif)
p2 = Personne.depuis_age("Fatima", 25)
print(p2.se_presenter())

# Méthode statique (utilitaire)
print(Personne.est_nom_valide("Ahmed"))    # True
print(Personne.est_nom_valide("123"))      # False
```

### 📊 Quand utiliser quoi ?

| Type | Quand l'utiliser | Exemple |
|------|------------------|---------|
| **Instance** | Besoin des données de l'objet | `self.calculer_total()` |
| **Classe** | Constructeurs alternatifs, agir sur la classe | `@classmethod def depuis_json(cls, json)` |
| **Statique** | Utilitaires, validations, pas besoin de self/cls | `@staticmethod def est_valide(...)` |

---

## 📦 Dataclasses

Les dataclasses réduisent le code répétitif pour les classes qui stockent principalement des données.

### Sans dataclass (beaucoup de code)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y
    
    def __lt__(self, autre):
        return (self.x, self.y) < (autre.x, autre.y)
```

### Avec dataclass (beaucoup plus simple !)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float
    
    def distance_origine(self):
        return (self.x**2 + self.y**2) ** 0.5

# Python génère automatiquement __init__, __repr__, __eq__
p1 = Point(3, 4)
p2 = Point(3, 4)

print(p1)           # Point(x=3, y=4)
print(p1 == p2)     # True
print(p1.distance_origine())  # 5.0
```

### 🎬 Exemple avancé

```python
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0  # Valeur par défaut
    categories: List[str] = field(default_factory=list)  # Liste vide par défaut
    date_ajout: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Appelé après __init__ pour validation"""
        if self.prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        if self.quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")
    
    @property
    def valeur_stock(self):
        return self.prix * self.quantite
    
    def est_disponible(self):
        return self.quantite > 0

# Utilisation
produit = Produit(
    nom="Ordinateur",
    prix=5000,
    quantite=10,
    categories=["Électronique", "Informatique"]
)

print(produit)
print(f"Valeur du stock: {produit.valeur_stock} DH")
print(f"Disponible: {produit.est_disponible()}")

# Comparaison automatique
produit2 = Produit("Ordinateur", 5000, 10, ["Électronique", "Informatique"])
print(produit == produit2)  # False (date_ajout différente)
```

### Options de dataclass

```python
from dataclasses import dataclass

@dataclass(
    frozen=True,      # Rend l'objet immutable (non modifiable)
    order=True,       # Génère __lt__, __le__, __gt__, __ge__
    slots=True        # Utilise __slots__ pour économiser la mémoire
)
class Point3D:
    x: float
    y: float
    z: float = 0.0

p1 = Point3D(1, 2)
# p1.x = 5  # ❌ Erreur : frozen=True
print(p1 < Point3D(2, 3))  # ✅ Fonctionne : order=True
```

---

## 🎪 Gestionnaire de Contexte (`with`)

Le gestionnaire de contexte garantit qu'une ressource est correctement fermée/libérée, même en cas d'erreur.

### Le problème sans `with`

```python
# ❌ MAUVAIS - risque de ne pas fermer le fichier
fichier = open("data.txt", "w")
fichier.write("Hello")
# Si une erreur se produit ici, le fichier ne sera jamais fermé !
raise Exception("Oups")
fichier.close()  # Cette ligne ne sera jamais exécutée
```

### La solution avec `with`

```python
# ✅ BON - fichier fermé automatiquement
with open("data.txt", "w") as fichier:
    fichier.write("Hello")
    raise Exception("Oups")  # Même si erreur...
# Le fichier est TOUJOURS fermé ici !
```

### 🔨 Créer ton propre gestionnaire

```python
class Chronometre:
    def __enter__(self):
        """Appelé au début du bloc 'with'"""
        print("⏰ Chronomètre démarré")
        self.debut = time.time()
        return self  # Retourne l'objet à utiliser
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Appelé à la fin (même si erreur)"""
        self.fin = time.time()
        duree = self.fin - self.debut
        print(f"⏱️ Temps écoulé : {duree:.2f} secondes")
        
        # Si une exception s'est produite
        if exc_type is not None:
            print(f"⚠️ Erreur détectée : {exc_value}")
        
        return False  # False = propage l'exception

# Utilisation
import time

with Chronometre():
    print("Début du traitement...")
    time.sleep(2)
    print("Traitement terminé")
# Le chronomètre affiche automatiquement le temps
```

### 🎬 Exemples pratiques

#### 1. Connexion à une base de données

```python
class ConnexionDB:
    def __init__(self, serveur):
        self.serveur = serveur
        self.connexion = None
    
    def __enter__(self):
        print(f"📡 Connexion à {self.serveur}...")
        self.connexion = f"Connexion active vers {self.serveur}"
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"🔌 Déconnexion de {self.serveur}")
        self.connexion = None
        return False
    
    def executer(self, requete):
        if self.connexion:
            print(f"🔍 Exécution : {requete}")
            return "Résultats..."

# Utilisation - garantit la déconnexion
with ConnexionDB("localhost") as db:
    db.executer("SELECT * FROM clients")
    db.executer("UPDATE produits SET prix = 100