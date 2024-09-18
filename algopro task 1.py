import random

def guess_number():
    lowest_number = 1
    highest_number = 100
    secret_number = random.randint(lowest_number, highest_number)
    attempts = 0

    print("Please guess a number between 1 and 100!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("That's too low!")
        elif guess > secret_number:
            print("That's too high!")
        else:
            print(f"Yay! You did it!")

guess_number()

