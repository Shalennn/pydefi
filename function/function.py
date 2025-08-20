def listAlphabet():
    return [chr(i) for i in range(ord("A"), ord("Z") + 1)]
def listAlphabetMinuscule():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

def enumerateur(a):
    enumeration = ()
    while a != 0:
        b = a%10
        a = (a - b)//10
        enumeration += (b,)
    return(enumeration)

# Permet de savoir si le nom contient les différents éléments si oui alors return True
def est_valide(a):
    return all(c in "24" for c in str(a))

# permet de savoir combien d'un même élément dans un nombre
def compte_4(a):
    return str(a).count('4')