class Box:
    pass

class MessageBox(Box):
    pass

class ErrorBox(Box):
    def __init__(self, message) -> None:
        super().__init__()
        self.message = message

    def diplay(self, gameDisplay):
        print(self.message)
        pass 
    pass