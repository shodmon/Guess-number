import random

def guess():
    randomNumber = random.randint(1,100)
    guessedNumber = 0
    numberOfTries = 0
    print ("Welcome to the game 'Guess the number'!\nGuess number between 1 and 100")
    while randomNumber != guessedNumber:
        numberOfTries+=1
        guessedNumber = int(input(""))
        if randomNumber > guessedNumber:
            print("Too low.")
        elif randomNumber < guessedNumber:
            print("Too high.")
    print(f"Congratulations, you found the right number in {numberOfTries} tries!")

guess()