from turtle import Screen
from Snakes import Snake
from Food import food
from score import Score
import time
window = Screen()
window.setup(800,500)
window.bgcolor("black")
window.tracer(0)

the_food = food()
a_snake = Snake()
the_score = Score()


Snake_Game = True
while Snake_Game:
   
    window.update()
    a_snake.move()
    time.sleep(0.1)
    window.listen()
    window.onkey(a_snake.go_up, "Up")
    window.onkey(a_snake.go_down, "Down")
    window.onkey(a_snake.go_left, "Left")
    window.onkey(a_snake.go_right, "Right")
    if a_snake.head.distance(the_food) < 15:
        the_food.move()
        a_snake.new_snake()
        the_score.increasing()

    # the snake hit the walls 
    if a_snake.head.xcor() > 400 or a_snake.head.ycor() > 240 or a_snake.head.xcor() < -400 or a_snake.head.ycor() < -240 :

        Snake_Game = False
        window.bgcolor("peru")
        the_score.end_game()   

    # # the head hit a snake 
    # for snake in a_snake.Turtles:    
    #  if a_snake.head.distance(snake) < 50:
    #     Snake_Game = False
    #     window.bgcolor("peru")        
    #     the_score.end_game()

   
window.exitonclick()
