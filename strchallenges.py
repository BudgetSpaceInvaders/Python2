# Make a function how_many that, given a list of a number
# and a thing name, returns a grammatically correct sentence
# describing the number of things.
#
# >>>> how_many([5, "trinket"])
# There are 5 trinkets.
# >>>> how_many([1, "king"])
# There is 1 king.

def how_many(the_list):
    num = the_list[0]
    thing = the_list[1]
    if num == 1:
        return f"There is {num} {thing}."
    else:
        return f"There are {num} {thing}s."


# Add print statements here to test what your code does:
print(how_many([5, "trinket"]))
print(how_many([1, "king"]))
