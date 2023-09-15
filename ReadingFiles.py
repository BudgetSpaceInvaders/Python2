# Deschidem fișierul pentru citire
with open("exemplu.txt", "r") as fisier:
    # Citim conținutul întregului fișier
    continut = fisier.read()

# Închidem fișierul automat folosind blocul 'with'
print(continut)

# Deschidem fișierul pentru scriere
with open("nou.txt", "w") as fisier:
    fisier.write("Acesta este un nou fișier.\n")
    fisier.write("Linia 1\n")
    fisier.write("Linia 2\n")

# Închidem fișierul automat folosind blocul 'with'


# Deschidem fișierul în modul adăugare ('a')
with open("exemplu.txt", "a") as fisier:
    fisier.write("Aceasta este o linie adăugată.\n")

# Închidem fișierul automat folosind blocul 'with'
