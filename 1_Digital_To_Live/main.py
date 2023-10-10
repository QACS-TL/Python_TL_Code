import random


def prompt_for_number():
    guess = int(input("Please enter your guess "))
    return guess


number = random.randint(1, 100)
guess = prompt_for_number()
count = 1
while guess != number:
    count += 1
    if guess > number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = prompt_for_number()

print(f"You've guessed right! The number was {number}")
print(f"It only took you {count} guesses!")