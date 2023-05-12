import random
from random import randint

"""A number-guessing game."""

# Put your code here
name = str(input("Howdy, what's your name?"))
print(f"{name}, I'm thinking of a number between 1 and 100.")

print("Try to guess my number.")

your_guess = int(input("Your guess?"))

my_number = randint(1, 100)

counter = 1

while your_guess != my_number:
    if your_guess < my_number:
        print("Your guess is too low, try again.")
        counter += 1
        your_guess = int(input("Your guess? "))

    elif your_guess > my_number:
        print("Your guess is too high, try again.")
        counter += 1
        your_guess = int(input("Your guess? "))

    else:
        break
    
print(f"Well done, {name}! You found my number in {counter} tries!")
