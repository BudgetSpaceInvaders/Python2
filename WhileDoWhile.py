"""secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7:
        break"""



n = 3972345678
x = 0
while True:
    if n // 10 < 1:
        x += 1
        fin = x
        print(fin)
        break
    else:
        n = n // 10
        x += 1
