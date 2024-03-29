import statistics as st

"""def list_maker(x):
    list = []
    while x != "\n":
        x = input("Please type a number: ")
        if x != "\n" or x != '':
            list.append(float(x))
        else:
            pass


list_maker(0)
print(list)

def average_sorter():
    pass"""

user_input = input("Enter numbers, (blank line to stop): ")
numbers = []

while user_input.strip() != "":
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input")
    user_input = input("Enter numbers, (blank line to stop): ")

print(numbers)


def average_sorter(numbers):
    aver = st.mean(numbers)
