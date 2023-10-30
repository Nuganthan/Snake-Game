from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f'Score = {self.score}', font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score = {self.score}', font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT, align=ALIGNMENT)