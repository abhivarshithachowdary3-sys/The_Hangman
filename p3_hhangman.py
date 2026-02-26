import random

# Hangman stages
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

words = ["python", "hangman", "computer", "programming", "developer"]

computers_word = random.choice(words)

word_display = ["_"] * len(computers_word)
letters_guessed = set()
wrong_guesses = 0
max_wrong = 6
game_won = False

print("="*40)
print("       WELCOME TO HANGMAN!")
print("="*40)
print("Guess the word one letter at a time.")
print(f"You have {max_wrong} wrong guesses allowed.")
print()
print("Word to guess:")
print(" ".join(word_display))
print()

while wrong_guesses < max_wrong and not game_won:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("You can enter only one guess at a time and it should be an alphabet")
        continue

    if guess in letters_guessed:
        print("Already Guessed")
        continue

    letters_guessed.add(guess)

    if guess in computers_word:
        for i in range(len(computers_word)):
            if computers_word[i] == guess:
                word_display[i] = guess
        print("Correct!")      

        if "_" not in word_display:
            game_won = True  

    else:
        wrong_guesses += 1
        print(f"Wrong! You have only {max_wrong - wrong_guesses} guesses left.")

    print("".join(word_display))
    print(f"Guessed Letters: {sorted(letters_guessed)}")
    print(HANGMAN_STAGES[wrong_guesses])
    print()

# AFTER the while loop (same indentation as 'while')
if game_won:
    print(f"🎉 You won! The word was: {computers_word}")
else:
    print(f"💀 Game Over! The word was: {computers_word}")