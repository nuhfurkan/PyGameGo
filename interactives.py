from objects import Rectangle
from colors import Color

class InteractiveObject:
    def __init__(self) -> None:
        pass

    def onClick(self, onDoFunc: function):
        onDoFunc()
        pass

    def onHover(self, onDoFunc: function):
        onDoFunc()
        pass

class RectangleButton(Rectangle, InteractiveObject):
    def __init__(self, x, y, w, h, color=Color("black").get_color()) -> None:
        super().__init__(x, y, w, h, color) # constructer for Rectangle class
        super(Rectangle, self).__init__(InteractiveObject)  # constructer for InteractiveObject class