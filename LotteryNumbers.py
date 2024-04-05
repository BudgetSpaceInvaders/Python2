from random import randint

ticket = set()
# for x in range(0, 6):
#     ticket.add(randint(1, 49))
while len(ticket) < 6:
    ticket.add(randint(1, 49))
ticket = sorted(ticket)

guessed_numbers = set()
cur_nr = 0
nr_tries = 6
try:
    for x in range(0, nr_tries):
        cur_nr = int(input("Please type a number between 0 and 50: "))
        if cur_nr <= 0 or cur_nr >= 50:
            raise TypeError
        if cur_nr in ticket:
            print(f"The number {cur_nr} is in the lottery ticket!")
            guessed_numbers.add(cur_nr)
        else:
            print(f"Wrong! The ticket was {ticket}!")
            break
except TypeError:
    print("Please type a number between 0 and 50, not a string!")
guessed_numbers = sorted(guessed_numbers)

if guessed_numbers == ticket:
    print("Against all odds, you won!")
else:
    print("You lost! Better luck next time!")
