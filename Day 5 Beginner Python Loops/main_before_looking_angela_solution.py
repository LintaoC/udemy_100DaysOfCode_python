#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_not_random = ""

for number_letters in range(nr_letters):
  password_not_random += letters[random.randint(0,25)]
for number_symbols in range(nr_symbols):
  password_not_random += symbols[random.randint(0,8)]
for number_numbers in range(nr_numbers):
  password_not_random += numbers[random.randint(0,9)]

print(password_not_random)

password_random = ""
randomized_character = ""

for number_numbers in range(len(password_not_random)):
  randomized_character = random.choice(password_not_random)
  password_random += randomized_character
  password_not_random = password_not_random.replace(randomized_character,"",1)

print(f"Your password is: {password_random}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P




