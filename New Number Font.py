patterns = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]


def display_digit(num):
    digits = [int(d) for d in str(num)]  # convert number to list of digits
    rows = [""] * 5  # initialize the rows to empty strings
    for digit in digits:
        pattern = patterns[digit]  # get the pattern for the current digit
        for i, row in enumerate(pattern):
            rows[i] += row + " "  # add the current row to the corresponding row of the display
    for row in rows:
        print(row)  # print the final display


display_digit(7325)
