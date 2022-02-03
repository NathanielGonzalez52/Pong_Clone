from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
p_one = Paddle((350,0))
p_two = Paddle((-350,0))
ball = Ball()
game_is_on = True
game_start = True
hit_paddle = 0
top = False
bot = False
n = 0
while game_is_on == True:

    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(p_one.move_up, "Up")
    screen.onkeypress(p_one.move_down, "Down")
    screen.onkeypress(p_two.move_up,"w")
    screen.onkeypress(p_two.move_down,"s")

    ball.move()
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    #Detect collision with right paddle and left paddle

    if ball.distance(p_one) < 50 and ball.xcor() > 320 or ball.distance(p_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    #right paddle misses
    if ball.xcor()>450:
        ball.out_of_bounds()
        scoreboard.l_point()
    #left paddle misses
    if ball.xcor()<-450:
        ball.out_of_bounds()
        scoreboard.r_point()








screen.exitonclick()