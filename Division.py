import random


def generate_division_examples(a, b):
    # Integer division
    int_division = a // b
    print(f"{a} // {b} = {int_division} (Integer Division)")

    # Floating-point division
    float_division = a / b
    print(f"{a} / {b} = {float_division} (Floating-Point Division)")

    # Modular division (remainder)
    remainder = a % b
    print(f"{a} % {b} = {remainder} (Modular Division)")


# Input two numbers from the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
# Check if the second number is not zero (to avoid division by zero)
if num2 != 0:
    generate_division_examples(num1, num2)
else:
    print("Error: Division by zero is not allowed.")
