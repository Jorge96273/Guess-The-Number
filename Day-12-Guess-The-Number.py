import random
from two import logo

num_of_trys = 0
RANDOM_NUM = random.choice(range(2, 100))
print("Welcome to the Random Number Guessing Game :)")
print("You are going to have to guess a number between 1-100")
mode = input("Which difficulty would you like? \neasy = 5 guesses and hard = 10 guesses \ntype \"easy\" or \"hard\"\n").lower()

if mode == "easy":
  num_of_trys = 10
elif mode == "hard":
  num_of_trys = 5

def guesses(trys):
  global RANDOM_NUM
  while trys > 0:
    guess = int(input("What number would you like to guess?\n"))
    if RANDOM_NUM > guess:
      trys -= 1
      print("Sorry, your guess is too LOW!")
      print(f"You have {trys} attempts left")
    elif RANDOM_NUM == guess:
      print("CONGRATS, you guessed RIGHT!")
      trys = 0
    elif RANDOM_NUM < guess:
      trys -= 1
      print("Sorry, your guess is too HIGH!")
      print(f"You have {trys} attempts left")
    if trys == 0:
      print("OH NO, you ran out of guesses!")


guesses(trys = num_of_trys)