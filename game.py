import pygame
import colors
from objects import *
from events import *
from player import *

class Game:
    def __init__(self, name) -> None:
        pygame.init()
        self.event_handler = EventHandler()
        self.display_width = 800
        self.display_heigth = 600
        self.game_name = name
        self.fps_count = 60
        self.elems = []
        self.player: Player = None

        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_heigth))
        pygame.display.set_caption(self.game_name)
        self.clock = pygame.time.Clock()


    def set_display_width(self, new_width):
        self.display_width = new_width
        pass

    def set_diplay_heigth(self, new_heigth):
        self.display_heigth = new_heigth
        pass

    def add_elem(self, new_elem):
        self.elems.append(new_elem)
        pass

    def add_player(self, new_player):
        self.player = new_player

    def handle_event(self, event, elem):
        x_change = 0
        y_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
        elem.move_x(x_change)
        elem.move_y(y_change)
        if self.event_handler.handle_collision(self.player, self.elems) == True:
            print("Collision")
        pass

    def message_display(self, text: Text):
        TextSurf = text.text_surface()
        TextRect = text.get_rect()
        TextRect.center = ((self.display_width/2),(self.display_heigth/2))
        self.gameDisplay.blit(TextSurf, TextRect)

    def StartGame(self):
        onGoing = True

        while onGoing:
            self.gameDisplay.fill(colors.white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onGoing = False

        #print(event)

        # Game starts here
            self.player.display(gameDisplay=self.gameDisplay)
            if self.player.get_x() > self.display_width - self.player.get_width() or self.player.get_x() < 0:
                onGoing = False
            self.handle_event(event, self.player)

            for elem in self.elems:
                if elem.check_error() == True:
                    elem.display_errors(gameDisplay = self.gameDisplay)
                else:
                    elem.display(gameDisplay=self.gameDisplay)
                
            myText = Text("Hello there")
            self.message_display(myText)

            pygame.display.update()
            self.clock.tick(self.fps_count)   

        pygame.quit()
        quit()