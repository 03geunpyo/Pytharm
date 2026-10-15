import random

words = ["hangman", "python", "computer", "program", "developer"]

while True:
    secret_word = random.choice(words)
    guessed = ["_"] * len(secret_word)
    trials = 6

    print(" ".join(guessed))

    while trials > 0 and "_" in guessed:
        guess = input("글자 입력: ").lower()

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed[i] = guess
            print(" ".join(guessed))
        else:
            trials -= 1
            print(f"Nope! {trials} trials left")
            print(" ".join(guessed))

    if "_" not in guessed:
        print("Good Job!")
    else:
        print("Fail!")

    play_again = input("게임을 계속하시겠습니까? (y/n): ").lower()
    if play_again != 'y':
        break