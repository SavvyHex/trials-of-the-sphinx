from tkinter import *
from structured_quiz import StructuredQuiz

class RegForm():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Registration Form")
        self.window.geometry("300x300")

        a = Label(self.window ,text = "Username").grid(row = 0,column = 0)
        b = Label(self.window ,text = "Full Name").grid(row = 1,column = 0)
        c = Label(self.window ,text = "Password").grid(row = 2,column = 0)
        d = Label(self.window ,text = "Repeat Password").grid(row = 3,column = 0)
        a1 = Entry(self.window).grid(row = 0,column = 1)
        b1 = Entry(self.window).grid(row = 1,column = 1)
        c1 = Entry(self.window).grid(row = 2,column = 1)
        d1 = Entry(self.window).grid(row = 3,column = 1)

        self.window.mainloop()

    def save_input(self):
        pass

class StrucQuizForm():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quiz Configuration")
        self.window.geometry("300x150")

        a = Label(self.window, text="Subject").grid(row=0, column=0)
        b = Label(self.window, text="Number of Questions").grid(row=1, column=0)

        self.sub = StringVar()
        self.n_q = IntVar()
        self.sub.set("General Knowledge")
        self.n_q.set(5)
        self.pick_sub = OptionMenu(self.window, self.sub, *["Science", "General Knowledge"]).grid(row=0, column=1)
        self.num_questions = OptionMenu(self.window, self.n_q, *list(map(str, list(range(5, 51, 5))))).grid(row=1, column=1)
        
        submit_button = Button(self.window, text="Submit", command=self.submit).grid(row=3, column=0)
        self.window.mainloop()

    def submit(self):
        self.window.destroy()
        StructuredQuiz(self.n_q.get(), self.sub.get())

if __name__ == "__main__":
    RegForm()