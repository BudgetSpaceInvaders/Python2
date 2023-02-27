"""
# # Example 1

word = 'by'
print(len(word))

# Example 2

empty = ''
print(len(empty))

# Example 3
# Don't forget that a backslash (\) used as an escape character is not included in the string's total length.
# The code in Example 3, therefore 0outputs 3.

i_am = 'I\'m'
print(len(i_am))

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
#The asterisk makes the string be replicated as many times as the number it is multiplied with
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function.

char_1 = 'Ð'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function.

print(chr(197))
print(chr(205))

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


#Capitalize
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())


# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))


def mysplit(strng):
    strng = strng.lstrip()
    x = " "
    words = []
    y = 0
    for z in range(0, len(strng)):
        if strng[z] == x:
            words.append(strng[y:z])
            y = z + 1
    return words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#Homework: Fiecare sarcina separat dau commit and push
#https://www.geeksforgeeks.org/multi-dimensional-lists-in-python/
nr1 = [["#"],["#"],["#"]]
for x in range(0, len(nr1)):
    for y in range(0, len(nr1(x))):
        print(nr1[x][y], end = " ")


matrice = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
valoare = matrice[1][2] # rândul 2 este al doilea element al listei principale, iar coloana 3 este al treilea element al listei din acel rând
print(valoare) # 6"""


nrt = int(input("Please write a number here --> "))
if nrt == 0:
    print("   1  2  3  4  5  6  7  8  9  0")
if nrt < 0:
    print("Please write a number above 0.")
else:
    print("  1 2 3 4 5 6 7 8 9 0")
    for x in range(1, nrt+1):
        for y in range(1, 10):
            print(x*y, end=" ")
        print()
