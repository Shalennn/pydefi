roux = 1
blanc = 0
noir = 2

#roux * blanc * noir = 777 * (roux + blanc + noir)
# blanc < roux
# noir > roux & noir < 2 * blanc
# troupeau < 1000
# 
for blanc in range(0,200):
    for roux in range(blanc+1, 200):
        for noir in range (roux+1,200):
            troupeau = blanc+roux+noir
            if(blanc * roux * noir == troupeau * 777):
                if(troupeau <1000 and noir < 2*blanc and blanc < roux):
                    print(troupeau)
