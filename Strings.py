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
print(valoare) # 6


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


#nrdz = input("Please write a sequence of numbers: ")
# x0 = ["###", "# #", "# #", "# #", "###"]
# x1 = [" # ", " # ", " # ", " # ", " # "]
# x2 = ["###", "  #", "###", "#  ", "###"]
# x3 = ["###", "  #", "###", "  #", "###"]
# x4 = ["# #", "# #", "###", "  #", "  #"]
# x5 = ["###", "#  ", "###", "  #", "###"]
# x6 = ["###", "#  ", "###", "# #", "###"]
# x7 = ["###", "  #", "  #", "  #", "  #"]
# x8 = ["###", "# #", "###", "# #", "###"]
# x9 = ["###", "# #", "###", "  #", "###"]
# for i in range(len(x1)):
#   print(x0[i],x1[i],x2[i], x3[i], x4[i], x5[i], x6[i], x7[i], x8[i], x9[i])

patterns = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]

def display_digit(num):
    digits = [int(d) for d in str(num)]  # convert number to list of digits
    rows = [""] * 5  # initialize the rows to empty strings
    for digit in digits:
        pattern = patterns[digit]  # get the pattern for the current digit
        for i, row in enumerate(pattern):
            rows[i] += row + " "  # add the current row to the corresponding row of the display
    for row in rows:
        print(row)  # print the final display

display_digit(7325)


optsel = int(input("Would you like to cipher(1) or to decipher(2): "))
keycode = int(input("What will be the key of the cipher: "))
citext = ""
if optsel == 1:
    plain = input("Please write a message to be encrypted: ")
    for x in plain:
        if x == " ":
            citext += x
        else:
            citext += chr(ord(x)+keycode)


if optsel == 2:
    plain2 = input("Please write a message to be decrypted: ")
    for y in plain2:
        if y == " ":
            citext += y
        else:
            citext += chr(ord(y)-keycode)
print(citext)"""


# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

