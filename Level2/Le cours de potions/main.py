fiole = [20,20,20,0]

# (1/3 de fiole[0] dans fiole[1]) si (fiole[1]+(fiole[0]/3))<25

N=int(input("Nombre de tour souhaité ?\n"))

for i in range(N):
    for j in range(1,4) :
        V=fiole[i%4]
        V_tiers=V/3
        V_s=fiole[(i+j)%4]
        if V_tiers+V_s >25 :
            fiole[i%4]=round(V-(25-V_s),1)
            fiole[(i+j)%4]=25
        else :
            fiole[(i+j)%4]+=V_tiers
            fiole[i%4]-=V_tiers
Finale=[round(i,1) for i in fiole]
print(Finale)

