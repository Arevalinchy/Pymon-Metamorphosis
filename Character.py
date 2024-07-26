
import pygame

class Character:
    def __init__(self, attribiute,sprite):
        self.attribute = attribiute
        self.sprite = pygame.image.load(sprite)
        self.reversedSprite = pygame.transform.flip(self.sprite, True, False)
        self.health = 500
    def __str__(self):
        texto = "soy un {0}".format(self.attribute)
        return texto
    





    

        
