from boxes import ErrorBox

class Color:
    colorList = {
        "white": (255, 255, 255),
        "black": (0,0,0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }

    def __init__(self, name: str="", r:int=0, g:int=0, b:int=0) -> None:
        if name != "":
            try:
                tpl = self.colorList[name]
            except:
                ErrorBox("Undefined color name used").diplay()
            self.red = tpl[0]
            self.green = tpl[1]
            self.blue = tpl[2]
        else:
            self.red = r
            self.green = g
            self.blue = b
        pass

    def set_color(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def get_color(self):
        return (
            self.red,
            self.green,
            self.blue
        )