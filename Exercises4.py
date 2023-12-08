arr_1 = [7, 2, 5, 9]
arr_1 = sorted(arr_1)


def index_finder(arr_1, target):
    len_arr_1 = len(arr_1) - 1
    if target in arr_1:
        printer1 = f"The number is on position number {arr_1.index(target)}"
        return printer1
    else:
        for x in range(0, len(arr_1)):
            if x >= 1 and x - 1 < target < x + 1 and x > len(arr_1):
                printer2 = f"The number would be on position number {x}"
                return printer2
            elif target < x - 1 and x == 1:
                printer3 = "The number would be before the first position"
                return printer3
            elif target > x and x == len(arr_1) - 1:
                printer4 = f"The number would be on position {len(arr_1)}"
                return printer4
            else:
                printer5 = "I have no idea how you got here."
                return printer5


print(index_finder(arr_1, 1))
