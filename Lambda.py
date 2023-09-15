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
