import random

from utils import make_fair

class Question:
    def __init__(self) -> None:
        self.op = random.choice(["+", "-", "*", "/"])
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)
        self.get_ans()
        self.get_options()

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
        self.ans = make_fair(self.ans)

    def get_options(self) -> None:
        indices = [0, 1, 2, 3]
        self.options = [0, 0, 0, 0]
        o1 = self.ans
        o2 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        o3 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        o4 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        ops = [o1, o2, o3, o4]
        while indices:
            index = random.choice(indices)
            choice = random.choice(ops)
            self.options[index] = choice
            indices.remove(index)
            ops.remove(choice)
        self.ans_opt = chr(self.options.index(self.ans) + 97)

    def __str__(self) -> str:
        return f"""What is {self.a}{self.op}{self.b}?
a) {self.options[0]}
b) {self.options[1]}
c) {self.options[2]}
d) {self.options[3]}"""

    def __repr__(self) -> str:
        return str(self)