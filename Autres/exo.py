# UTILISATION DE LA FONCTION all() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Exo 1 : --------------------------------------------------
# Vérifie si tous les nombres d’une liste sont positifs.
# Exemple : [3, 5, 7, 10] → True, [3, -1, 7] → False.
liste1 = [3, 5, 7, 10]
liste2 = [3, -1, 7]
print("Exercice 1 #######################")
print(all(i>0 for i in liste1))
print(all(i>0 for i in liste2))


#Exo 2 : --------------------------------------------------
# Vérifie si tous les mots d’une liste commencent par une majuscule.
# Exemple : ["Paris", "Rome", "Berlin"] → True.
print("Exercice 2 #######################")
liste3 = ["Paris", "Rome", "Berlin"]
print(all(i[0].isupper() for i in liste3))

#Exo 3 : --------------------------------------------------
# Vérifie si une phrase ne contient que des lettres (pas de chiffres, pas de symboles).
# Exemple : "Bonjour" → True, "Hello123" → False.
print("Exercice 3 #######################")
mot1 = "Bonjour"
mot2 = "Hello123"
print(all(i.isalpha() for i in mot1)) # True
print(all(i.isalpha() for i in mot2)) # False


# Exercices intermédiaires

#Exo 4 : --------------------------------------------------
# On te donne une liste de tuples représentant des coordonnées (x, y).
# Vérifie si tous les points sont dans le premier quadrant (c.-à-d. x > 0 et y > 0).
print("Exercice 4 #######################")


#Exo 5 : --------------------------------------------------
# On te donne une liste de mots. Vérifie si tous ont la même longueur.
# Exemple : ["chat", "lion", "ours"] → True.
print("Exercice 5 #######################")
liste5 = ["chat", "lion", "ours"]
liste6 = ["chat", "lion", "ours", "cheval"]
print(all(len(i)==len(liste5[0]) for i in liste5))
print(all(len(i)==len(liste6[0]) for i in liste6))

#Exo 6 : --------------------------------------------------
# On te donne une liste de nombres. 
# Vérifie s’ils sont tous pairs et consécutifs (par ex. [2, 4, 6, 8]).
print("Exercice 6 #######################")
liste7 = [2, 4, 6, 8, 10]
liste8 = [2, 3, 6, 8, 10]

def estUneSuite(liste):
    if len(liste) < 2:
        return True
    diff = liste[1] - liste[0]
    return all(b - a == diff for a,b in zip(liste, liste[1:]))

print(all(i%2==0 and estUneSuite(liste7) for i in liste7))
print(all(i%2==0 and estUneSuite(liste8) for i in liste8))


#Exo 7 : --------------------------------------------------
# Écris une fonction qui prend une liste de listes (matrice) et 
# retourne True si toutes les sous-listes ont la même longueur.
print("Exercice 7 #######################")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~