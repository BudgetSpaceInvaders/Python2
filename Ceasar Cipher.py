import sys

optsel = int(input("Would you like to cipher(1) or to decipher(2): "))
keycode = int(input("What will be the key of the cipher: "))
citext = ""
if optsel == 1:
    plain = input("Please write a message to be encrypted: ")
    for x in plain:
        if x == " ":
            citext += x
        else:
            citext += chr(ord(x) + keycode)

if optsel == 2:
    plain2 = input("Please write a message to be decrypted: ")
    for y in plain2:
        if y == " ":
            citext += y
        else:
            citext += chr(ord(y) - keycode)
print(citext)

plain = input("Please write a message to be encrypted: ")
keycode = int(input("What will be the key of the cipher(1-25): "))
if keycode > 0 and keycode < 26:
    pass
else:
    print("Please print a number between 1 and 25 as the key code!")
    sys.exit()
citext = ""
y = 0
for x in plain:
    if x == " ":
        citext += x
    elif not x.isalpha():
        citext += x
    else:
        x = chr(ord(x) + 1)
        if x.isalpha() and y != x:
            y += 1
        elif not x.isalpha() and x.isupper():
            x = chr(90)
        elif not x.isalpha() and x.islower():
            x = chr(122)
        elif y == x:
            citext += x
        elif not x.isalpha() and y == x and x.islower():
            citext += chr(122)
        elif not x.isalpha() and y == x and x.isupper():
            citext += chr(90)
print(citext)


def caesar_cipher(text, shift):
    # Encrypts text using a Caesar cipher with a variable shift value.
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted


text = input("Enter text to encrypt: ")
while True:
    shift = input("Enter shift value (1-25): ")
    if shift.isdigit() and 1 <= int(shift) <= 25:
        shift = int(shift)
        break
    else:
        print("Invalid shift value. Please enter a number between 1 and 25.")

encrypted = caesar_cipher(text, shift)
print("Encrypted text: ", encrypted)
