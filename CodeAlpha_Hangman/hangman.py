"""
CodeAlpha Internship - Task 1: Hangman Game
"""

import random

# A small list of predefined words to guess from
WORD_LIST = ["python", "hangman", "internship", "coding", "keyboard"]

MAX_WRONG_GUESSES = 6


def choose_word():
    """Pick a random word from the list."""
    return random.choice(WORD_LIST)


def display_progress(word, guessed_letters):
    """Show the word with unguessed letters as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses used: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        # Check win condition: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    # If loop ends without returning, player has run out of guesses
    print(f"You lost! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
