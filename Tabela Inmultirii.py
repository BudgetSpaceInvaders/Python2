nrt = int(input("Please write a number here --> "))
if nrt == 0:
    print("   1  2  3  4  5  6  7  8  9  0")
if nrt < 0:
    print("Please write a number above 0.")
else:
    print("  1 2 3 4 5 6 7 8 9 0")
    for x in range(1, nrt+1):
        for y in range(1, 10):
            print(x*y, end=" ")
        print()