from turtle import Screen
import time
import turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_game_on = True

try:
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect food collision
        if snake.head.distance(food) < 20:
            snake.extend()
            food.refresh()
            scoreboard.increase_score()

        # Detect wall collision
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 245 or snake.head.ycor() < -245):
            is_game_on = False
            scoreboard.game_over()

        # Detect self collision
        for segment in snake.segments[1:]:#skip the head
            if snake.head.distance(segment) < 10:#if the distance between head and rest of body of snake is <10 then game over
                is_game_on = False
                scoreboard.game_over()

except turtle.Terminator:
    print("Turtle screen was closed.")

screen.exitonclick()
