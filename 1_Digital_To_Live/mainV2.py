import random


def prompt_for_number():
    guess = int(input("Please enter your guess: "))
    return guess

def switch(count):
    if count == 1:
        return "Was that genius or just a fluke?"
    elif 1 < count <= 3:
        return "Well done, you are a great guesser!"
    elif 3 < count <= 6:
        return "Good job, you are a solid guesser"
    else:
        return "That was pretty poor guessing, it has to be said!"


number = random.randint(1, 100)
file = r"C:\labs\HighLowGameHallOfTheChampions.txt"
guess = prompt_for_number()
guesses = [guess]
count = 1
while guess != number:
    count += 1
    if guess > number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = prompt_for_number()
    guesses.append(guess)

print(f"You've guessed right! The number was {number}")

pluralise = "es"
if count == 1:
    pluralise = ""
    name = input("You've done so well we are going to add your name to the Hall of Champions.Please enter your name: ")
    with open(file, mode="a") as fh_out:
        fh_out.write(f"\n{name}")

print(f"It took you {count} guess{pluralise}! {switch(count)}")
print(f"Here's a list of your guesses: {guesses}")

print("A list of past and present CHAMPIONS:")
with open(file, mode="rt") as fh_in:
    for name in fh_in.readlines():
        print(name, end="")