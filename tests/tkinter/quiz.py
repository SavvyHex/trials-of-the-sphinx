from tkinter import *

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
        title = Label(self.window, text="iQuiz Application",
                        width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

if __name__ == "__main__":
    QuizApp()