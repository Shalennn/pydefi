etage = 50
somme = 0
while etage > 0:
    pomme = etage * etage
    if(pomme%3==0):
        somme += pomme
    etage -=1
print(somme)