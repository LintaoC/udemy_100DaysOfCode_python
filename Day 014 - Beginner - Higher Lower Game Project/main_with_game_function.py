from art import logo, vs
from game_data import data
import random
from replit import clear

DATA_A = []
DATA_B = []
ALREADY_PICKED_DATA = []
SCORE = 0

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
    
def game():
    l_data_a = pick_random_data()
    l_data_b = pick_random_data()
    score = 0

    while True:
        print(f"Already picked datas, {ALREADY_PICKED_DATA}")
        print(f"Already picked datas len, {len(ALREADY_PICKED_DATA)}")

        print(logo)
        print(f"Compare A: {l_data_a['name']}, a {l_data_a['description']}, from {l_data_a['country']}")
        print(vs)
        print(f"Against B: {l_data_b['name']}, a {l_data_b['description']}, from {l_data_b['country']}")

        PLAYER_GUESS = input("Who has more followers? Type 'A' or 'B': ").lower()

        if len(ALREADY_PICKED_DATA) == 50:
            score += 1
            clear()
            print(f"You bet the game! With a score of {score}!")
            return
        elif compare_data(l_data_a, l_data_b) == PLAYER_GUESS:
            score += 1
            clear()
            print(f"You're right! Current score: {score}!")
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}!")
            return

        print(f"Data A: {l_data_a['follower_count']}, Data b: {l_data_b['follower_count']},")

        if compare_data(l_data_a, l_data_b) == "b":
            print("B < A")
            l_data_a = l_data_b
        
        l_data_b = pick_random_data()

game()
"""
print(len(data))
print(data[0])
print(data[0]["name"])
print(data[0]["follower_count"])
print(data[0]["description"])
print(data[0]["country"])
"""



