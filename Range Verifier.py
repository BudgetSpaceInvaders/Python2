def read_int(prompt, min, max):
    while True:
        try:
            f = int(input(prompt))
            if f < min or f > max:
                print("Error: not in range")
            else:
                return f
        except ValueError:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
