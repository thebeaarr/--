from article import Article

a1 = Article("A100", "Clavier mécanique", 79.90, 12)
a2 = Article("A200", "Souris gamer", 49.90, 25)
a3 = Article("A300", "Écran 27 pouces", 199.90, 8)

articles = (a1, a2, a3)

for a in articles:
    print(a)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} DH")
