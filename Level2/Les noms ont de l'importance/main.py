
def listAlphabetMinuscule():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

alphabet = listAlphabetMinuscule()
print(alphabet)
reponse = []
with open('input.txt', 'r') as f:
    for mots in f:
        mot = mots
        mots = mots.replace("\n", "")
        motss = mots.replace(' ','').lower()
        resultat = 0
        valeurMot = 0
        # print(mots)
        for j in alphabet:
            compteur = motss.count(j)
            # print(compteur)
            nbLettre = len(motss)
            # print("nombre de lettre",nbLettre)
            if compteur >= 1:
                resultat += 1
        valeurMot = resultat/nbLettre
        reponse.append((mot,valeurMot))
reponse = sorted(reponse, key=lambda valeur: (valeur[1], valeur[0]))
print(reponse[:10])

# TODO UTILISATION DE set() -------------->
# resultat = []
# with open('input.txt', 'r') as f:
#     for mot in f:
#         bonjour = mot
#         bonjour = bonjour.replace("\n","")
#         mot = mot.strip().lower().replace(" ", "")
#         nb_total = len(mot)
#         nb_distinct = len(set(mot))
#         valeur = nb_distinct / nb_total
#         resultat.append((bonjour, valeur))
# resultat = sorted(resultat, key=lambda valeur: (valeur[1], valeur[0]))
# print(resultat[:10])
# TODO ---------------------------------------------------------------------