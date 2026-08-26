from turtle import Turtle

#score class
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.high_score =self.get_scores()
        self.penup()
        self.goto(0,220)
        self.color("white")
        self.hideturtle()
        self.update_score()
    #show the score
    def update_score(self):
        self.write(f"Score: {self.score}      High score: {self.high_score}", align="center",font=('Garamond',18, "bold"))
    # Save pervious scores
    def get_scores(self):
        with open("high_score.txt", "r") as file: 
            return  int(file.read())
        
    def save_highscore(self):
        with open("high_score.txt", "w" )as file :
           file.write(str(self.high_score))       
        
    # increase the score
    def increasing(self):
        self.clear()
        self.score +=1
        self.update_score()
        
    def end_game(self):
        self.goto(0,0)
        if self.score > self.high_score :
            self.high_score= self.score
            self.save_highscore()
        self.write(f"Game over\nfinal Score: {self.score}\nHigh score: {self.high_score}", align="center",font=('Garamond',18, "bold"))

        