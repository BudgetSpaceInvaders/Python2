def palchecker(word):
    revword = word[::-1]
    if word == revword:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


word = input("Please write a palindrome: ")
word = word.replace(" ", "")
word = word.lower()
palchecker(word)
