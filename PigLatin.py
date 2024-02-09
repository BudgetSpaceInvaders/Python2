def pig_latin(word):
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    if word.lower()[0] in vowels:
        word += "way"
    else:
        word = word[1:] + word[0] + "ay"
    word = word.capitalize()
    return word


print(pig_latin("Highway"))
