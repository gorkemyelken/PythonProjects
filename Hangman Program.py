
#NAME: Görkem
#SURNAME: Yelken


from random import randint
import string

# Welcome
print("Welcome to the game Hangman!")

# Get all English alphabet lowercase letters to a list variable
remaining_letters = list(string.ascii_lowercase)

# Given wordlist
wordlist = ["algorithm", "cloud", "computer", "cookie", "device", "download", "driver", "ethernet", "freeware", "gateway", "graphic", "hardware", "keyboard", "keyword",
            "laptop", "megabyte", "memory", "monitor", "network", "password", "screenshot", "software", "toolbaar", "upload", "website"]

# Initializing guess variable
guess = ''

# Function is_word_guessed() : Returns true if user successfully guesses all letters, otherwise returns false


def is_word_guessed(secretWord, letterGuessed):
    # Convert list to set to get rid of dublicate letters
    secretWord = set(secretWord)
    result = all(elem in letterGuessed for elem in secretWord)
    return True if result is True else False

# Function get_guessed_word() : Returns the current result of the game


def get_guessed_word(secretWord, lettersGuessed):
    global check
    global remainingGuess
    secretWord = list(secretWord)
    currentResult = list()
    # Creating the visualization of result. If
    for i in secretWord:
        if i in lettersGuessed:
            currentResult.append(' ')
            currentResult.append(i)
            currentResult.append(' ')
        else:
            currentResult.append(' _ ')
    print(''.join(currentResult))
    # If user guesses all the letters then wons the game
    if is_word_guessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        check = False
    elif remainingGuess == 0:
        gameLost()

# Function get_available_letters() : Returns all remaining unused letters


def get_available_letters(lettersGuessed):
    # Remove the guessed letter from remaining letters list and return the list
    for i in lettersGuessed:
        if i in remaining_letters:
            remaining_letters.remove(i)
    return remaining_letters

# Function printALL() : Prints general information in each evaluation


def printAll(remaining, guessedLetters):
    if remaining == 1:
        print("You have", remaining, "guess left.")
    else:
        print("You have", remaining, "guesses left.")
    print("Available letters:", get_available_letters(guessedLetters))
    print("\n*********************************************************************")

# Function getInput(): Gets an input from user checks if input...


def getInput(user_guess):
    while True:
        user_guess = input("\nPlease guess a letter:")
        if user_guess == '':
            print("Please enter a letter! Again:")
            continue
        else:
            return user_guess[0].lower()

# Function evaluate(): Evaluates the guess of the player.


def evaluate(guess):
    global remainingGuess
    if guess in letters_guessed:
        print("Oops! You've already guessed that letter.")
        print("\n*********************************************************************")
        guess = getInput(guess)
        evaluate(guess)
    elif guess in secret_word:
        remainingGuess = remainingGuess - 1
        letters_guessed.append(guess)
        print("Good guess: ", end='')
        get_guessed_word(secret_word, letters_guessed)
    elif guess not in secret_word:
        print("Bad guess, try again.")
        remainingGuess = remainingGuess - 1
        letters_guessed.append(guess)
        if remainingGuess == 0:
            gameLost()

# Function gameLost(): This function finishes the game when remaining number of guess is 0


def gameLost():
    global check
    if remainingGuess == 0:
        check = False
        print("You lose!")


print("\n-------------------- Starting the HANGMAN game! ---------------------\n")

secret_word = wordlist[randint(0, len(wordlist)-1)]
remainingGuess = len(secret_word) + 5
print("I am thinking of a word that is", len(secret_word), "letters long.")

# Create empty list to store player's guesses
letters_guessed = list()

# Information about selected word
printAll(remainingGuess, letters_guessed)

# Variable which controls the running of the game loop
check = True

# The game loop
while check:
    guess = getInput(guess)
    print("Guess is:", guess)
    evaluate(guess)
    printAll(remainingGuess, letters_guessed)
