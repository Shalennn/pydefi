monstre = [0,0,0,0]

# Attaque de antonio
killChauv = 2
killSkel = 1
killZomb = 1
killFanto = 1

for i in range(1,3001):
    if(i%2==0):
        #ajout des chauves-souris
        monstre[0] +=10
    if(i%5==0):
        #ajout des skelets
        monstre[1] +=5
    if(i%6==0):
        #ajout des zombies
        monstre[2] +=4
        # il tue des chauves-souris
        monstre[0] -= killChauv
    if(i%10==0):
        #ajout des fantomes
        monstre[3] += 3
    #! Attaque skelette
    if(i%20==0):
        monstre[1] -= killSkel
    #! Attaque zombie
    if(i%30==0):
        monstre[2] -= killZomb
    #! Attaque fantome
    if(i%40==0):
        monstre[3] -= killFanto
        # Attaque de antonio
    if(i%240==0):
        killChauv += 2
        killSkel += 1
        killZomb += 1
        killFanto += 1
print(monstre)