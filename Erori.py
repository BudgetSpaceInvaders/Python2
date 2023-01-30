"""class FormulaError(Exception):
    pass
calc = input("Please input the number of variables: ")

try:
    calc = int(calc)
except ValueError:
    print("Introduce a natural number")

if calc < 2:
    print("Please write a number that is equal or greater then 2")

listnr = []

while len(listnr) != calc:
    x = input("Please insert a number: ")

    try:
        x = float(x)
        listnr.append(x)
    except ValueError:
        print("Introduce a natural number")

print(listnr)

# oper = calc - 1
# opernr = []
# perop = ["-", "+", "*", "/", "//", "%", "**"]
#
# for y in range(0, oper):
#     x = input("Please insert an operation: ")
#     if x not in perop:
#         x = input("Please insert an operation: ")
#     else:
#         opernr.append(x)


class FormulaError(Exception):
    pass
calc = input("Please input the number of variables: ")

try:
    calc = int(calc)
except ValueError:
    print("Introduce a natural number")

if calc < 2:
    print("Please write a number that is equal or greater then 2")

listnr = []

while len(listnr) != calc:
    x = input("Please insert a number: ")

    try:
        x = float(x)
        listnr.append(x)
    except ValueError:
        print("Introduce a natural number")

print(listnr)

oper = calc - 1
opernr = []
perop = ["-", "+", "*", "/", "//", "%", "**"]
while len(opernr)<oper:
#for y in range(0, oper):
    x = input("Please insert an operation: ")
    if x not in perop:
        x = input("Please insert another operation: ")
    else:
        opernr.append(x)
print(opernr)

ecuatie = []

for x in range(0, calc-1):
    ecuatie.append(listnr[x])
    if len(opernr) < len(listnr):
        ecuatie.append(opernr[x])
else:
    ecuatie.append(listnr[calc-1])
print(ecuatie)


while oper > 0:
    x = 1
    poz = 1
    prim = x - 1
    if ecuatie[x] == "+":
        ras = ecuatie[prim] + ecuatie[poz + 1]
    if ecuatie[x] == "-":
        ras = ecuatie[prim] - ecuatie[poz + 1]
    if ecuatie[x] == "*":
        ras = ecuatie[prim] * ecuatie[poz + 1]
    if ecuatie[x] == "/":
        ras = ecuatie[prim] / ecuatie[poz + 1]
    if ecuatie[x] == "//":
        ras = ecuatie[prim] // ecuatie[poz + 1]
    if ecuatie[x] == "%":
        ras = ecuatie[prim] % ecuatie[poz + 1]
    if ecuatie[x] == "**":
        ras = ecuatie[prim] ** ecuatie[poz + 1]
    oper = oper - 1
    ecuatie = ecuatie[3:]
    ecuatie.insert(0, ras)
    print(ecuatie)


#Statement 1
str1 = input(str("Please write a sentence here --> "))
print(str1[2])
print(str1[-2])
print(str1[0:5])
print(str1[:-2])

for x in range(0, len(str1), 2):
    print(str1[x], end="")
print("")

for y in range(1, len(str1), 2):
    print(str1[y], end="")
print("")
print(str1[::-1])
for x in range(len(str1)-1, 0, -2):
    print(str1[x], end="")
print("")
print(len(str1))


#Statement 2
str2 = input(str("Please write a sentence here --> "))
ras = str2.count(" ") + 1
print("There are", ras, "words in this sentence")


#Statement 3
str3 = input(str("Please write a sentence here --> "))
rezo = len(str3)
rezol = rezo // 2
if rezo % 2 == 0:
    print(str3[0:rezol])
    print(str3[rezol:len(str3)])
else:
    print(str3[0:rezol+1])
    print(str3[rezol+1:len(str3)])



str33 = input("Please write a sentence here --> ")
rezolv = (len(str33)+1)//2
print(str33[rezolv:len(str33)], end="")
print(str33[0:rezolv])

print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

#Statement 4
str4 = input("Please write a sentence here --> ")
rezolva = str4.index(" ")
print(str4[rezolva+1:len(str4)], end=" ")
print(str4[0:rezolva])


#Statement 5
str5 = input("Please write a sentence here --> ")
rez1 = str5.find("f")
rez2 = str5.rfind("f")
if str5.count("f") == 1:
    print(rez1)
elif str5.count("f") >= 2:
    print(rez1, rez2)


#Statement 6
str6 = input("Please write a sentence here --> ")
fcnt = str6.count("f")
if fcnt >= 2:
    rez3 = str6.find("f")
    rez4 = str6.find("f", rez3+1)
    print("The second occurrence of the letter f appears on the index", rez4)
if fcnt == 1:
    rez3 = str6.find("f")
    print("-1")
if fcnt == 0:
    print("-2")


#Statement 7
str7 = input("Please write a sentence here in which h occurs at least twice --> ")
rez5 = str7.count("h")
if rez5 >= 2:
    rez6 = str7.find("h")
    rez7 = str7.rfind("h")
    print(str7[0:rez6], end="")
    print(str7[rez7+1:len(str7)])
else:
    print("Please insert a sentence that has at least 2 occurrences of the letter h")"""
