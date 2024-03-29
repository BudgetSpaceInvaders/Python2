n = int(input("Number of days: "))
sum = 0

for i in range(1, n, 1):
    print("Day", i)
    x = int(input("Number of tickets: "))
    sum += x

print(f"Total number of tickets sold is {sum}.")