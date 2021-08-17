import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet_dict = {row["letter"]:row["code"] for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Type your word: ").upper()
nato_word = [nato_alphabet_dict[letters] for letters in user_word]
print(nato_word)

