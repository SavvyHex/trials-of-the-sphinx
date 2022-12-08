import random

class Question:
    def __init__(self) -> None:
        self.op = random.choice(["+", "-", "*", "/"])
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)
        self.get_ans()

    def get_ans(self) -> None:
        op = self.op
        if op == "+":
            self.ans = self.a + self.b
        elif op == "-":
            self.ans = self.a - self.b
        elif op == "*":
            self.ans = self.a * self.b
        elif op == "/":
            self.ans = self.a / self.b