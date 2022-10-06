import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_guess = screen.textinput(title="make your bet", prompt="Which turtle is your champion red/green/"
                                                            "blue/yellow/purple/orange ?: ")

print(user_guess)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
race_turtles = []
for turtle_racer in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_racer])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[turtle_racer])
    race_turtles.append(new_turtle)

if user_guess:
    race_on = True


while race_on:
    for turtle in race_turtles:
        if turtle.xcor() > 270:
            win_turtle = turtle.pencolor()
            if win_turtle == user_guess:
                print(f"You won! The winner was the {win_turtle} Turtle!")
            else:
                print(f"You lost!, The winner was the {win_turtle} Turtle!")
                race_on = False
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()


