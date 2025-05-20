from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)
# position = (30)
starting_positions = [(0,0),(-20,0),(-40,0)]
    # new_turtle.backward(position)
Score = 0   # position-=10
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extand()
        scoreboard.increase_score()

    #colision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()


    #colision with tail
    for segment in snake.segemnts[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()