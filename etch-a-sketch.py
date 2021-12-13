from turtle import Turtle, Screen

kittu = Turtle()
screen = Screen()
screen.title("Etch A Sketch")

def move_ahead():
    kittu.forward(10)

def move_back():
    kittu.backward(10)

def lookup():
    kittu.left(10)

def lookdown():
    kittu.right(10)

def clear():
    kittu.reset()

screen.onkey(move_ahead, "Right")
screen.onkey(move_back, "Left")
screen.onkey(lookup, "Up")
screen.onkey(lookdown, "Down")
screen.onkey(clear, "space")


screen.listen()

screen.exitonclick()