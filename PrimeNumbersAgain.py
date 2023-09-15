the_list = []


def prim(x):
    for y in range(2, x):
        if x % y == 0:
            return False
        else:
            continue
    else:
        return True



for x in range(2, 200):
    if prim(x) == True:
        the_list.append(x)
    else:
        pass

print(the_list)
