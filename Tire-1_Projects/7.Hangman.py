import random

# List of words for the game
WORDS = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]

# Function to choose a random word
def choose_word():
    return random.choice(WORDS)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to draw the hangman
def draw_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[attempts]

# Main game function
def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + draw_hangman(6 - attempts))
        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

    if attempts == 0:
        print("\n" + draw_hangman(6))
        print("You lost! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()