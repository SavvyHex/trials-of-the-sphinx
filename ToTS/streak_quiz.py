from tkinter import *
from tkinter import messagebox
from math_question import Question

class StreakQuiz:
    def __init__(self) -> None:

        self.score = 0

        self.window = Tk()
        self.window.title("Trials of the Sphinx (Streak)")
        self.window.geometry("620x450")

        self.display_title()

        self.canvas = Canvas(width=620, height=450)

        self.question_text = self.canvas.create_text(350, 100, text="Question here", width=680, fill="black", font=('Helvetica', 20, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=10, font=("Helvetica", 15, "bold"))
        self.feedback.place(x=250, y=380)

        self.buttons()

        self.window.mainloop()
    
    def display_title(self):
        title = Label(self.window, text="Math Streak Quiz!", width=40, bg="teal", fg="orange", font=("Helvetica", 24, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        self.question = Question()
        self.canvas.itemconfig(self.question_text, text=self.question.question)

    def radio_buttons(self):
        choice_list = list()
        y = 175
        for option in self.question.options:
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("Helvetica", 14))
            choice_list.append(radio_btn)
            radio_btn.place(x=200, y=y)
            y += 40
        return choice_list

    def display_options(self):
        val = 0
        self.user_answer.set(None)
        for option in self.question.options:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        if str(self.question.ans) == str(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer!'
            self.score += 1
            self.display_question()
            self.display_options()
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = (f'WRONG! The right answer is: {self.question.ans}')
            self.display_result()
            self.score = 0

    def buttons(self):
        next_button = Button(self.window, text="Next", command=self.next_btn, width=10, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        next_button.place(x=300, y=350)
        quit_button = Button(self.window, text="Quit", command=self.quit, width=5, bg="red", fg="white", font=("Helvetica", 16, " bold"))
        quit_button.place(x=500, y=50)

    def display_result(self):
        messagebox.showinfo("SCORE", f"Your score was {self.score}")

    def quit(self):
        from main import QuizApp
        self.display_result()
        self.window.destroy()
        QuizApp()