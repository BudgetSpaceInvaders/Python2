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
guessed_word = ""
nr_tries = 5
while nr_tries != 0:
    guess_letter = input("Please type a letter: ")
    if guess_letter in secret_word:
        print("The guessed letter is in the word.")
    else:
        print("The guessed letter is NOT in the word.")
    nr_tries -= 1
else:
    guessed_word = input("PLEASE TYPE THE WORD: ")
    guessed_word = guessed_word.lower()
    if guessed_word == secret_word:
        print("You won!")
    else:
        print("You lost!")
