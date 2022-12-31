from tkinter import *
from tkinter import messagebox
from structured_quiz import StructuredQuiz

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
        StructuredQuiz(self.n_q.get(), "gk" if self.sub.get() == "General Knowledge" else "sci")

class RegForm():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Registration")
        self.window.geometry("300x150")

        a = Label(self.window, text="Username").grid(row=0, column=0)
        b = Label(self.window, text="Password").grid(row=1, column=0)
        c = Label(self.window, text="Confirm Password").grid(row=2, column=0)

        self.name = StringVar()
        self.pwd = StringVar()
        self.c_pwd = StringVar()
        self.enter_name = Entry(self.window, textvariable=self.name).grid(row=0, column=1)
        self.enter_pwd = Entry(self.window, textvariable=self.pwd, show="*").grid(row=1, column=1)
        self.confirm_pwd = Entry(self.window, textvariable=self.c_pwd, show="*").grid(row=2, column=1)
        
        submit_button = Button(self.window, text="Submit", command=self.submit).grid(row=3, column=0)
        self.window.mainloop()

    def submit(self):
        from main import QuizApp
        pwd = self.pwd.get()
        name = self.name.get()
        c_pwd = self.c_pwd.get()
        if pwd == c_pwd:
            with open("user_info.txt", "w") as info:
                info.write(f"{name} {pwd}")
            messagebox.showinfo("SUCCESS!", "You have successfully registered...\nClose this notification to return to the main page")
            self.window.destroy()
            QuizApp()
        else:
            messagebox.showinfo("ERROR!", "Please ensure that \"Password\" and \"Confirm Password\" match.")

class LoginForm():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("300x150")

        a = Label(self.window, text="Username").grid(row=0, column=0)
        b = Label(self.window, text="Password").grid(row=1, column=0)

        self.name = StringVar()
        self.pwd = StringVar()
        self.enter_name = Entry(self.window, textvariable=self.name).grid(row=0, column=1)
        self.enter_pwd = Entry(self.window, textvariable=self.pwd, show="*").grid(row=1, column=1)
        
        submit_button = Button(self.window, text="Submit", command=self.submit).grid(row=3, column=0)
        self.window.mainloop()

    def submit(self):
        from main import QuizApp
        pwd = self.pwd.get()
        name = self.name.get()
        with open("user_info.txt", "r") as info:
            data = info.read().split()
        if name == data[0] and pwd == data[1]:
            messagebox.showinfo("SUCCESS!", "You have successfully logged in")
            self.window.destroy()
            QuizApp()
        else:
            messagebox.showinfo("ERROR!", "Incorrect username/password")

if __name__ == "__main__":
    RegForm()