from random import randint
ticket = set()
# for x in range(0, 6):
#     ticket.add(randint(1, 49))
while len(ticket) < 6:
    ticket.add(randint(1, 49))
ticket = sorted(ticket)
print(ticket)

# HOMEWORK: USER INTRODUCES NUMBERS AND THEN IF CORRECT ADDS TO SET, IF SET EQUALS SET, USER WINS !!!1!11!1!!1
