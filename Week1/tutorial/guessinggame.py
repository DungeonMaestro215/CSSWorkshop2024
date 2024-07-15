# Guessing game
from random import randint

# Think of a secret number
secret_number = randint(50, 100)

done = False
while (not done):
    # Have the user guess the number
    guess = int(input("Guess a number: "))

    # Check if the guess is right
    if (guess == secret_number):
        # If the guess is right, then say congrats
        print("Congrats!")
        done = True
    else:
        if (guess > secret_number):
            print("Guess lower")
        else:
            print("Guess higher")
