
import pygame

class Character:
    def __init__(self, attribiute,sprite, weakness):
        self.attribute = attribiute
        self.sprite = pygame.image.load(sprite)
        self.reversedSprite = pygame.transform.flip(self.sprite, True, False)
        self.weakness = weakness
        self.health = 500
    def __str__(self):
        texto = "soy un {0}".format(self.attribute)
        return texto
"""
class Pollo(Character):
    def __init__(self):
        super().__init__("Pollo", "IMAGENES/Seleccion_de_personajes/SPRITE_POLLO1.png")
        self.weeknes = "Espada"

    
class Mago(Character):
    def __init__(self):
        super().__init__("Mago", "IMAGENES/Seleccion_de_personajes/SPRITE_MAGA3.png")
        self.weeknes = "Pollo"
    

class Espada(Character):
    def __init__(self):
        super().__init__("Espada", "IMAGENES/Seleccion_de_personajes/SPRITE_ESPADA.png")
        self.weeknes = "Mago"

"""    



    

        
