import pygame as py
from random import randint

class Bag(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = py.image.load("pngwing.com.png")
        self.image = py.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(x=0, y=520)

    def update(self):
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            self.rect.x = self.rect.x - 1.5
        if keys[py.K_RIGHT]:
            self.rect.x = self.rect.x + 1.5



class Cherep(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = py.image.load("ddd.png")
        self.image = py.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.y = randint(-1000, -10)
        self.rect.x = randint(0, 600)
    def update(self):
        self.rect.y += 1