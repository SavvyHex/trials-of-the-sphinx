from tkinter import *

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
        self.window.geometry("300x300")

if __name__ == "__main__":
    StrucQuizForm()
#    RegForm()