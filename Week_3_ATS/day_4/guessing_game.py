import pyinputplus as pyip
import random

guessed = random.randint(0, 9)
print(guessed)
user_guess = pyip.inputNum(prompt="Guess a number between 0-9: ")
for i in range(5):
    if user_guess == guessed:
        print("Guess correct!")
        break
    if user_guess < guessed:
        user_guess = pyip.inputNum(prompt="Guess lesser than number. Try again: ")
        continue
    user_guess = pyip.inputNum("Guess greater than number. Try again: ")
    
