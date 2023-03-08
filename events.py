import pygame

class Collider:
    def __init__(self) -> None:
        self.collidable = True
        pass

    def get_collidable(self):
        return self.collidable
    pass

class EventHandler:
    def __init__(self) -> None:
        pass

    def handle_collision(self, player, elems):
        for elem in elems:
            if elem.get_collider().get_collidable() == True:
                if player.get_x() > (elem.get_x() + elem.get_w()):
                    continue
                if (player.get_x()+player.get_width()) < elem.get_x():
                    continue
                if player.get_y() > (elem.get_y() + elem.get_h()):
                    continue
                if player.get_y()+player.get_heigth() < elem.get_y():
                    continue
                else:
                    return True
        return False
