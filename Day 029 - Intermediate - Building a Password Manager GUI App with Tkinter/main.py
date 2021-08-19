import tkinter
from tkinter import messagebox
import random
import pyperclip

CLEAR_BG = "#DDDDDD"
DARK_BLUE = "#222831"
BLUE = "#30475E"
RED = "#F05454"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, tkinter.END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning - Empty fields", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"The are the details entered:"
                                                          f"\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        entry_website.delete(0, tkinter.END)
        entry_password.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
windows =  tkinter.Tk()
windows.title("Password Manager")
windows.config(padx=30, pady=30)


logo_img = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)

label_website = tkinter.Label(text="Website:", fg=BLUE)
label_email = tkinter.Label(text="Email/Username:")
label_password= tkinter.Label(text="Password:")

entry_website = tkinter.Entry(width=35)
entry_website.focus()
entry_email = tkinter.Entry(width=35)
entry_email.insert(0, "myemail@email.com")
entry_password = tkinter.Entry(width=24, justify="left", highlightthickness=0)

button_generate_password = tkinter.Button(text="Generate Password", font=("", 6, ""), justify="center",
                                          highlightthickness=0, width =11, command=generate_password)
button_add= tkinter.Button(text="Add", width=33, command=save)

canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
label_email.grid(column=0, row=2)
label_password.grid(column=0, row=3)
entry_website.grid(column=1, row=1, columnspan=2)
entry_email.grid(column=1, row=2, columnspan=2)
entry_password.grid(column=1, row=3)
button_generate_password.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)

windows.mainloop()
