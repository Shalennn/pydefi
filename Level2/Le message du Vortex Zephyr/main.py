motDepart = 'PASDEPANIQUE'

def listAlphabet():
    return [chr(i) for i in range(ord("A"), ord("Z") + 1)]

n = 3
for i in motDepart:
    if(i in listAlphabet()):
        if( listAlphabet().index(i)+n > 26):
            n -= 26
        #print(listAlphabet()[listAlphabet().index(i)+n])
    n+=10


entree = 'HFKAO ZTEIA ZPJNT VASWY FBRMO GUOYA GJFWP IIOVU KELHB OXMAG JOLEK WHELH XEXDJ HCEWU XPHCK VBULC LEMOM HZ'
testInverse = entree.replace(" ","")
alphabet = listAlphabet()
n = len(alphabet)

for x in range(26):
    for y in range(26):
        motTest = []
        decrement = x
        for lettre in testInverse:
            index = (alphabet.index(lettre) - decrement) % n
            motTest.append(alphabet[index])
            decrement += y
        #print(f"Décalage ini={x}, incrément={y} ==> {''.join(motTest)}")


motTest = []
decrement = 7
for lettre in testInverse:
    index = (alphabet.index(lettre) - decrement) % n
    motTest.append(alphabet[index])
    decrement += 5
print(f"Décalage ini={x}, incrément={y} ==> {''.join(motTest)}")