from sympy import *

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# Lista de cuvinte
cuvinte = ["salut tuturor", "buna ziua", "la revedere"]

# Funcția lambda pentru transformarea cuvintelor
transformare = lambda s: s.upper().replace(" ", "_")

# Aplicăm funcția lambda utilizând map() pentru fiecare cuvânt din lista de cuvinte
rezultat = list(map(transformare, cuvinte))

# Rezultatul va fi o listă cu cuvintele transformate
print(rezultat)

# Homework: CHECK NOTION


# Number 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
func1 = lambda x: x * 0.5
res1 = map(func1, list1)
con1 = list(res1)
print(con1)

# Number 2

list2 = ["Chair", "Table", "Lamp", "Pen", "Pencil", "Curtain", "Cactus", "Shelf"]

func2 = lambda x: x.lower()
res2 = map(func2, list2)
con2 = list(res2)
print(con2)

# Number 3

list3 = ["John Doe", "Mike Willington", "Stefan Cel Mare", "George Washington", "Emmanuel Macron", "Klaus Iohannis",
         "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr."]

print(list(map(lambda x: ''.join([i[0] for i in x.split()]), list3)))

# Number 4

list4 = [17, 3, -4, -9, 0, 32, -13]

print(list(map(lambda x: (x * 9 / 5) + 32, list4)))


# ======================================================
def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


# Create two multiplier functions with different factors

double = make_multiplier(2)

triple = make_multiplier(3)

# Use the multiplier functions

result1 = double(5)  # result1 is 10 (5 * 2)

result2 = triple(5)  # result2 is 15 (5 * 3)

# Number 5
list5 = [0, 1, 2, 4, 6, 9, 10, 14, -15, -17, -3, 19]

print(list(filter(lambda x: x >= 10, list5)))

# Number 6
list6 = ["Tomato", "Cheese", "Bread", "Lettuce", "Chicken", "Egg", "Milk", "Juice", "Water"]

print(list(filter(lambda x: len(x) > 5, list6)))

# Number 7
list7 = ["Astronomy", "Astrology", "Append", "Apple", "Chair", "Table", "Cactus", "Paper", "String"]

print(list(filter(lambda x: x.lower().startswith("a"), list7)))

# Number 8
list8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

print(list(filter(lambda x: isprime(x), list8)))
