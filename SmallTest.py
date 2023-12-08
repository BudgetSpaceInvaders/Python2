"""
# Task 1: Roman Numerals Into Arabic Numbers
rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
cur_rom = input("Please type a roman numeral here: ")


def rom_to_arab(cur_rom):
    arab_num = 0
    for x in range(len(cur_rom)):
        try:
            if x < len(cur_rom) - 1 and rom_num[cur_rom[x]] < rom_num[cur_rom[x + 1]]:
                arab_num -= rom_num[cur_rom[x]]
            else:
                arab_num += rom_num[cur_rom[x]]
        except BaseException:
            print("Something went wrong, please try again.")
    else:
        print("Your arab number is:", arab_num)


rom_to_arab(cur_rom)

# HOMEWORK: Task: Integer to Roman Numeral Conversion
# Write a Python function that takes an integer as input and converts it into a Roman numeral. The function should return the Roman numeral as a string.


roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
             40: "XL", 50: "L", 90: "XC", 100: "C",
             400: "CD", 500: "D", 900: "CM", 1000: "M"}



def arab_to_rom(num):
    result = ""
    for value, symbol in sorted(roman.items(), reverse = True):
        while num >= value:
            result += symbol
            num -= value
    return result

print(arab_to_rom(2579))"""


def int_to_roman(num):
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    integer_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for i in range(len(integer_values)):
        while num >= integer_values[i]:
            num -= integer_values[i]
            result += roman_symbols[i]
    return result


print(int_to_roman(4321))
