import random

WORDS = ["Ronald", "laptop", "computer", "programming", "developer", "keyboard", "nothing"]
word = ""
blanks = []
lives = 6
guessed_letters = []

def wordGuessing():
    global word, blanks, lives, guessed_letters
    word = random.choice(WORDS)
    blanks = ["_"] * len(word)
    lives = 6
    guessed_letters = []
    print("Word guessing!")
    display_word()

def display_word():
    print(" ".join(blanks))

def ask_for_guess():
    guess = input("Guess a letter: ").lower().strip()[:1] 
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        return ask_for_guess()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return ask_for_guess()
    guessed_letters.append(guess)
    return guess


def update_word_with_guess(guess):
    for i, letter in enumerate(word):
        if letter == guess:
            blanks[i] = guess

def check_all_blanks_filled():
    return "_" not in blanks

def lose_life():
    global lives
    lives -= 1

def run_WordGuessing():
    wordGuessing()
    while True:
        guess = ask_for_guess()
        if guess in word:
            update_word_with_guess(guess)
            print("Correct!")
        else:
            lose_life()
            print(f"Wrong! Life left: {lives}")

        display_word()

        if check_all_blanks_filled():
            print("You win!")
            break
        elif lives == 0:
            print(f"Game over! The word was '{word}'.")
            break

if __name__ == "__main__":
    run_WordGuessing()