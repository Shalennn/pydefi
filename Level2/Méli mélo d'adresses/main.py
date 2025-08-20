entreeDuProblem = "1a6e1g1i1l1m1n1o2r2s2u1y"

def listAlphabetMinuscule():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

alphabet = listAlphabetMinuscule()

with open("adresse.txt", "r") as fichier:
    content = fichier.readlines()
    longueur = len(content)
    sommeDesI = 0
    for i in range(longueur):
        phrase = content[i].replace(" ", "")
        result =''
        for j in alphabet:
            compteur = phrase.count(j)
            if compteur > 0:
                result += str(compteur) + j
        if(result == entreeDuProblem):
            print(content[i])
