numero = []
for i in range(10):
    numero.append(str(i))

numero2 = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}

with open('suokteur.txt', 'r') as f:
    compteur = 0
    for ligne in f:
        ligne = ligne.replace('\n','')
        for chiffre in ligne:
            compteur = numero.count(chiffre)
            numero2[chiffre] +=compteur

resultat = ''
for i in numero2.items():
    if(i[1]<250 and i[0]!='.'):
        resultat += i[0]*(250-i[1])

print("test :", resultat)
