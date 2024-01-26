secret_word_easy = "car"
secret_word_easy = secret_word_easy.lower()
secret_word_medium = "sheep"
secret_word_medium = secret_word_medium.lower()
secret_word_hard = "radioactive"
secret_word_hard = secret_word_hard.lower()
chosen_word = input("Please choose the difficulty: Easy, Medium or Hard: ")
chosen_word = chosen_word.lower()
if chosen_word == "easy":
    secret_word = secret_word_easy
if chosen_word == "medium":
    secret_word = secret_word_medium
if chosen_word == "hard":
    secret_word = secret_word_hard
if chosen_word == "secret":
    secret_word = "titanium"
guessed_word = ""
secret_list = list(secret_word)
nr_tries_2 = 3
nr_tries = len(secret_word) + 5
guessed_letters = []
print("The word is", len(secret_word), "letters long!")
while nr_tries != 0:
    guess_letter = input("Please type a letter: ")
    if guess_letter in secret_word:
        print("The guessed letter is in the word.")
        guessed_letters.append(guess_letter)
    else:
        print("The guessed letter is NOT in the word.")
    nr_tries -= 1
    print("THERE ARE", nr_tries, "TRIES LEFT!")
else:
    for x in secret_list:
        nr_rep = secret_list.count(x)
        if nr_rep >= 2:
            nr_rep -= 1
            for y in range(nr_rep):
                guessed_letters.append(x)

    guessed_letters.sort()
    print(guessed_letters)
    guessed_word = input("PLEASE TYPE THE WORD: ")
    guessed_word = guessed_word.lower()
    nr_tries_2 -= 1
    if guessed_word == secret_word and nr_tries_2 != 0:
        print("You won!")
    else:
        print("You lost!")
