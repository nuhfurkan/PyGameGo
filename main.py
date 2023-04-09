from navigate import Navigator
from colors import Color
from player import Player
from objects import Circle
from interactives import RectangleButton
from game import Game
from nextgame import NextGame

def gameFunc(self):
    myGame = Game("some name")
    ## Creting a game can be removed

    myUfo = Player(10, 10, "images/ufo.png")

    myRect = RectangleButton(300, 300, 150, 150)
    myRect.set_img("images/ufo.png")
    print(type(myRect))
    def buttononhoverfunc():
        myRect.color = Color(r=255, b=0, g=0).get_color()
        pass
    myRect.onHover(buttononhoverfunc)
    myCircle = Circle(150, 150, 25)

    myGame.add_elem(myCircle)
    myGame.add_interactive(myRect)
    myGame.add_player(myUfo)

    ## Also, I want to remove those 2 lines
    myGame.StartGame()

myNextGame = NextGame("test")
myNextGame.bind(gameFunc)
myNextGame.start()
