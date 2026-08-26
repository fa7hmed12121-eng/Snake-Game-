from turtle import Turtle

#snake body
class Snake:
    pass
    #globle opjects
    def __init__(self):
     self.Turtles = []
     self.destince = [(60,0),(40,0),(20,0),(0,0)]
     self.create_snake()
     self.head = self.Turtles[-1]
    #create snake
    def create_snake(self):
       for i in range(len(self.destince)):
        a_snake = Turtle("square")
        a_snake.color("white")
        a_snake.penup()
        a_snake.goto(self.destince[i])
        self.Turtles.append(a_snake)  

    #move turtles
    def move(self):
      for a in range(len(self.Turtles)-1):
        #All snakes follow the head snake
        self.Turtles[a].goto(self.Turtles[a+1].pos())
      self.Turtles[-1].forward(20)

    #change turtle destince
    def go_up(self):
      self.Turtles[-1].setheading(90)
      
    def go_down(self):
     self.Turtles[-1].setheading(270)

    def go_left(self):
      self.Turtles[-1].setheading(180)

    def go_right(self):
      self.Turtles[-1].setheading(0)

  #Create a new turtle
    def new_snake(self):
      self.a_snake = Turtle("square")
      self.a_snake.penup()
      self.a_snake.color("yellow")
      self.Turtles.insert(0,self.a_snake)

 
    

  
  
     