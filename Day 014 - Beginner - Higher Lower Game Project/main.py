from art import logo, vs
from game_data import data
import random
from replit import clear

DATA_A = []
DATA_B = []
ALREADY_PICKED_DATA = []
SCORE = 0
GAME_END = False
#TODO Create a function to pick one item in game_data at random
#TODO AVOID TO take the same data as previously
#todo if all number are used, end of the game
def pick_random_data():
    random_number = random.randint(0, 49)
    while random_number in ALREADY_PICKED_DATA:
        random_number = random.randint(0, 49)
    random_data = data[random_number]
    ALREADY_PICKED_DATA.append(random_number)
    return random_data


#TODO Create a function to compare a specific two items and return the higher one
def compare_data(data_a, data_b):
    result = ""
    if data_a["follower_count"] > data_b["follower_count"]:
        result = "a"
    else:
        result = "b"
    return result
    

DATA_A = pick_random_data()
DATA_B = pick_random_data()

while not GAME_END:
    print(logo)
    print(f"Compare A: {DATA_A['name']}, a {DATA_A['description']}, from {DATA_A['country']}")
    print(vs)
    print(f"Against B: {DATA_B['name']}, a {DATA_B['description']}, from {DATA_B['country']}")

    PLAYER_GUESS = input("Who has more followers? Type 'A' or 'B': ").lower()

    if len(ALREADY_PICKED_DATA) == 50:
        SCORE += 1
        clear()
        print(f"You bet the game! With a score of {SCORE}!")
        GAME_END = True
    elif compare_data(DATA_A, DATA_B) == PLAYER_GUESS:
        SCORE += 1
        clear()
        print(f"You're right! Current score: {SCORE}!")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {SCORE}!")
        GAME_END = True

    print(f"Data A: {DATA_A['follower_count']}, Data b: {DATA_B['follower_count']},")

    if compare_data(DATA_A, DATA_B) == "b":
        DATA_A = DATA_B
    
    DATA_B = pick_random_data()

"""
print(len(data))
print(data[0])
print(data[0]["name"])
print(data[0]["follower_count"])
print(data[0]["description"])
print(data[0]["country"])
"""



