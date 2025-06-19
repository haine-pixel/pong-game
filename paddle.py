from turtle import Turtle
paddle_start_cords = [(350,0),(-350,0)]
PADDLE_SPEED = 30
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_list = []
        self.create_paddle()
        self.left_paddle = self.paddle_list[1]
        self.right_paddle = self.paddle_list[0]

    def create_paddle(self):
        for cords in paddle_start_cords:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.speed("fastest")
            new_paddle.shapesize(stretch_wid=5,stretch_len=1)
            new_paddle.penup()
            new_paddle.goto(cords)
            self.paddle_list.append(new_paddle)

    def left_up(self):
        if self.left_paddle.ycor() < 260:
            new_y = self.left_paddle.ycor() + PADDLE_SPEED
            self.left_paddle.goto(self.left_paddle.xcor(),new_y)

    def left_down(self):
        if self.left_paddle.ycor() > -260:
            new_y = self.left_paddle.ycor() - PADDLE_SPEED
            self.left_paddle.goto(self.left_paddle.xcor(),new_y)

    def right_up(self):
        if self.right_paddle.ycor() < 260:
            new_y = self.right_paddle.ycor() + PADDLE_SPEED
            self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def right_down(self):
        if self.right_paddle.ycor() > -260:
            new_y = self.right_paddle.ycor() - PADDLE_SPEED
            self.right_paddle.goto(self.right_paddle.xcor(), new_y)






