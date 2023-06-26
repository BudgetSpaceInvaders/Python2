import math

dictionar = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# First exercise
"""sum = 0
for x in dictionar:
    sum += dictionar[x]
print(sum)
# Second exercise
print(max(dictionar.values()))
# Third exercise
str1 = input("Please write a line of words: ")
str2 = input("Please write a second line of words: ")
str1.lower()
str2.lower()
str1.replace(" ", "")
str2.replace(" ", "")
str1 = ''.join(c for c in str1 if c.isalpha())
str2 = ''.join(c for c in str2 if c.isalpha())
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
else:
    print("The strings aren't the same length.")"""
# Fourth Exercise
point = int(input("Please write a number: "))
sum = 0


def check_prim(primnr):
    if primnr < 2:
        return False
    for i in range(2, primnr):
        if primnr % i == 0:
            return False
    return True


for x in range(2, point):
    if check_prim(x):
        sum += x
print(sum)
