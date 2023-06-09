def fruit_labeler(thing):
    if type(thing) == int:
        print("oranges")
    elif type(thing) == str:
        print("apples")
    else:
        print("bananas")


fruit_labeler(4)


def fruit_labeler2(thing2):
    if isinstance(thing2, int):
        return "oranges"
    elif isinstance(thing2, str):
        return "apples"
    else:
        return "bananas"


print(fruit_labeler2(4))
