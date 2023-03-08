from player import *
from game import Game
from objects import *

myGame = Game("The Game")
myUfo = Player(10, 10, "images/ufo.png")

myRect = Rectangle(300, 300, 150, 150)
myCircle = Circle(150, 150, 25)

myGame.add_elem(myCircle)
myGame.add_elem(myRect)
myGame.add_player(myUfo)
myGame.StartGame()

