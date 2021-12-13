from game import *

WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.title("The Turtle Race")
screen.setup(width=WIDTH, height=HEIGHT)
screen.colormode(255)
game_on = True
game = TurtleGame(WIDTH, HEIGHT)

num_of_players = int(screen.textinput(title="Turtles ready to race", prompt="How many?"))
players = game.get_players(num_of_players)
game.set_players(players)

while game.is_game_on(players):
    game.move_players(players)

screen.exitonclick()
