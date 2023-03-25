from objects import Rectangle, Object
from colors import Color
import pygame

class InteractiveObject(Object):
    def __init__(self) -> None:
        Object.__init__(self)
        self.onHoverFunc: function = None
        self.onClickFunc: function = None
        pass

    def onClick(self, onDoFunc = None):
        self.onClickFunc = onDoFunc
        pass

    def isClick(self, coords) -> bool:
        return False

    def onHover(self, onDoFunc = None):
        self.onHoverFunc = onDoFunc
        pass

    def isHover(self, coords) -> bool:
        if self.get_x()+self.get_w() > coords[0] > self.get_x() and self.get_y() + self.get_h() > coords[1] > self.get_y():
            return True
        return False

    def handleEvents(self, coords):
        if self.isHover(coords) == True:
            self.onHoverFunc()
        if self.isClick(coords) == True:
            self.onClickFunc()
        pass

class RectangleButton(InteractiveObject):
    def __init__(self, x, y, w, h, color = Color("black").get_color()) -> None:
        InteractiveObject.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cords = []
        self.set_cords()
        self.color = color
        pass

    def set_cords(self):
        self.cords = [self.x, self.y, self.w, self.h]
        pass

    def display(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, self.cords)
        pass
        