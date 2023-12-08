import random
import sys


def guessing_game():
    secretnr = random.randint(0, 100)
    typednr = int(input("User, take a guess: "))
    makingsure = 10
    guesses = 3
    try:
        while makingsure > 3:
            if 0 <= typednr <= 100:
                while typednr != secretnr and guesses > 1:
                    if typednr > secretnr:
                        typednr = int(input("Too high! Please try again: "))
                        guesses -= 1
                    elif typednr < secretnr:
                        typednr = int(input("Too low! Please try again: "))
                        guesses -= 1
                if guesses > 1:
                    return sys.exit("Just right! You have won!")
                else:
                    return sys.exit("You have no remains left! You lost!")
            else:
                typednr = int(input("Please type a number between 0 and 100: "))
    except ValueError:
        print("Type a number, not something else!")


print(guessing_game())
