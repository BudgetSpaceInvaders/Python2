def ubbi_dubbi(word):
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    if word.lower()[0] in vowels:
        word += "way"
    else:
        word = word[1:] + word[0] + "ay"
    return word


sentence = "Pig Latin is a strange and abnormal language!"

last = sentence[-1]
if last == "!" or last == "." or last == "?":
    sentence = sentence[:-1]
list1 = sentence.split()
translated_words = [pig_latin(word) for word in list1]
sentence = ' '.join(translated_words).capitalize() + last
print(sentence)
