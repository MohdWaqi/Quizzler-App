from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 120, width=280, text="question_text", font=("Arial", 20, "italic"),
                                fill=THEME_COLOR)
        self.canvas.grid(row=1, columnspan=2, pady=50)
        self.label = Label(text="Score: 0", font=("Arial", 15, "normal"))
        self.label.config(bg=THEME_COLOR, fg="White")
        self.label.grid(row=0, column=1)
        self.right = PhotoImage(file="images/true.png")
        self.true = Button(image=self.right, highlightthickness=0, command=self.mark)
        self.true.grid(row=2, column=0)
        self.wrong = PhotoImage(file="images/false.png")
        self.false = Button(image=self.wrong, highlightthickness=0, command=self.cross)
        self.false.grid(row=2, column=1)
        self.new_question()
        self.window.mainloop()

    def new_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.text, text="Gya khatm!!! Tata Goodbye.😂😂🤣")
            self.false.config(state="disabled")
            self.true.config(state="disabled")

    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.new_question)

    def mark(self):
        self.check_answer("true")

    def cross(self):
        self.check_answer("false")
