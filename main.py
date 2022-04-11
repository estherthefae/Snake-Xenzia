from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

tims = []
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()


begin_game = True
while begin_game:
    scoreboard.write_score()
    screen.update()
    snake.move()
    screen.onkey(fun= snake.move_up, key="Up")
    screen.onkey(fun= snake.move_down, key="Down")
    screen.onkey(fun=snake.move_left, key="Left")
    screen.onkey(fun=snake.move_right, key="Right")

    if snake.head.distance(food) < 15:
        food.change_food_location()
        if scoreboard.score % 4 == 0 and scoreboard.score != 0:
            scoreboard.update_score_big()
        else:
            scoreboard.update_score_normal()
        if scoreboard.score % 4 == 0:
            food.big_ball()
        else:
            food.normal_ball()
        scoreboard.clear()
        snake.grow()
        scoreboard.write_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        begin_game = False
        scoreboard.end_game()

    for tim in snake.tims[1:]:
        if snake.head.distance(tim) < 10:
            begin_game = False
            scoreboard.end_game()
screen.exitonclick()
