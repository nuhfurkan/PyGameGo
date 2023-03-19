from datetime import datetime
import sqlite3
import os
import pickle
import tkinter
from tkinter.simpledialog import askstring

class Saver:
    class PlayerSaver():
        def __init__(self, player, address: str) -> None:
            self.x = player.x
            self.y = player.y
            self.url = player.url
            self.address = address
            self.recordPlayer()
            pass

        def recordPlayer(self):
            fileX = open(self.address+"/x", "wb")
            pickle.dump(self.x, fileX)
            fileX.close()

            fileY = open(self.address+'/y', "wb")
            pickle.dump(self.y, fileY)
            fileY.close()

            fileUrl = open(self.address+'/url', "wb")
            pickle.dump(self.url, fileUrl)
            fileUrl.close()
            pass

        pass

    def __init__(self) -> None:
        self.now = datetime.now()
        self.current_time = str(self.now)
        #print(self.current_time)
        self.conn = sqlite3.connect("records")
        self.initiateDataBase()
        pass

    def initiateDataBase(self):
        if os.path.exists("recordsFiles") == False:
            os.makedirs("recordsFiles")
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS games([gameId] INTEGER PRIMARY KEY AUTOINCREMENT, [fileName] TEXT NOT NULL, [recordName] TEXT)")
        self.conn.commit()
        c.close()
        pass

    def Save(self, game):
        os.makedirs("recordsFiles/"+self.current_time)
        os.makedirs("recordsFiles/"+self.current_time+'/player')
        playerRecord = self.PlayerSaver(game.player, "recordsFiles/"+self.current_time+'/player')
        recordFileElems = open("recordsFiles/"+self.current_time+'/elems', "wb")
        pickle.dump(game.elems, recordFileElems)
        recordFileElems.close()
        
        newMessage = tkinter.Tk()
        newMessage.geometry("0x0")
        name = askstring('Name', 'Enter a record name?')
        newMessage.destroy()

        c = self.conn.cursor()
        c.execute(
               "INSERT INTO games(fileName, recordName) VALUES('"+
                self.current_time+"',"+
                "'"+name+"'"
            ")"
        )
        self.conn.commit()
        c.close()
        pass