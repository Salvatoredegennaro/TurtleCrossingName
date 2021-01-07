from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.go_back()

    def go_back(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def finish_line(self):
        if self.ycor() > 280:
            return True




