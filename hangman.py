import random

# List of 5 predefined words
words = ["apple", "tiger", "python", "school", "mobile"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the complete word is guessed
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get a letter from the user
    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)