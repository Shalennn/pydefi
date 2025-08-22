from datetime import date, timedelta

semaine = {
    0:len('lundi'),
    1:len('mardi'),
    2:len('mercredi'),
    3:len('jeudi'),
    4:len('vendredi'),
    5:len('samedi'),
    6:len('dimanche')
}

debut = date(2000,1,1)
fin = date(2025,8,22)

compteur = 0
d = debut
while d <= fin:
    jourSemaine = d.weekday()
    longeurJour = semaine[jourSemaine]
    print(d.weekday())
    if(d.day + longeurJour)%10 == 0:
        compteur +=1
    d+= timedelta(days=1)
print(compteur)