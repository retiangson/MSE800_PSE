import random

listOfWords = ["ronald", "laptop", "computer", "programming", "developer", "keyboard", "nothing"]
word = ""
blanks = []
lives = 6
guessed_letters = []

class InitConfiguration:
    @staticmethod
    def generate_random_word():
        return random.choice(listOfWords)

    @staticmethod
    def generate_blanks(selected_word):
        return ["_"] * len(selected_word)

class WordGuessingGame:
    @staticmethod
    def wordGuessing():
        global word, blanks, lives, guessed_letters
        lives = 6
        guessed_letters = []
        
        word = InitConfiguration.generate_random_word()
        blanks = InitConfiguration.generate_blanks(word)

        print("Word guessing!")
        WordGuessingGame.display_word()

    @staticmethod
    def display_word():
        print(" ".join(blanks))

    @staticmethod
    def ask_for_guess():
        guess = input("Guess a letter: ").lower().strip()[:1] 
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            return WordGuessingGame.ask_for_guess()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            return WordGuessingGame.ask_for_guess()
        guessed_letters.append(guess)
        return guess

    @staticmethod
    def update_word_with_guess(guess):
        for i, letter in enumerate(word):
            if letter == guess:
                blanks[i] = guess

    @staticmethod
    def check_all_blanks_filled():
        return "_" not in blanks

    @staticmethod
    def lose_life():
        global lives
        lives -= 1

    @staticmethod
    def start_WordGuessing():
        WordGuessingGame.wordGuessing()
        while True:
            guess = WordGuessingGame.ask_for_guess()
            if guess in word:
                WordGuessingGame.update_word_with_guess(guess)
                print("Correct!")
            else:
                WordGuessingGame.lose_life()
                print(f"Wrong! Life left: {lives}")

            WordGuessingGame.display_word()

            if WordGuessingGame.check_all_blanks_filled():
                print("You win!")
                break
            elif lives == 0:
                print(f"Game over! The word was '{word}'.")
                break

if __name__ == "__main__":
    WordGuessingGame.start_WordGuessing()