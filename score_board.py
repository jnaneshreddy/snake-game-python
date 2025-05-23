from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 0, 'normal')



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score is : {self.high_score}", False, ALIGNMENT,FONT )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT)



    def increase_score(self):
        self.score+=1

        self.update_scoreboard()

