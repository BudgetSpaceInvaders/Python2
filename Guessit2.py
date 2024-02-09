def get_secret_word(difficulty):
    words = {
        "easy": "cat",
        "medium": "sheep",
        "hard": "hippopotamus",
        "secret": "titanium",
        "extreme": "antidisestablishmentarianism"
    }
    return words.get(difficulty.lower(), "cat")


def display_guessed_letters(secret_word, guessed_letters):
    display = [leter if leter in guessed_letters else "_" for leter in secret_word]
    print(" ".join(display))


def main():
    chosen_word = input("Choose a difficulty (easy, medium, hard, secret, extreme): ")
    secret_word = get_secret_word(chosen_word)
    guessed_letters = []
    nr_trials = len(secret_word) + 5
    print(f"The word is {len(secret_word)} letters long. You have {nr_trials} trials.")

    while nr_trials > 0:
        guess_letter = input("Guess a letter: ").lower()

        if guess_letter in secret_word:
            print("The letter is in the word!")
            guessed_letters.append(guess_letter)
        else:
            print("The letter is not in the word.")
        display_guessed_letters(secret_word, guessed_letters)
        nr_trials -= 1
        print(f"You have {nr_trials} trials left.")
        result_string = ''.join(guessed_letters)
        if result_string == secret_word:
            print("You guessed the word! You win!")
            break
    else:
        guessed_word = input("What is the word? ").lower()
        if guessed_word == secret_word:
            print("You guessed the word! You win!")
        else:
            print(f"You didn't guess the word. The word was {secret_word}.")
            print("Game over.")


if __name__ == "__main__":
    main()