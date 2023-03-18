import tkinter
from game import Game
from objects import Rectangle, Circle
from player import Player

class Navigator:
    def __init__(self, gameName) -> None:
        self.gameName = gameName
        self.navigation = tkinter.Tk()
        self.navigation.title(self.gameName)
        self.navigation.geometry('800x600')

        playButton = tkinter.Button(self.navigation, text="New Game", command=self.newGame)
        playButton.pack()

        self.navigation.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.navigation.mainloop()
        pass

        
    def newGame(self):
        myGame = Game(self.gameName)
        myUfo = Player(10, 10, "images/ufo.png")

        myRect = Rectangle(300, 300, 150, 150)
        myCircle = Circle(150, 150, 25)

        myGame.add_elem(myCircle)
        myGame.add_elem(myRect)
        myGame.add_player(myUfo)

        self.navigation.destroy()
        myGame.StartGame()
        pass

    

    def onClosing(self):
        quit()

        
