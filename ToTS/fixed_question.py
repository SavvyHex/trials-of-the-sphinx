class Question():
    def __init__(self, question:str, options:list, ans:str) -> None:
        self.question = question
        self.options = options
        self.ans = ans

    def __str__(self) -> str:
        return f"""{self.question}
a) {self.options[0]}
b) {self.options[1]}
c) {self.options[2]}
d) {self.options[3]}"""

    def __repr__(self) -> str:
        return str(self)