import random
from art import logo

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

RANDOM_NUMBER = random.randint(1, 100)
print(f"Pssst, the correct answer is {RANDOM_NUMBER}")

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
    NBR_OF_GUESS = 10
else:
    NBR_OF_GUESS = 5

END_OF_THE_GAME = False


def check_user_guess(guess):
    user_won = False
    if guess == RANDOM_NUMBER:
        print(f"You got it! The answer was {RANDOM_NUMBER}.")
        user_won = True
    elif guess > RANDOM_NUMBER:
        print("Too high\nGuess again")
    elif guess < RANDOM_NUMBER:
        print("Too low\nGuess again")
    return user_won


while not END_OF_THE_GAME:
    user_guess = int(input(f"""You have {NBR_OF_GUESS} attempts remaining to guess the number.
Make a guess:"""))
    if check_user_guess(user_guess) or NBR_OF_GUESS == 1:
        END_OF_THE_GAME = True
    else:
        NBR_OF_GUESS -= 1

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
