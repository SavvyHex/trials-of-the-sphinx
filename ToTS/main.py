import tkinter
from streak_quiz import StreakQuiz

class QuizApp():
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Trials of the Sphinx")
        self.window.geometry("850x530")

        self.canvas = tkinter.Canvas(width=800, height=250)
        self.name = self.canvas.create_text(400, 125, text="Trials of the Sphinx", width=680, fill="black", font=('Helvetica', 20, 'bold'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=30)
        self.buttons()

        self.window.mainloop()

    def buttons(self) -> None:
        streakbutton = tkinter.Button(self.window, text="Streak Quiz", command=self.start_streak, width=15, bg="blue", fg="white", font=("Helvetica", 16, " bold"))
        streakbutton.place(x=320, y=200)

    def start_streak(self) -> None:
        self.window.destroy()
        StreakQuiz()

if __name__ == "__main__":
    QuizApp()