import os
import time
import threading

from question import Question

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

    def enterhighscore(self) -> None:
        with open("highscore.txt", "r+") as f:
            try:
                highscore = int(f.read())
            except ValueError:
                highscore = 0
        if highscore < self.score:
            print("NEW HIGHSCORE")
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))

    def game_over(self) -> None:
        print("GAME OVER")
        print(f"The answer was {self.question.ans_opt}){self.question.ans}")
        print(f"Your score was {self.score}")
        self.enterhighscore()
        os._exit(0)

    def run(self) -> None:
        print("\nAnswer all questions you can in one minute... Any wrong answer will lead to elimination... Good luck!")
        for i in range(3,0,-1):
            print(f"{i}...")
            time.sleep(1)
        print("GO!\n")

        timer = threading.Thread(target=self.countdown)
        timer.daemon = True
        timer.start()
        while self.running:
            print(self.question)
            self.guess = input().lower()
            while self.guess not in "abcd":
                print("Please enter ONLY a, b, c or d")
                self.guess = input().lower()

            if self.guess == self.question.ans_opt:
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