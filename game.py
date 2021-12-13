from turtle import Turtle, Screen
from random import Random, randint
from random_utils import random_color


class TurtleGame:

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.START_X = -int(self.WIDTH / 2) + 10
        self.FINISH_X = abs(self.WIDTH / 2) - 50
        self.players = []

    def get_players(self, num):
        for i in range(num):
            player = Turtle()
            player.shape("turtle")
            player.color(random_color())
            player.penup()
            self.players.append(player)
        return self.players

    def set_players(self, players):
        for i in range(len(players)):
            if i % 2 == 0:
                players[i].goto(self.START_X, (i + 1) * (self.WIDTH / (3 * len(players))))
            else:
                players[i].goto(self.START_X, -(i + 1) * (self.WIDTH / (3 * len(players))))

    def move_players(self, players):
        for player in players:
            player.forward(randint(1, 10))

    def is_game_on(self, players):
        for player in players:
            if player.xcor() > self.FINISH_X:
                player.resizemode("user")
                player.shapesize(2, 2, 1)
                return False
        return True
