# Created By Jarod L Cunningham
# This is a Game of Hangman where the users plays against the computer.
import random
HANGMAN_PICS= ['''
               +---+
                   |
                   |
                   |
                  ===''','''
               +---+
               O   |
                   |
                   |
                  ===''', '''
               +---+
               O   |
               |   |
                   |
                  ===''', '''
               +---+
               O   |
              /|   |
                   |
                  ===''', '''
               +---+
               O   |
              /|\  |
                   |
                  ===''', '''
               +---+
               O   |
              /|\  |
              /    |
                  ===''', '''
               +---+
               O   |
              /|\  |
              / \  |
                  ===''']
words = ' ant baboon badger bat beer beaver camel cat clam cobra couger coyotw crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole mokey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skcunk sloth snake spider stork swam tiger toad trout turkey turtle weasel whale wombat zebra'. split()

def getRandomWord(wordList):
    ### This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secret):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter.
            print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function makes sure the plaer entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess= input()
        guess=guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess
        
def playagain():
    # This function retunrs True if the player wants to play again, otherwise it returns Fasle.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if player has won
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foudAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The Secret word is "' + secretWord + '"! You Have Won!')
            gameIsDone=True
    else: 
        missedLetters = missedLetters + guess

    #check if player has guessed to many times and lost.
    if len(missedLetters) == len(HANGMAN_PICS) -1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\n After' + str(len(missedLetters)) +' missed guesses and '+ str(len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
        gameIsDone = True

        #Ask the player if they want to play again(but only if the game is done).
        if gameIsDone:
            if playagain():
                missedLetters =''
                correctLetters = ''
                gameIsDone =False
                secretWord =getRandomWord(words)
            else:
                break
# Created By Jarod L Cunningham
# This is a Game of Hangman where the users plays against the computer.