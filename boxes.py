import tkinter
from tkinter import messagebox

class Box:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.geometry("0x0")
        pass
    pass

class MessageBox(Box):
    pass

class ErrorBox(Box):
    def __init__(self, message) -> None:
        super().__init__()
        self.message = message

    def diplay(self):
        self.window
        messagebox.showerror("Error", self.message)
        print(self.message)
        pass 
    pass