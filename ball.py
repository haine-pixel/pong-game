from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


    def hit_right_paddle_while_coming_up(self):
        new_xcor = self.xcor() - int(400 / 300 * 10)
        new_ycor = self.ycor() + 10
        self.goto(new_xcor, new_ycor)

    def reset(self):
        self.goto(0,0)
        self.speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.speed *= 0.9
        print(self.speed)