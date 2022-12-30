import tkinter
from streak_quiz import StreakQuiz
from forms import *

class QuizApp():
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Trials of the Sphinx")
        self.window.geometry("620x450")

        self.canvas = tkinter.Canvas(width=620, height=450)
        self.canvas.pack(expand=True, fill=BOTH)

        bg = PhotoImage(file="./main_bg.png")
        self.canvas.create_image(0,0,image=bg, anchor="nw")
        
        self.name = self.canvas.create_text(300, 70, text="Trials of the Sphinx", width=680, fill="black", font=('Helvetica', 20, 'bold'))
        name_box = self.canvas.create_rectangle(self.canvas.bbox(self.name), fill="white")
        self.canvas.tag_lower(name_box, self.name)
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