import tkinter
from streak_quiz import StreakQuiz
from forms import *

class QuizApp():
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Trials of the Sphinx")
        self.window.geometry("620x450")

        self.canvas = tkinter.Canvas(width=800, height=250)

        ph = PhotoImage(file="ToTS\main_bg.png")
        bgimg = Label(self.window, image=ph)
        bgimg.place(x=0, y=0)
        
        self.name = self.canvas.create_text(400, 70, text="Trials of the Sphinx", width=680, fill="black", font=('Helvetica', 20, 'bold'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=30)
        self.buttons()

        self.window.mainloop()

    def buttons(self) -> None:
        streakbutton = tkinter.Button(self.window, text="Math Streak Quiz", command=self.start_streak, width=15, bg="blue", fg="white", font=("Helvetica", 16, " bold"))
        streakbutton.place(x=200, y=180)
        strucbutton = tkinter.Button(self.window, text="Structured Quiz", command=self.structured_quiz, width=15, bg="green", fg="white", font=("Helvetica", 16, " bold"))
        strucbutton.place(x=200, y=240)

    def start_streak(self) -> None:
        self.window.destroy()
        StreakQuiz()

    def structured_quiz(self) -> None:
        self.window.destroy()
        StrucQuizForm()

if __name__ == "__main__":
    QuizApp()