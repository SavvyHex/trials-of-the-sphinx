import tkinter
from streak_quiz import StreakQuiz

class QuizApp():
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Trials of the Sphinx")
        self.window.geometry("850x530")
        self.window.mainloop()

if __name__ == "__main__":
    QuizApp()