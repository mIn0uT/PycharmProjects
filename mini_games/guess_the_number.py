import random  # imported class must be used or ele error will show


def guess(x):
    random_number = random.randint(1, x)  # get a random number
    guess = 0  # get the user number guess
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {random_number} corretly!")


""" Computer guesses a random number from range
you'll tell if its to low or high or correct
Computer randomly guess number until you pressed C"""


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f"Is {guess} too high (H), too loq (L), or correct (C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")


computer_guess(15)
