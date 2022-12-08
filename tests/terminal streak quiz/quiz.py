import random
from typing import List
from question import Question

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.operations = ["+", "-", "*", "/"]
    
    def get_question(self) -> Question:
        pass

    def run(self) -> None:
        while True:
            pass

if __name__ == "":
    game = Game()
    game.run()
    input()