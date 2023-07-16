from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("green")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

