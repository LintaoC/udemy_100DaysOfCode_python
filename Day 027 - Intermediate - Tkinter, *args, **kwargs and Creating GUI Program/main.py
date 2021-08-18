import tkinter

def button_click():
    input_str = input.get()
    my_label.config(text=input_str)
    print("I got clicked")

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))

# 2 ways of updating a label
my_label["text"] = "New text"
my_label.config(text="New Text")

# Button
button = tkinter.Button(text="Click Me", command=button_click)
button_2 = tkinter.Button(text="Button 2", command=button_click)
# Entry
input = tkinter.Entry(width=10)

my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
button_2.grid(column=3, row=0)
input.grid(column=4, row=4)
# my_label.place(x=100, y=0)
# my_label.pack()
# button.pack()
# input.pack()

window.mainloop()
