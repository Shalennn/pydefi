import re

releveTooms = [10, 12, 6, 9, 18.5, 22, 7, 4, 9, 10]

with open("donneesEntree.txt", "r") as donneeEntree:
    content = donneeEntree.readlines()
    longueur = len(content)
    sommeDesI = 0
    for i in range(longueur):
        test = re.split(" - |, |\n", content[i])
        test.pop(len(test)-1)
        test.pop(0)
        ecart = 0
        compteur = 0
        for j in range (len(test)):
            a = round(float(test[j]),2)
            b = round(releveTooms[j],2)
            c = round(a - b,2)
            if(j == 0):
                ecart = c
                ecart = round(ecart,2)
            if(c != ecart):
                pass
            else:
                compteur+=1
        if(compteur == len(test)):
            sommeDesI += (i+1)
    print(sommeDesI)



#~~~~~~~~~~~~~~~~~~~~~~ "Opti" chat gpt ~~~~~~~~~~~~~~~~~~~~~~~
# def somme_indices_fichier(path, reference):
#     somme = 0
#     with open(path, "r", encoding="utf-8") as f:
#         for i, ligne in enumerate(f, start=1):
#             # Sépare l'ID du reste, en tolérant les espaces
#             parts = re.split(r"\s*-\s*", ligne.strip(), maxsplit=1)
#             if len(parts) != 2:
#                 continue  # ligne mal formée

#             _, droite = parts  # on ignore l'ID
#             # Découpe les valeurs en tolérant les espaces après/avant la virgule
#             try:
#                 mesures = [float(x) for x in re.split(r"\s*,\s*", droite) if x]
#             except ValueError:
#                 continue  # valeur non numérique

#             if len(mesures) != len(reference):
#                 raise ValueError(f"Longueur différente à la ligne {i}: {len(mesures)} vs {len(reference)}")

#             # Écarts arrondis au centième et test "tous égaux"
#             ecarts = [round(m - r, 2) for m, r in zip(mesures, reference)]
#             if all(e == ecarts[0] for e in ecarts):
#                 somme += i
#     return somme

# print(somme_indices_fichier("donneesEntree.txt", releveTooms))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
