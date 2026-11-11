## Steps

<aside>

The Algorithm of Snake game, [algorithm.draw.io](Snake_game.drawio.png)

</aside>

#### 1.Create the main file to set up the game workplace [main.py](main.py)

- I have set up the using black background, using trace to reduce any cutting in the screen, updating the screen as well
- I have included all main functions in main file

---

#### 2.Create the Snake body using OOP, [Snake_body.py](Snakes.py)

- I have used OOP to create snake body, so I can make the snake body move to specific destinations
- I have generated 6 shapes as default depending on the positions (-40, -20, 0, 20, 40, 60), so I got the a full length body, to make sure that shapes are not at same position
- The default movement is 10 forward , I made the last shape is the head so all rest shapes follow it, means that they are go wherever the head shape goes

---

#### 3.Create Food using OOP as well , [food.py](Food.py)

- I have used OOP to create the food body and set up its body style, so I have create function to make it move randomly whenever the snake eat it
- The default position is the center , so whenever the game start over it will appear in (0,0)

#### 4.Make the Snake grows when it eats food

- I have added another function to generate a new shape and add it at the tail of snake body, so it will follow the head

#### 5.Score board to count how many food that snake eats, [Score.py](score.py)
