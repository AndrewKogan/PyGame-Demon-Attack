import pygame

class Devil:
    def __init__(self, x, y): # gives some basic properties
        self.x = x
        self.y = y
        self.is_jumping = True
        self.is_falling = False
        self.move_x = 0
        self.move_y = 0
        self.image = pygame.image.load("devil.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update(self, ground_list):#allows gravity to work properly as well as collision with the ground
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y + self.move_y
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.move_y = 0
            self.rect.bottom = g.rect.top
        if len(ground_hit_list) == 0:
            self.is_falling = True
        if len(ground_hit_list) >= 1:
            self.is_falling = False
            self.move_y = 0

    def gravity(self): #gives a value to gravity
        if self.is_falling:
            self.move_y += .005

    def move(self,new_x,new_y):#makes enemy teleport to new location if necessary
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_right(self): #allows enemy to move right
        self.rect.x += .5

    def move_left(self): #allows enemy to move left
        self.rect.x -= .51