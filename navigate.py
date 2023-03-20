import tkinter
from game import Game
from objects import Rectangle, Circle
from player import Player
from reader import Reader
import pickle

class Navigator:
    def __init__(self, gameName) -> None:
        self.gameName = gameName
        self.navigation = tkinter.Tk()
        self.navigation.title(self.gameName)
        self.navigation.geometry('800x600')

        self.playButton = tkinter.Button(self.navigation, text="New Game", command=self.newGame)
        self.playButton.pack()

        self.gameList = tkinter.Listbox(self.navigation)
        self.gameList.pack()
        self.loadPreviousGames()

        self.selectGame = tkinter.Button(self.navigation, text="Play Game", command=self.selectListItem)
        self.selectGame.pack()

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

    def loadPreviousGames(self):
        reader = Reader()
        for elem in reader.readRecords():
            self.gameList.insert(elem.id, elem)
        pass

    def selectListItem(self):
        cs = self.gameList.curselection()
        #print(cs[0])
        reader = Reader()
        pgame = reader.readRecords()[cs[0]]
        pgame.printThis()
        self.oldGame(pgame)
        pass

    def oldGame(self, game):
        game.fname = "recordsFiles/" + game.fname
        myGame = Game(self.gameName)
        filex = open(game.fname+"/player/x", "rb")
        playerx = pickle.load(filex)
        filey = open(game.fname+"/player/y", "rb")
        playery = pickle.load(filey)
        fileurl = open(game.fname+"/player/url", "rb")
        playerurl = pickle.load(fileurl)
        myUfo = Player(playerx, playery, playerurl)

        fileelem = open(game.fname+"/elems", "rb")
        elems = pickle.load(fileelem)

        for elem in elems:
            myGame.add_elem(elem)
        myGame.add_player(myUfo)

        self.navigation.destroy()
        myGame.StartGame()
        pass

    def onClosing(self):
        quit()