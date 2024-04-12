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


# def generate_lottey_numbers():
#     return set(sorted(random.sample(range(1, 50), 6)))
#
# import random
#
#
# def generate_lottey_numbers():
#     return set(sorted(random.sample(range(1, 50), 6)))
#
#
# def check_ticket(played_numbers, winning_numbers):
#     return sorted(set(played_numbers)) == winning_numbers
#
#
# lottery_numbers = generate_lottey_numbers()
# print("Welcome to the lottery!")
# user_input = input("Enter your 6 numbers separated by spaces: ")
# # user_numbers = list(map(int, user_input.split()))
# try:
#     user_numbers = [int(num) for num in user_input.split()]
# except ValueError:
#     print("Please enter only numbers.")
#     exit(1)
# if len(user_numbers) != 6:
#     print("Please enter exactly 6 numbers.")
#     exit(1)
# if check_ticket(user_numbers, lottery_numbers):
#     print("Congratulations! You won the lottery!")
# else:
#     print("Sorry, you did not win this time.")
