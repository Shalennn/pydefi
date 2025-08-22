
dictionnaire = {
                    0:2,
                    1:3,
                    2:4,
                    3:5,
                    4:6,
                    5:3,
                    6:4,
                    7:5,
                    8:6,
                    9:7
                }

def enumerateur(a):
    enumeration = []
    if a ==0:
        return 0
    while a > 0:
        b = a%10
        a = (a - b)//10
        enumeration += (b,)
    return tuple(reversed(enumeration))

resultat = 0
for i in range(2000,10000):
    compteur = 0
    for j in enumerateur(i):
        if j in dictionnaire:
            compteur += dictionnaire[j]
    compteur -= (len(enumerateur(i))-1)
    if(i%compteur==0):
        # print(compteur)
        resultat +=1
print(resultat)