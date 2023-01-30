"""
#Ex 1: Calculate the multiplication and sum of two numbers
from math import trunc

def exercitii(a,b):
    a = trunc(a)
    b = trunc(b)
    if a * b <= 1000:
        print(a*b)
    else:
        print(a+b)
exercitii(52,17)


#Ex 2: Print characters from a string that are present at an even index number
sentence = input("Write your sentence: ")

for x in range(0, len(sentence)):
    if x % 2 == 0:
        print(sentence[x], end= "")


#Ex 3: Remove first n characters from a string
def remove_chars(chars, n):
    chars = chars[n:]
    return chars


chars = input("Write your sentence: ")
n = int(input("Choose how many letters you want to be deleted from the start of the sentence: "))
print(remove_chars(chars, n))


#Ex 4: Check if the first and last number of a list is the same
my_list = [7, 6, 3, 8, 0, 1, 7]
x = False
if my_list[0] == my_list[len(my_list)-1]:
    x = True
else:
    x = False
print(x)


#Ex 5: Display numbers divisible by 5 from a list
j = int(input("Input a number that will be the length of the list: "))
divcu5 = []
for x in range(0, j):
    b = int(input("Input a number: "))
    divcu5.append(b)
for x in range(0, j):
    if divcu5[x] % 5 == 0:
        print("The number", divcu5[x],"can be divided by 5.")

#Ex 5: The reverse function and how it works
my_list3 = [1, 2, 3, 4, 5]
my_list3.reverse()
print(my_list3)


#Ex 6: Turn every item of a list into its square
l = int(input("Input a number that will be the length of the list: "))
sqrat2 = []
for x in range(0, l):
    g = int(input("Input a number: "))
    sqrat2.append(g)
for x in range(0, l):
    print("The number", sqrat2[x],"and it's square is", sqrat2[x]**2)


#Ex 7: Zip in python
list1 = ["M", "na", "i", "Mi", "Will"]
list2 = ["y", "me", "s", "ke", "ington"]

pyzips = zip(list1, list2)

print(tuple(pyzips))


#Ex 8: Homework
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


# list2.reverse()
# for x in range(0, 4):
#     print(list1[x], "", end="")
#     print(list2[x])

for x in range(0, 6):
    for y in range(0, x):
        print(x, end=" ")
    else:
        print()


#Ex 8: Writing digits in reverse
digitcode = int(input("Please input a code of at least 4 digits: "))

while digitcode > 0:
    print(digitcode % 10, end=" ")
    digitcode = digitcode // 10


#Ex 9: Printing the multiplication table from 1 to 10
x = 0
y = 0

for x in range(1, 11):
    for y in range(1,11):
        print(x*y, end=" ")
    print("\t\t")


#Ex 10: Half of a pyramid but with asterisks
for x in range(5, 0, -1):
    for y in range(0, x):
        print("*", end=" ")
    else:
        print()


#Ex 11: Homework

# Homework

j = 9
for x in range(4, 11, 2):
    print(j*' '+x*'*')
    if j != 5:
        j = j - 1
    else:
        j = j + 1

j = 6
for x in range(10, 3, -2):
    print(j*' '+x*'*')
    if j != 5:
        j = j + 1
    else:
        j = j - 1

#Ex 12: Diamond star pattern
n = 5

# upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()


#Ex 13: Hourglass pattern
n = 5
# downward pyramid
for i in range(n - 2):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()

# upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()


#Ex 14: Hollow Diamond Star Pattern
linnum = 5
spanum = 4
midnum = -2
for x in range(linnum):
    if midnum < 0:
        print(spanum * " " + "*")
    else:
        print(spanum * " " + "*", midnum * " " + "*")
    spanum = spanum - 1
    midnum = midnum + 2

spanum = 1
midnum = 4
for x in range(linnum - 1):
    if midnum < 0:
        print(spanum * " " + "*")
    else:
        print(spanum * " " + "*", midnum * " " + "*")
    spanum = spanum + 1
    midnum = midnum - 2"""
