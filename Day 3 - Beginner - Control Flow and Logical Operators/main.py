print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input("You just arrived to the island, where do you want to go? Type 'left' or 'right'\n").lower()

if choice == "left":
  choice = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
  if choice == "wait":
    choice = input("The boat bring you to the island. There is an house with 3 doorrs. On red, one yellow, one blue. Which color do you choose? Type 'red', 'yellow' or 'blue'\n").lower()
    if choice == "yellow":
      print("Congratz!!! You win")
    elif choice == "red":
      print("The room is on fire, you get burned. Game over")
    elif choice == "blue":
      print("The room is full of angry kitten, you get eaten by them! (cute) Game over")
    else:
      print("Game over")
  else:
    print("You get attacked by a shark. Game Over")
else:
  print("Arg, you fall into a hole! Game Over")

