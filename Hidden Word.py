"""strin = input("Please type a word here: ")
lstrin = input("Please type a sequence of letters that will verify if there is the first word in this sentence: ")
letlis = []
for x in strin:
    if x.isalpha():
        letlis.append(x)

ordin = []

for x in range(0, len(letlis)):
    ch = lstrin.find(letlis[x])
    if ch != -1:
        ordin.append(ch)
    else:
        print("There isn't the hidden word")
        break

ordins = sorted(ordin)

if ordin == ordins:
    print("There is the hidden word")
else:
    print("There isn't the hidden word")

# for x in range(0, len(letlis)-1):
#     rword = lstrin.find(letlis[x])
#     lword = lstrin.rfind(letlis[x])
#     if rword < lword:
#         rword = lword
#     else:
#         lstrin = lstrin[0:x:len(lstrin)]"""


# Ask the user for the two strings
word = input("Enter a word: ")
combination = input("Enter a combination of characters: ")

# Check if the characters in the word are hidden in the combination
i = -1
for letter in word:
    i = combination.find(letter, i + 1)
    if i == -1:
        print("No, the characters are not hidden.")
        break
else:
    print("Yes, the characters are hidden.")
