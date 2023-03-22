from objects import Rectangle, Object
from colors import Color
import pygame

class InteractiveObject(Object):
    def __init__(self) -> None:
        Object.__init__()
        pass

    def onClick(self, onDoFunc: function):
        onDoFunc()
        pass

    def onHover(self, onDoFunc: function):
        onDoFunc()
        pass

    def handleEvents(self):
        pass

class RectangleButton(InteractiveObject):
    def __init__(self, x, y, w, h, color = Color("black").get_color()) -> None:
        InteractiveObject.__init__()
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
        