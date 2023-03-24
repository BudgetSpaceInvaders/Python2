strin = input("Please type a word here: ")
lstrin = input("Please type a sequence of letters that will verify if there is the first word in this sentence: ")
letlis = []
for x in strin:
    if x.isalpha():
        letlis.append(x)

for x in range(len(letlis)):
    rword = lstrin.find(letlis[x])
    lword = lstrin.find(letlis[x+1])
    if rword < lword:
        rword = lword
    else:
        lstrin = lstrin[0:x:len(lstrin)]
