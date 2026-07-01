import random

# list iof words
words = ["python", "computer", "program", "developer","internship"]

# select a random word
word = random.choice(words)

# create a list of underscores
guessed_word = ["_"] * len(word)

# number of attempts
attempts = 6

# stored guessed letters
guessed_letter = []

print("====== Welcome to Hangman Game =====")

while attempts > 0 and "_" in guessed_word:
    print("\nword:"," ".join(guessed_word))
    print("Attempts Left:", attempts)

    guess = input("Enter a Letter: ").lower()

    # validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue
    # check repeated guess
    if guess in guessed_letter:
        print("You already guessed that letter.")
        continue
    guessed_letter.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        attempts -= 1

# final result
if "_" not in guessed_word:
    print("\n Congratulations!")
    print("You Guessed the word:", word)
else:
    print("\n Game over!")
    print("The correct word was:", word)
