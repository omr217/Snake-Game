from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
screen.listen()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")


    if snake.segments[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score_board.update_score()
        score_board.clear()
        score_board.increase_score()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score_board.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score_board.game_over()





















































screen.exitonclick()