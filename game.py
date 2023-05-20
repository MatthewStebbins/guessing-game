import random
from random import randint

"""A number-guessing game."""

# Put your code here
def input_validation(text):
    while not text.isdigit():
        text = input("Invaild input! Please enter a number between 1 - 100:")
    return text

done = False
while not done:
    best_score = 1000
    guesses_left = 20
    name = str(input("Howdy, what's your name?"))
    print(f"{name}, I'm thinking of a number between 1 and 100.")

    print("Try to guess my number.")

    your_guess = int(input_validation(input("Your guess?")))

    my_number = randint(1, 100)

    counter = 1
    guesses_left -= 1

    while your_guess != my_number:
        if guesses_left > 0: 
            if your_guess < my_number:
                print("Your guess is too low, try again.")
                counter += 1
                guesses_left -= 1
                your_guess = int(input_validation(input("Your guess? ")))

            elif your_guess > my_number:
                print("Your guess is too high, try again.")
                counter += 1
                guesses_left -= 1
                your_guess = int(input_validation(input("Your guess? ")))

            else:
                break
        else:
            break
    
    if guesses_left == 0:
        print("Too many tries!")
    else:
        print(f"Well done, {name}! \nYou found my number in {counter} tries! \nThe game still had {guesses_left} tries available!")

    if counter < best_score:
        best_score = counter

    new_game = input("Would you like to play again? Y or N ")

    new_game = new_game[0].capitalize()

    if new_game == "N":
        print(f"Your best score was {best_score} tries")    
        done = True
    else:
        done = False