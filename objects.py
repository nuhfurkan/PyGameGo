import pygame
from colors import Color
from events import *
from errors import *

class Object:
    def __init__(self) -> None:
        self.collide = Collider()
        self.err = Error()
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
        pass

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_h(self):
        return self.h
    
    def get_w(self):
        return self.w

    def get_collider(self):
        return self.collide
    
    def check_error(self):
        return self.err.any_error()
    
    def display_errors(self, gameDisplay):
        self.err.display(gameDisplay=gameDisplay)
        pass

    pass

class Text(Object):
    def __init__(self, text: str) -> None:
        Object.__init__(self)
        self.text = text
        self.font = pygame.font.SysFont(None, 24)
        self.textSurface = self.font.render(text, True, Color("black").get_color())
        
    def text_surface(self):
        return self.textSurface
    
    def get_rect(self):
        return self.textSurface.get_rect()
    
class Rectangle(Object):
    def __init__(self, x, y, w, h, color = Color("black").get_color()) -> None:
        Object.__init__(self)
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

class Line(Object):
    def __init__(self, start_x, start_y, end_x, end_y, width, color = Color("black").get_color()) -> None:
        Object.__init__(self)
        self.sx = start_x
        self.sy = start_y
        self.ex = end_x
        self.ey = end_y
        self.color = color
        self.w = width
        pass

    def display(self, gameDisplay):
        pygame.draw.line(gameDisplay, self.color, (self.sx, self.sy), (self.ex, self.ey), self.w)
        pass

class Circle(Object):
    def __init__(self, x, y, radius, color = Color("black").get_color()) -> None:
        Object.__init__(self)
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
        pass

    def display(self, gameDisplay):
        pygame.draw.circle(gameDisplay, self.color, (self.x, self.y), self.r)
        pass

class Polygon(Object):
    def __init__(self, coordinates: tuple, color = Color("black").get_color()) -> None:
        Object.__init__(self)
        self.cords: tuple = ()
        if self.set_cords(coordinates) == False:
            self.err.set_error("Not matching coordinates")
        self.color = color
        pass

    def set_cords(self, coordinates):
        for elem in coordinates:
            if type(elem) == type(tuple):
                if len(elem) == 2:
                    continue
                else:
                    return False
            else:
                return False
        self.cords = coordinates
        return True

    def display(self, gameDisplay):
        pygame.draw.polygon(gameDisplay, self.color, self.cords)
        pass    