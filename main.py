from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()
screen.onkey(paddle.left_up,"w")
screen.onkey(paddle.left_down,"s")
screen.onkey(paddle.right_up,"Up")
screen.onkey(paddle.right_down,"Down")





game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
 # ball collide with paddle
    if ball.xcor() > 320 and ball.distance(paddle.right_paddle) <50 or ball.xcor() < -320 and ball.distance(paddle.left_paddle) < 50:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() == 380:
        scoreboard.left_score_increase()
        ball.reset()
    if ball.xcor() == -380:
        scoreboard.right_score_increase()
        ball.reset()

    if scoreboard.score_left == scoreboard.FINAL_SCORE or scoreboard.score_right == scoreboard.FINAL_SCORE:
        scoreboard.game_over()
        game_on = False























screen.exitonclick()