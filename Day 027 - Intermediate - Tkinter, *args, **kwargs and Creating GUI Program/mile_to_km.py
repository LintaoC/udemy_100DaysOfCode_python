import tkinter


def calculate():
    miles = float(input_miles.get())
    km = miles * 1.609
    label_result.config(text=f"{round(km, 1)}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Label
label_is_equal_to = tkinter.Label(text="is equal to", font=("Ariel", 12, ""))
label_miles = tkinter.Label(text="Miles", font=("Ariel", 12, ""))
label_km = tkinter.Label(text="Km", font=("Ariel", 12, ""))
label_result = tkinter.Label(text="0", font=("Ariel", 12, ""))

# Button
button_calculate = tkinter.Button(text="Calculate", command=calculate)

# Entry
input_miles = tkinter.Entry(width=10, justify="center")

label_is_equal_to.grid(column=0, row=1)
label_miles.grid(column=2, row=0)
label_km.grid(column=2, row=1)
label_result.grid(column=1, row=1)
button_calculate.grid(column=1, row=2)
input_miles.grid(column=1, row=0)

window.mainloop()
