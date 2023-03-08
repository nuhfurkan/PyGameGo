import pygame

class Player:
    def __init__(self, x ,y, url) -> None:
        self.x = x
        self.y = y
        self.url = url
        self.heigth = 100
        self.width = 100

        self.set_image()
        pass

    def set_heigth(self, new_heigth):
        self.heigth = new_heigth
        self.set_image()
    
    def set_width(self, new_width):
        self.width = new_width
        self.set_image()

    def get_width(self):
        return self.width

    def get_heigth(self):
        return self.heigth

    def move_x(self, change):
        self.x += change

    def move_y(self, change):
        self.y += change
        
"""
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
"""

    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
    
    def set_image(self):
        self.image = pygame.image.load(self.url)
        self.image = pygame.transform.scale(self.image, (self.width, self.heigth))

    def display(self, gameDisplay: pygame.surface):
        gameDisplay.blit(self.image, (self.x,self.y))
