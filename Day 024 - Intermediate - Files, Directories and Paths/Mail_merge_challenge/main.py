# ##
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open and get the name list, put the name into a list with readlines()
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()

# Open the letter template and save it into a string
with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()
    for name in names_list:
        # For each name in the list, replace [name] of the letter template by the name listed
        name = name.strip()  # Stip the name to remove the backspace
        letter_final = letter_template
        letter_final = letter_final.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}_letter.txt", mode="w") as letter_finalized:
            # Finally write an new file with the letter finalized
            letter_finalized.write(letter_final)
