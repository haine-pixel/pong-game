from turtle import Turtle
FONT_LINE = ("arial",15,"normal")
FONT_NUMBER = ("arial",60,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.score_board()
        self.FINAL_SCORE = 6
    def add_score(self):
        pass

    def score_board(self):
        self.clear()
        self.teleport(-150,200)
        self.write(f"{self.score_left}",move = False, align = "center",font = FONT_NUMBER)
        self.teleport(150, 200)
        self.write(f"{self.score_right}", move=False, align="center", font=FONT_NUMBER)
        self.central_line()

    def right_score_increase(self):
        self.score_right += 1
        self.score_board()
    def left_score_increase(self):
        self.score_left += 1
        self.score_board()


    def central_line(self):
        y_cords = 300
        for i in range(27):
            self.goto(0,y_cords)
            self.write("|",move = False,align="center",font=FONT_LINE)
            y_cords -= 30


    def game_over(self):
        self.home()
        self.write("GAME OVER", move = False, align = "center", font = FONT_NUMBER )