import random
import sys

# n = 3
# m = 3
# massiv =[[0]*n]
# d = int(input("Enter the dimension of array: "))
# for i in range(n):
#         massiv[i]=[0]*m
# print(massiv)

d = int(input("Enter the dimension of array: "))
massiv = [[int(j) for j in input("Enter the data :").split()] for i in range(d)]
# massiv = []
# for i in range(d):
#     row = []
#     for j in range(d):
#         row.append(random.randint(1, d))
#     massiv.append(row)

for row in massiv:
    for elem in row:
        if elem > 0 and elem <= d:
            print(elem, end=" ")
        else:
            print(
                "Please write the data to be between the numbers 0 and the number of the dimension you chose next time!")
            sys.exit()
    print()


# for row in massiv:
#     for elem in row:
#         print(elem, end=" ")
#     print()

def RowChecker():
    for row in massiv:
        Sudoku = True
        a = set(row)
        if d == len(a):
            Sudoku = True
        else:
            return False
    return Sudoku


def ColChecker():
    for row in range(d):
        col_set = set()
        for col in range(d):
            col_set.add(massiv[col][row])
        if len(col_set) == d:
            Sudok2 = True
        else:
            return False
    return Sudok2


def SudokuChecker():
    r = RowChecker()
    c = ColChecker()
    # if r == False or c == False:
    #     print("This isn't a Sudoku!")
    if r == True and c == True:
        print("This is a Sudoku!")
    else:
        print("This isn't a Sudoku!")


SudokuChecker()
