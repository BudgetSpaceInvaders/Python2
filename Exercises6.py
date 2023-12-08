# The used list

nr_list = [2, 4, 6]


# The function
def my_sum(*nr_list):
    final_answer = 0
    try:
        for x in nr_list:
            # Summing the numbers up
            final_answer += x
    except TypeError:
        print("No strings, only integers!")
        # The returning
    return final_answer



# The actual output
print(my_sum(10, 13, 18, 4, 0, 6, 17, 12, 20))
