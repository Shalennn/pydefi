##
# 3 nombre entier < 1000
# somme des 3 && produits des 3 ne contient que des 4 et des 2
# 
# 
# 
# ##
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from function.function import *

start = time.time()
# def serviette(a):
#     compteur = 0
#     for i in range(len(enumerateur(a))):
#         if(enumerateur(a)[i]!=2 and enumerateur(a)[i]!=4):
#             return False
#         else:
#             compteur +=1
#         if (compteur == len(enumerateur(a))):
#             return True

# bleauta = []
# maximum = (0,0,0,0)
# for i in range(999):
#     for j in range(999):
#         for k in range(999):
#             somme = i*j*k
#             produit = i+j+k
#             if(serviette(somme)== True and serviette(produit) == True):
#                 #print(i,j,k,)
#                 test = 0
#                 for l in range(len(enumerateur(i))):
#                     if(enumerateur(i)[l]==4):
#                         test+=1
#                 for m in range(len(enumerateur(j))):
#                     if(enumerateur(j)[m]==4):
#                         test+=1
#                 for n in range(len(enumerateur(k))):
#                     if(enumerateur(k)[n]==4):
#                         test+=1
#                 testbis = (i,j,k,test)
#                 if(testbis[3]>maximum[3]):
#                     maximum = testbis
# print(maximum)


# ~~~~~~~~~~~~OPTIMISATION~~~~~~~~~~~~~~
def est_valide(a):
    return all(c in "24" for c in str(a))

def compte_4(a):
    return str(a).count('4')

maximum = (0,0,0,0)
for i in range(400):
    for j in range(400):
        for k in range(400):
            produit = i*j*k
            somme = i+j+k
            if est_valide(somme) and est_valide(produit):
                nb4 = compte_4(i) + compte_4(j) + compte_4(k)
                if nb4 > maximum[3]:
                    maximum = (i, j, k, nb4)
print(maximum)
# ~~~~~~~~~~~~OPTIMISATION~~~~~~~~~~~~~~

print(time.time() - start)
