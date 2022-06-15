from random import randint

def guess(x):
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Too low, try again: ")
        elif guess > random_number:
            print("Too high, try again: ")
    print(f"You guessed it, is {random_number}")

guess(100)
