import tkinter
from game import Game
from objects import Rectangle, Circle
from player import Player
from reader import Reader
from interactives import RectangleButton
from colors import Color
import pickle

class Navigator:
    # Initiates a navigation screen using tkinter, where list of previous games presented.
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

    # Function to create a new game
    # For this part, actually another object should be send here as parameter and this method should initiate a new game by referancing that object        
    def newGame(self):
        myGame = Game(self.gameName)
        myUfo = Player(10, 10, "images/ufo.png")

        myRect = RectangleButton(300, 300, 150, 150)
        print(type(myRect))
        def buttononhoverfunc():
            myRect.color = Color(r=255, b=0, g=0).get_color()
            pass
        myRect.onHover(buttononhoverfunc)
        myCircle = Circle(150, 150, 25)

        myGame.add_elem(myCircle)
        myGame.add_interactive(myRect)
        myGame.add_player(myUfo)

        self.navigation.destroy()
        myGame.StartGame()
        pass

    # Method to fetch list of previous games from records file - sqlite
    def loadPreviousGames(self):
        reader = Reader()
        for elem in reader.getRecords():
            self.gameList.insert(elem.id, elem)
        pass

    # Method called when a previous game selected
    def selectListItem(self):
        cs = self.gameList.curselection()
        #print(cs[0])
        reader = Reader()
        pgame = reader.getRecords()[cs[0]]
        pgame.printThis()
        self.oldGame(pgame)
        pass

    # Method to recover a previously recorded game from the recorded data
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
        fileIntElem = open(game.fname+"/intElems", "rb")
        elems = pickle.load(fileelem)
        intElems = pickle.load(fileIntElem)

        for elem in intElems:
            myGame.add_interactive(elem)
        for elem in elems:
            myGame.add_elem(elem)
        myGame.add_player(myUfo)

        self.navigation.destroy()
        myGame.isRecovered = True
        myGame.recoverData = game
        myGame.StartGame()
        pass

    # Close navigator - end app
    def onClosing(self):
        quit()