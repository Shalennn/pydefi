from collections import Counter

with open("suokteur.txt", "r") as f:
    grille = [ligne.strip() for ligne in f if ligne.strip()]
print("grille :",grille)

# Comptage des chiffres et des trous
compte = Counter("".join(grille))

# Dimensions
nb_cases = sum(len(l) for l in grille)
cible = nb_cases // 10  # chaque chiffre doit apparaître exactement cible fois

# Construction du résultat
resultat = ""
for d in map(str, range(10)):
    manquants = cible - compte.get(d, 0)
    if manquants > 0:
        resultat += d * manquants

# print(resultat)
