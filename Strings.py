"""
# # Example 1

word = 'by'
print(len(word))

# Example 2

empty = ''
print(len(empty))

# Example 3
# Don't forget that a backslash (\) used as an escape character is not included in the string's total length.
# The code in Example 3, therefore 0outputs 3.

i_am = 'I\'m'
print(len(i_am))

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
#The asterisk makes the string be replicated as many times as the number it is multiplied with
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function.

char_1 = 'Ð'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function.

print(chr(197))
print(chr(205))

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])"""
