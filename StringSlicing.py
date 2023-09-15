# Task 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = numbers[3:6]
print(new)
# Task 2
message = "Hello, Python!"
news = message[::-1]
print(news)
# Task 3
sentence = "I love programming in Python"
newly = sentence[7:18]
print(newly)
# Task 4
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newspaper = numbers1[::2]
print(newspaper)
# Task 5
colors = ["red", "green", "blue", "yellow", "orange"]
colorful = colors[-3:]
print(colorful)
# Task 6
text = "I like cats and dogs"
coords = text.find("cats")
ltext = text[:coords]
rtext = text[-9:]
ltext += "rabbits"
newtext = ltext + rtext
print(newtext)
# Task 7
word = "abcdefghij"
neword = word[::2]
print(neword)
# Task 8
word = "character"
new_word = ""
if len(word) % 2 == 1:
    new_word = word[(len(word) // 2) - 1:(len(word) // 2) + 2]
    print(new_word)
else:
    new_word = word[(len(word) // 2) - 2:(len(word) // 2) + 1]
    print(new_word)
# Task 9
email = "john.doe@example.com"
coords2 = email.find("@")
domain = email[coords2 + 1:]
print(domain)


# Task 10
def remove_prefix_suffix(input_string, prefix_length, suffix_length):
    if len(input_string) < prefix_length + suffix_length:
        return input_string
    return input_string[prefix_length:-suffix_length]


# Example usage:
text = "###Hello, Python###"
modified_text = remove_prefix_suffix(text, 3, 3)
print(modified_text)
