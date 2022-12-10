from typing import List
from question import Question

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.get_question()
    
    def get_question(self) -> None:
        self.question = Question()

    def run(self) -> None:
        run = True
        while run:
            print(self.question)
            if float(input()) == self.question.ans:
                print("Correct")
                self.score += 1
                self.get_question()
            else:
                print(f"WRONG!!! the correct answer is {self.question.ans}")
                print(f"Your score is {self.score}")
                run = False

if __name__ == "__main__":
    game = Game()
    game.run()