from datetime import datetime
import sqlite3
import os
import  dill as pickle
import tkinter
from tkinter.simpledialog import askstring
import shutil

class Saver:
    # A temporary shadow object of records
    class PlayerSaver():
        def __init__(self, player, address: str) -> None:
            self.x = player.x
            self.y = player.y
            self.url = player.url
            self.address = address
            self.recordPlayer()
            pass

        # pygaem.surface does not pickle, so players recorded seperately
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

    # Create database if there is no
    def initiateDataBase(self):
        if os.path.exists("recordsFiles") == False:
            os.makedirs("recordsFiles")
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS games([gameId] INTEGER PRIMARY KEY AUTOINCREMENT, [fileName] TEXT NOT NULL, [recordName] TEXT)")
        self.conn.commit()
        c.close()
        pass

    # Save records
    # recoverData is a parameter if override is necessary
    def Save(self, game, recoverData = None):
        thisTime = self.current_time
        name = None
        
        if recoverData != None:
            c = self.conn.cursor()
            print("Record name: " + recoverData.fname)
            c.execute(
               "DELETE FROM games WHERE gameId = "+ str(recoverData.id) + ";"
            )
            self.conn.commit()
            c.close()
            shutil.rmtree(recoverData.fname)
            name = recoverData.name
            thisTime = recoverData.fname.split("/")[-1]	
            pass
        os.makedirs("recordsFiles/"+thisTime)
        os.makedirs("recordsFiles/"+thisTime+'/player')
        playerRecord = self.PlayerSaver(game.player, "recordsFiles/"+thisTime+'/player')
        recordFileElems = open("recordsFiles/"+thisTime+'/elems', "wb")
        pickle.dump(game.elems, recordFileElems)
        recordFileElems.close()

        recordFileIntElems = open("recordsFiles/"+thisTime+'/intElems', "wb")
        pickle.dump(game.interaticeObjects, recordFileIntElems)
        recordFileIntElems.close()
        
        if name == None:
            newMessage = tkinter.Tk()
            newMessage.geometry("0x0")
            name = askstring('Name', 'Enter a record name?')
            newMessage.destroy()

        c = self.conn.cursor()
        c.execute(
               "INSERT INTO games(fileName, recordName) VALUES('"+
                thisTime+"',"+
                "'"+name+"'"
            ")"
        )
        self.conn.commit()
        c.close()
        pass