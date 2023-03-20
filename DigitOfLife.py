# bday = input("Please write your birthday date(in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")
# lsbday = []
# for x in bday:
#     if x.isdigit():
#         lsbday.append(int(x))
#
# answ = sum(lsbday)
#
# print(answ)
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# if answ not in nums:
#     lsbday.clear()
#     for x in str(answ):
#         if x.isdigit():
#             lsbday.append(int(x))
#             answ = sum(lsbday)
#     print(answ)
#
# alfa = 0
# numar = 0
# while answ > 0:
#     numar += answ % 10
#     answ = answ // 10
#     if numar < 10:
#         print(numar)
#     if numar > 9:
#         alfa += numar % 10
#         numar = numar // 10
#         if alfa < 10:
#             print(alfa)


# Ask the user for their birthday
birthday = input("Enter your birthday (YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")

# Remove all non-numeric characters
birthday = "".join(filter(str.isdigit, birthday))

# Calculate the Digit of Life
while len(birthday) > 1:
    birthday = str(sum(int(digit) for digit in birthday))

# Output the result
print("Your Digit of Life is:", birthday)
