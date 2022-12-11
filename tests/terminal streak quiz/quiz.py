import os
import time
import threading

from question import Question
from utils import make_fair

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.get_question()
        self.running = True
        self.guess = None
    
    def get_question(self) -> None:
        self.question = Question()

    def countdown(self) -> None:
        time.sleep(60)
        self.game_over()

    def game_over(self) -> None:
        print("GAME OVER")
        print(f"The answer was {self.question.ans}")
        print(f"Your score was {self.score}")
        os._exit(0)

    def run(self) -> None:
        print("\nAnswer all questions you can in one minute... Any wrong answer will lead to elimination... Good luck!")
        for i in range(3,0,-1):
            print(f"{i}...")
            time.sleep(0.5)
        print("GO!\n")

        timer = threading.Thread(target=self.countdown)
        timer.daemon = True
        timer.start()
        while self.running:
            print(self.question)
            self.question.ans = make_fair(self.question.ans)
            self.guess = input()
            
            try:
                self.guess = float(self.guess)
            except ValueError:
                print("Please Enter a proper number")
                self.guess = None

            if self.guess == self.question.ans:
                print("Correct")
                self.score += 1
                self.get_question()
            elif self.guess == None:
                self.running = False
            else:
                self.game_over()
                self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()