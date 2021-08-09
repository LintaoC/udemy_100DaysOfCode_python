from replit import clear
from art import logo

#Dictionary for bidders key = Names ; Value = Value
bidders = {}
is_other_bid = ""

def add_bidders(names, value):
    bidders[names] = value

print(logo)

while is_other_bid != "no":
    name_input = input("What is your name?: ")
    value_input = int(input("What is your bid?: $"))
    add_bidders(names = name_input, value= value_input)

    is_other_bid = input("Are there any other bidders? Type 'yes or 'no'. ").lower()

    if is_other_bid == "yes":
        clear()

#Check who is the winner
winner = ""
is_are = "is"
highest_bid = 0
for key in bidders:
    if bidders[key] > highest_bid:
        winner = key
        highest_bid = bidders[key]
    elif bidders[key] == highest_bid:
        winner += "; " + key
        highest_bid = bidders[key]
        is_are = "are"

print(f"The winner {is_are} {winner} , with a bid of ${highest_bid}")
#HINT: You can call clear() to clear the output in the console.