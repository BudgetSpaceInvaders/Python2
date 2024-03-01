def from_human2dog(years):
    if years < 0:
        return "Error, enter a positive number."
    elif years == 0:
        return "Your dog was just born."
    elif 0 > years <= 2:
        return f"Your dog has {10.5 * years} years."
    else:
        return f"Your dog has {10.5 * 2 + 4 * (years - 2)} years."


try:
    years = float(input("Please enter a number of human years to get dog years: "))
    print(from_human2dog(years))
except ValueError:
    print("Please enter a valid number.")
