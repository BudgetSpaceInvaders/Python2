import math

x = input("Enter x: ")
try:
    x = float(x)
    try:
        y = math.sqrt(x)
        print("The square root of", x, "equals to", y)
    except ValueError:
        print("Please enter a natural number.")
except ValueError:
    print("Please input a number, not a string.")

# try:
#     y = math.sqrt(x)
#     print("The square root of", x, "equals to", y)
# except ValueError:
#     print("Please enter a natural number.")
