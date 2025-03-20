import pygame

class Platforms:
    def __init__(self, x, y):# gives some basic properties
        self.x = x
        self.y = y
        self.move_x = 0
        self.move_y = 0
        self.image = pygame.image.load("platform.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])