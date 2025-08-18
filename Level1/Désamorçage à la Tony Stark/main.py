n = 1435
somme = 0
i = 0
while i < n:
    if i%3 == 0 or i%5 == 0:
        somme+=i
    i+=1
print(somme)