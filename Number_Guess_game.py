from art import logo
print(logo)
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """guess is guessed number, answer is actual answer, turns remaining attempts"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns  
        
#make a function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#Choosing a random number between 1 to 100
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)
turns = set_difficulty()
guess = 0

while guess != answer:
    guess = int(input("Enter the guessed number: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses. You lose.")
        break
    print(f"You have {turns} guesses left")
