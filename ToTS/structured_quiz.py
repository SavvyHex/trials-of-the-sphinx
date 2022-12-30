from random import shuffle
from tkinter import *
from tkinter import messagebox
from fixed_question import Question
from utils import *

class StructuredQuiz:
    def __init__(self, num:int=10, sub:str="") -> None:
        self.num = num
        self.question_number = 0

        self.correct = 0
        self.wrong = 0

        self.window = Tk()
        self.window.title("Trials of the Sphinx (Structured)")
        self.window.geometry("640x480")

        self.questions:list[Question] = list()
        self.get_questions(self.num, sub)
        self.display_title()

        self.canvas = Canvas(width=640, height=480)
        self.canvas.pack(expand=True, fill=BOTH)

        bg = PhotoImage(file="ToTS\struc_bg.png")
        self.canvas.create_image(0,0,image=bg, anchor="nw")
        self.question_text = self.canvas.create_text(320, 80, text="Question here", width=480, fill="white", font=('Helvetica', 20, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        self.user_answer = StringVar()

        self.opts = self.radio_buttons()
        self.display_options()

        self.feedback = Label(self.window, pady=10, font=("Helvetica", 15, "bold"))
        self.feedback.place(x=150, y=350)

        self.buttons()

        self.window.mainloop()
    
    def get_questions(self, n:int, cat:str):
        self.questions = list()
        questions_raw = get_questions_from_net(n, cat)
        for q in questions_raw:
            ops = [make_sense(q["correct_answer"])]+list(map(make_sense, q["incorrect_answers"]))
            shuffle(ops)
            qu = Question(make_sense(q["question"]), ops, make_sense(q["correct_answer"]))
            self.questions.append(qu)

    def display_title(self):
        title = Label(self.window, text="Structured Quiz!", width=32, bg="teal", fg="orange", font=("Helvetica", 24, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        self.question = self.questions[self.question_number]
        self.canvas.itemconfig(self.question_text, text=self.question.question)

    def radio_buttons(self):
        choice_list = []
        y_pos = 180
        while len(choice_list) < 4:
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("ariel", 14))
            choice_list.append(radio_btn)
            radio_btn.place(x=200, y=y_pos)
            y_pos += 40
        return choice_list

    def display_options(self):
        val = 0
        self.user_answer.set(None)
        for option in self.question.options:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        self.question_number += 1
        if str(self.question.ans) == str(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer!'
            self.correct += 1
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = (f'WRONG! The right answer is: {self.question.ans}')
            self.wrong += 1
        if self.question_number < self.num:
            self.display_question()
            self.display_options()
        else:
            self.quit()

    def buttons(self):
        next_button = Button(self.window, text="Next", command=self.next_btn, width=10, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        next_button.place(x=320, y=420)
        quit_button = Button(self.window, text="Quit", command=self.quit, width=5, bg="red", fg="white", font=("Helvetica", 16, " bold"))
        quit_button.place(x=500, y=50)

    def display_result(self):
        try:
            accuracy = int(self.correct/self.question_number*100)
        except ZeroDivisionError:
            accuracy = 0
        messagebox.showinfo("RESULT", f"Correct : {self.correct}\nWrong : {self.wrong}\nAccuracy : {accuracy}")

    def quit(self):
        from main import QuizApp
        self.display_result()
        self.window.destroy()
        QuizApp()