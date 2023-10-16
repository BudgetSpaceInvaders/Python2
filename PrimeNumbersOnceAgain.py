def prim_check(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for y in range(2, int(x / 2 + 1)):
            if x % y == 0:
                return False
        return True


# Testăm funcția
numar_dat = int(input("Introduceți un număr: "))

if prim_check(numar_dat):
    print(f"{numar_dat} este un număr prim.")
else:
    print(f"{numar_dat} nu este un număr prim.")
