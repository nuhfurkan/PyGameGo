from datetime import datetime
import sqlite3
import os
import pickle

class Saver:
    def __init__(self) -> None:
        self.now = datetime.now()
        self.current_time = str(self.now)
        print(self.current_time)
        self.conn = sqlite3.connect("records")
        self.initiateDataBase()
        pass

    def initiateDataBase(self):
        os.makedirs("recordsFiles")
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS games([gameId] INTEGER PRIMARY KEY, [recordDate] timestamp, [fileName] TEXT NOT NULL)")
        self.conn.commit()
        c.close()
        pass

    def Save(self, elems: list):
        recordFile = open(self.current_time, "wb")
        pickle.dump(elems, recordFile)
        recordFile.close()
        pass
    

mySaver = Saver()


