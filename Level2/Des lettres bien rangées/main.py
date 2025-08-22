import unicodedata
with open('liste_mots_donna.txt', 'r') as f:
    mots = []
    for line in f:
        mots.append(line.strip())

def normaliser(mot):
    mot = mot.lower()
    mot = unicodedata.normalize('NFD', mot)
    return ''.join(l for l in mot if unicodedata.category(l) != 'Mn')

compteur = 0
for mot in mots:
    mot = normaliser(mot)
    if(all(mot[i] <= mot[i+1] for i in range(len(mot)-1)) and len(mot)>= 3):
        compteur+=1
print(compteur)
