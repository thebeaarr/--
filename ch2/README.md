## 📌 Chapitre — Encapsulation en Python

### 🔷 Introduction

L’encapsulation est un principe fondamental de la programmation orientée objet. Elle consiste à **protéger les données internes d’un objet** tout en offrant **une interface stable et simple** à l’utilisateur de cet objet.
En Python, même si l’encapsulation repose sur des **conventions de nommage** plutôt que sur des mots-clés stricts (`private`, `protected`…), elle joue un rôle crucial dans la création d’objets **fiables, robustes et faciles à maintenir**.

---

### 🔷 1. Principe général

Encapsuler signifie **masquer les détails internes d’implémentation** et n’exposer à l’extérieur que ce qui est nécessaire — l’**interface publique**.

➡ L’utilisateur d’une classe ne doit pas connaître ni manipuler directement la structure interne des données
➡ L’implémentation interne peut évoluer sans casser le code des utilisateurs si l’interface reste stable

---

### 🔷 2. Conventions d’accès aux attributs en Python

| Syntaxe | Niveau d’accès | Intention                                |
| ------- | -------------- | ---------------------------------------- |
| `nom`   | Public         | Utilisation normale                      |
| `_nom`  | Protégé        | Interne à la classe (ou sous-classes)    |
| `__nom` | Quasi-privé    | Protection renforcée via *name mangling* |

#### 🔹 Attribut protégé `_`

```python
class Capteur:
    def __init__(self):
        self._donnees_brutes = []  # Attribut interne
```

L’attribut reste accessible, mais le nom `_` indique qu’il **ne doit pas être manipulé depuis l’extérieur**.

#### 🔹 Attribut quasi-privé `__`

```python
class Compte:
    def __init__(self, solde):
        self.__solde = solde  # Transformé en _Compte__solde en interne
```

Le double souligné active un renommage automatique pour **éviter les conflits et les accès accidentels**.

---

### 🔷 3. Les propriétés : contrôler l’accès aux données

Les propriétés (`@property`) permettent de gérer l’accès aux attributs tout en conservant une syntaxe simple.

#### 🔹 Lecture seule (attribut calculé)

```python
class Rectangle:
    def __init__(self, largeur, hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    @property
    def surface(self):
        return self._largeur * self._hauteur
```

#### 🔹 Setter avec validation

```python
class CompteBancaire:
    def __init__(self, solde_initial=0):
        self._solde = solde_initial

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, montant):
        if montant < 0:
            raise ValueError("Solde négatif interdit")
        self._solde = montant
```

---

### 🔷 4. Séparation interface / implémentation

L’interface publique est constituée des méthodes accessibles par les utilisateurs.
L’implémentation interne peut changer librement sans impacter l’extérieur.

```python
class Logger:
    def log(self, message):  # Interface publique
        horodatage = self._now()  # Méthode interne
        print(f"[{horodatage}] {message}")

    def _now(self):
        from datetime import datetime
        return datetime.now().isoformat(timespec="seconds")
```

➡ L’utilisateur appelle **`log()`** sans connaître l’existence ou les détails de **`_now()`**.

---

### 🔷 5. Bonnes pratiques

✔ Utiliser des noms sans souligné pour l’interface publique
✔ Préfixer les attributs internes par `_` ou `__`
✔ Utiliser `@property` pour validation, contrôle et calcul automatique
✔ Garantir l’intégrité de l’objet dès `__init__` et dans les setters
✔ Tester et documenter uniquement **l’interface publique**

---

### ✨ Conclusion

L’encapsulation constitue un pilier de la conception orientée objet.
En Python, même si elle repose sur des conventions, elle permet de :

🔹 protéger l’état interne d’un objet
🔹 maintenir la cohérence et éviter les erreurs d’utilisation
🔹 simplifier l’interface pour l’utilisateur
🔹 rendre le code évolutif et maintenable

Un bon usage de l’encapsulation donne des classes **claires, fiables et professionnelles**.

---
