from turtle import Turtle, Screen
from random import Random, randint

WIDTH = 800
HEIGHT = 600
START_X = -int(WIDTH/2)+10
FINISH_X = abs(WIDTH/2)-50

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# kittu = Turtle()
screen = Screen()
screen.title("The Turtle Race")
screen.setup(width = WIDTH, height = HEIGHT)
screen.colormode(255)
game_on = True

# kittu.goto(START_X, 0)

def get_players(num):
    players = []
    for i in range(num):
        player = Turtle()
        player.shape("turtle")
        player.color(random_color())
        player.penup()
        players.append(player)
    return players

def set_players(players):
    for i in range(len(players)):
        if i % 2 == 0:
            players[i].goto(START_X, (i+1)*(WIDTH/(3*num_of_players)))
        else:
            players[i].goto(START_X, -(i+1)*(WIDTH/(3*num_of_players)))

def move_players(players):
    for player in players:
        player.forward(randint(1,10))

def is_game_on(players):
    for player in players:
        if player.xcor() > FINISH_X:
            player.resizemode("user")
            player.shapesize(2, 2, 1)
            return False
    return True

num_of_players = int(screen.textinput(title = "Guess the Winner", prompt="Your guess: "))
print(num_of_players)
players = get_players(num_of_players)
set_players(players)

while is_game_on(players):
    move_players(players)



screen.exitonclick()