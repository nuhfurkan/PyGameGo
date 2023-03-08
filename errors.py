from boxes import ErrorBox

class Error:
    def __init__(self) -> None:
        self.errors: list = []
        pass

    def set_error(self, error):
        self.errors.append(error)
        pass

    def any_error(self):
        if len(self.errors) == 0:
            return False
        else:
            return True
        
    def get_errors(self):
        return self.errors
    
    def display(self, gameDisplay):
        errorMessage = ""
        for error in self.errors:
            errorMessage += error + "\n"

        thisErrorBox = ErrorBox(errorMessage) 
        thisErrorBox.diplay(gameDisplay=gameDisplay)
        pass