from tkinter import *
from question import Question

class QuizApp:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        self.display_title()

        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill="black",
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        self.buttons()

        self.window.mainloop()
    
    def display_title(self):
        title = Label(self.window, text="Trials of the Sphinx",
                        width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        self.question = Question()
        self.canvas.itemconfig(self.question_text, text=self.question.question)

    def radio_buttons(self):
        choice_list = list()
        y = 220
        for option in self.question.options:
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("ariel", 14))
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
        if self.question.ans == self.user_answer.get():
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                        f'The right answer is: {self.question.ans}')

    def buttons(self):
        next_button = Button(self.window, text="Next", command=self.next_btn,
                            width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=460)
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                            width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)

if __name__ == "__main__":
    QuizApp()