# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:59:51 2020

@author: santi
"""

"Character select screen"

import pygame,sys
from pygame.locals import *

pygame.init()
size = width,height = 1920,1080



class Pollo:
    def __init__(self):
        self.atributo = "Pollo"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_POLLO1.png")
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
    


class Mago:
    def __init__(self):
        self.atributo = "Mago"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_MAGA1.png")
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
    
    
class Espada:
    def __init__(self):
        self.atributo = "Espada"
        self.imagen = pygame.image.load("IMAGENES/Seleccion_de_personajes/SPRITE_ESPADA.png")
    def __str__(self):
        texto = "soy un {0}".format(self.atributo)
        return texto
            
        
    

a = Pollo()
b = Mago()
c = Espada()
d = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco.png")
e = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco2.png")

a.imagen = pygame.transform.scale(a.imagen,(200,200))
b.imagen = pygame.transform.scale(b.imagen,(200,200))
c.imagen = pygame.transform.scale(c.imagen,(200,200))

fondo_select = pygame.image.load("IMAGENES/Seleccion_de_personajes/fondo2pix.png")


def characters():
    x1 = 145
    x2 = 145
    screen = pygame.display.set_mode(size)   
    selection = True
    selected = False 
    selected2 = False
    move = False
    while selection:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    selection = False
                elif event.key == K_BACKSPACE:
                    ss.Kirby()
                elif event.key == K_o:
                    selected = True
                elif event.key == K_p:
                    selected2 = True   
                elif event.key == K_d:
                    if selected == False:
                        if x1 == 685:
                            x1 = 145 
                        else:
                            x1 += 270
                elif event.key == K_a:
                    if selected == False:
                        if x1 == 145:
                            x1 = 685
                        else:
                            x1 -= 270
                elif event.key == K_RIGHT:
                    if selected2 == False:
                        if x2 == 685:
                            x2 = 145 
                        else:
                            x2 += 270
                elif event.key == K_LEFT:
                    if selected2 == False:
                        if x2 == 145:
                            x2 = 685
                        else:
                            x2 -= 270
                    
                    

        screen.blit(fondo_select, (0,0))                             
        screen.blit(d,(x1,235))
        screen.blit(e,(x2,235))
        screen.blit(a.imagen,(170,260))
        screen.blit(b.imagen,(440,260))
        screen.blit(c.imagen,(710,260))
        
        if selected and selected2:
            if x1 == 145:
                p1 = a
            elif x1 == 415:
                p1 = b
            elif x1 == 685:
                p1 = c
            if x2 == 145:
                p2 = a
            elif x2 == 415:
                p2 = b
            elif x2 == 685:
                p2 = c
            #test_3.battle(p1,p2)
            
            screen.fill((0,0,0))
            
            selected = False
            selected2 = False
            selection = False
            
            
            
        pygame.display.update()








        
   
    
   
