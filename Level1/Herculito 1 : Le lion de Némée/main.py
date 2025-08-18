entree = ['ARTEMIS', 'ASCLEPIOS' ,'ATHENA', 'ATLAS' ,'CHARON', 'CHIRON','CRONOS' ,'DEMETER','EOS', 'ERIS',
'EROS', 'GAIA', 'HADES' ,'HECATE', 'HEPHAISTOS','HERA', 'HERMES', 'HESTIA', 'HYGIE' ,'LETO' ,'MAIA',
'METIS' ,'MNEMOSYNE','NYX' ,'OCEANOS', 'OURANOS', 'PAN', 'PERSEPHONE','POSEIDON', 'RHADAMANTHE',
'SELENE' ,'THEMIS', 'THETIS' ,'TRITON', 'ZEUS']

def listAlphabet():
    return [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    
listTriee = []

for i in entree:
    sommeMot = 0
    for j in i:
        if(j in listAlphabet()):
            sommeMot += (listAlphabet().index(j)+1)
    listTriee.append((i,sommeMot),)

test= sorted(listTriee, key=lambda x: x[1])
listeFinal = []

for mot in test:
    listeFinal.append(mot[0])
    
print(" ".join(listeFinal))