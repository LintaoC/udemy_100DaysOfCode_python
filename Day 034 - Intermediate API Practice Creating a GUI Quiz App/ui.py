import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            fill=THEME_COLOR,
            text="Question",
            font=("Arial", 20, "italic"),
            width=280
        )

        self.label_score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")

        button_true_img = tkinter.PhotoImage(file="images/true.png")
        button_false_img = tkinter.PhotoImage(file="images/false.png")
        self.button_true = tkinter.Button(text="True", image=button_true_img, highlightthickness=0, command=self.right)
        self.button_false = tkinter.Button(text="False", image=button_false_img, highlightthickness=0, command=self.wrong)

        self.label_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.button_true.grid(row=2, column=1)
        self.button_false.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quizz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, self.get_next_question)
