def listAlphabetMinuscule():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

alphabet = listAlphabetMinuscule()
liste = ["&",'À',"é",'-','è','_',' ',"'",'.',',','«','»','?','!','î','à','ê','ù','(',')',';','ç',':','â','û','\n']
output = []
with open("input.txt", 'r') as f:
    for line in f:
        for i in line:
            i=i.lower()
            if(i not in alphabet and i not in liste):
                output +=str(i)
print(output)