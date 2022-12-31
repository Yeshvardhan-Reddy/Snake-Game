from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        scoreboard.repeat_game()
        snake.new_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.repeat_game()
            snake.new_snake()


# screen.exitonclick()
