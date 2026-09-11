import random

words = ["python" , "machine" , "learning" , "data" , "science"]

secret_word = random.choice(words) # select a random word

guessed_letters = [] # keep track of guessed letters
chance = 6 # number of chances that is 6

print("Welcome to the Secret Word Guessing Game!")

while chance > 0:

    display_word = ""

 # display the hidden word
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n Word:", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulation! You guess the word: " , secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)


    if guess in secret_word:
        print("Correct!")
    else:
        chance -= 1
        print("Wrong guess! chances left: " , chance)

    if chance == 0:
        print("\nGame Over!")
        print("The Word was: ", secret_word)