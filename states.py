from turtle import Turtle

class States:
    def __init__(self, position):
        self.position = position
        self.city = Turtle()
    def go_to_city(self):
        self.city.penup()
        self.city.goto(self.position[0],self.position[1])
        self.city.write(self.position[2], font=("Arial", 8, "bold"))
        self.city.pendown()
