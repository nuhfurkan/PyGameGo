import sqlite3

class Reader:
    class PastGame:
        def __init__(self, gameId: int, fileName: str = "", recordName: str = "") -> None:
            self.id = gameId
            self.fname = fileName
            self.name = recordName
            pass

        def printThis(self):
            print(self.id)
            print( self.fname)
            print(self.name)
            pass

        def __str__(self) -> str:
            return self.name
        pass

    def __init__(self) -> None:
        self.conn = sqlite3.connect("records")
        self.records = self.readRecords()
        pass

    def getRecords(self):
        return self.records

    # Method to read records from "games" table, "records" file
    """
    Structure of the "games" table
        gameId -> INTEGER PRIMARY KEY AUTOINCREMENT
        fileName -> TEXT NOT NULL // the name of the file timestamp taken by the Saver objects
        recordName -> TEXT // the name of the save given by the player
    """
    def readRecords(self):
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS games([gameId] INTEGER PRIMARY KEY AUTOINCREMENT, [fileName] TEXT NOT NULL, [recordName] TEXT)")
        c.execute("SELECT * FROM games")
        data = c.fetchall()
        res = []

        for elem in data:
            pGame = self.PastGame(
                gameId=elem[0],
                fileName=elem[1],
                recordName=elem[2]
            )
            res.append(pGame)
        return res