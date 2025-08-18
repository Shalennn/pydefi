nEntree = 797114

U = nEntree // 1000
N = nEntree % 1000
print(type(N))
for i in range(N):
    U = (U*13)%1000
    i+=1
print(U)