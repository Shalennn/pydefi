# ## Niveau Débutant+
from collections import Counter

#! 1. **Compter les lettres d’un mot**

#    * Écris un programme qui prend un mot en entrée et affiche combien de fois chaque lettre apparaît.
#    * Exemple : `"abracadabra"` → `{'a':5, 'b':2, 'r':2, 'c':1, 'd':1}`.

exo1 = 'abracadabra'
print(Counter(exo1))


#! 2. **Compter les mots d’une phrase**

#    * À partir d’une chaîne `"le chat mange le fromage"`, affiche combien de fois chaque mot apparaît.
exo2 = "le chat mange le fromage"
exo2 = exo2.split()
print(Counter(exo2))

#! 3. **Trouver la lettre la plus fréquente**

#    * Avec une phrase donnée, identifie la lettre (hors espaces) la plus fréquente.
#    * Exemple : `"hello world"` → `"l"` apparaît 3 fois.
exo3 = "hello world"
test3 = Counter(exo3.replace(" ",''))
plusSouvent = test3.most_common(1)
print("Exo 3:",plusSouvent)
# ---

# ## Niveau Intermédiaire

#! 4. **Comparer deux textes**

#    * Compte les lettres dans deux textes différents.
#    * Trouve quelles lettres apparaissent plus souvent dans le premier texte que dans le second.
print('Exo 4 :')
texteUn = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
texteDeux = "Sed ornare sed metus a ullamcorper."
a = Counter(texteUn.replace(" ",''))
b = Counter(texteDeux.replace(" ",''))

soustraction = a - b
print(soustraction)

#! 5. **Nettoyage automatique avant comptage**
import re
#    * À partir d’un paragraphe (mélange de majuscules, ponctuation), compte les occurrences de chaque mot après avoir :

#      * converti en minuscules
#      * retiré la ponctuation
#      * découpé en mots.
print('Exo 5 :')
texteUn = "Lorem I!:;,psum dolor sit amet, consectetur adipiscing elit."
mots = re.findall(r"\w", texteUn.lower())
print(Counter(mots))
#! 6. **Top-N éléments**

#    * Trouve les 3 mots les plus fréquents dans un texte.
#    * Exemple : `"chien chat chien lapin chien chat"` → `chien:3, chat:2, lapin:1`.
print('Exo 6 :')
texte = "chien chat chien lapin chien chat"
texteBis = texte.split()
print(Counter(texteBis))
# ---

# ## Niveau Intermédiaire+

#! 7. **Histogramme de fréquences**
print('Exo 7 :')
#    * À partir d’un texte, utilise `Counter` pour compter les lettres.
#    * Affiche ensuite un petit histogramme en console, par exemple :
texteUn = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
texteBis = texteUn.replace(' ','')
a = Counter(texteBis)

print(a)
for lettre,nb in a.items():
    print(f"{lettre}: {'*'*nb}")
#      ```
#      a: *****
#      b: **
#      c: *
#      ```

#! 8. **Anagrammes**

#    * Écris une fonction qui teste si deux mots sont des anagrammes (mêmes lettres avec mêmes fréquences).
#    * Exemple : `"listen"` et `"silent"` → True.
print('Exo 8 :')
mot1 = "listen"
mot2 = "silent"
print(Counter(mot1) == Counter(mot2))

