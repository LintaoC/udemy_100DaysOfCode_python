import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
windows = tkinter.Tk()
windows.title("Pomodoro")
windows.config(padx=50, pady=25, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))

label_timer = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
label_checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))

button_start = tkinter.Button(text="Start", fg=PINK, bg=YELLOW, justify="center",
                              highlightthickness=0, font=(FONT_NAME, 18, "bold"), command=start_timer)
button_reset = tkinter.Button(text="Reset", fg=PINK, bg=YELLOW, justify="center",
                              highlightthickness=0, font=(FONT_NAME, 18, "bold"), command=reset_timer)

label_timer.grid(column=1, row=0)
label_checkmark.grid(column=1, row=3)
button_start.grid(column=0, row=2)
button_reset.grid(column=2, row=2)
canvas.grid(column=1, row=1)

windows.mainloop()
