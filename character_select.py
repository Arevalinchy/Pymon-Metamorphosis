# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:59:51 2020

@author: santi
"""

"Character select screen"

import pygame,sys
from pygame.locals import *
import time
import Game
from Character import Character  

pygame.init()
        
    
#CLASES (TIPOS DE PERSONAJE)
pollo = Character("Pollo", "IMAGENES/Seleccion_de_personajes/SPRITE_POLLO1.png", "Espada")
mago = Character("Mago","IMAGENES/Seleccion_de_personajes/SPRITE_MAGA3.png","Pollo")
espada = Character("Espada", "IMAGENES/Seleccion_de_personajes/SPRITE_ESPADA.png","Mago")

#MARCOS PARA ELEGIR PERSONAJE
m_azul = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_Azul.png")
m_azul_chs = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_Azul_chs.png")

m_verde = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_verde.png")
m_verde_chs = pygame.image.load("IMAGENES/Seleccion_de_personajes/Marco_verde_chs.png")


#Character Sprites Scale
pollo.sprite = pygame.transform.scale(pollo.sprite,(300,300))
pollo.reversedSprite = pygame.transform.scale(pollo.reversedSprite,(300,300))

mago.sprite = pygame.transform.scale(mago.sprite,(300,300))
mago.reversedSprite = pygame.transform.scale(mago.reversedSprite,(300,300))

espada.sprite = pygame.transform.scale(espada.sprite,(300,300))
espada.reversedSprite = pygame.transform.scale(espada   .reversedSprite,(300,300))


m_azul = pygame.transform.scale(m_azul ,(300,300))
m_azul_chs = pygame.transform.scale(m_azul_chs,(300,300))
m_azul_chs.set_alpha(0)

m_verde = pygame.transform.scale(m_verde ,(300,300))
m_verde_chs = pygame.transform.scale(m_verde_chs ,(300,300))
m_verde_chs.set_alpha(0)

#SONIDOS
click_character = pygame.mixer.Sound("Sonidos/seleccion_char.wav")

esc_sound = pygame.mixer.Sound("Sonidos/esc_sound.mp3")



fondo_select = pygame.image.load("IMAGENES/Seleccion_de_personajes/fondo2pix.png")


def characters(screen):
    
    x1 = 380
    x2 = 380

    selection = True
    selected = False 
    selected2 = False
    
    
    while selection:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(esc_sound)
                    selection = False
                    
                elif event.key == K_e:
                    selected = True
                    m_azul.set_alpha(0)                
                    m_azul_chs.set_alpha(255)
                    pygame.mixer.Sound.play(click_character)

                elif event.key == K_p:
                    selected2 = True  
                    m_verde.set_alpha(0)                
                    m_verde_chs.set_alpha(255)
                    pygame.mixer.Sound.play(click_character)
                    
                elif event.key == K_d:
                    if selected == False:
                        if x1 == 1260:
                            x1 = 380 
                        else:
                            x1 += 440
                elif event.key == K_a:
                    if selected == False:
                        if x1 == 380:
                            x1 = 1260
                        else:
                            x1 -= 440
                elif event.key == K_RIGHT:
                    if selected2 == False:
                        if x2 == 1260:
                            x2 = 380 
                        else:
                            x2 += 440
                elif event.key == K_LEFT:
                    if selected2 == False:
                        if x2 == 380:
                            x2 = 1260
                        else:
                            x2 -= 440
                    
                    

        screen.blit(fondo_select, (0,0))  
                           
        screen.blit(m_azul,(x1,328))        
        screen.blit(m_azul_chs,(x1,328))
        
        screen.blit(m_verde,(x2,328))
        screen.blit(m_verde_chs,(x2,328))
        

    
        screen.blit(pollo.sprite,(380,340))
        screen.blit(mago.sprite,(820,366))
        screen.blit(espada.sprite,(1260,310))
        
        if selected and selected2:
            if x1 == 380:
                p1 = pollo
            elif x1 == 820:
                p1 = mago
            elif x1 == 1260:
                p1 = espada
            if x2 == 380:
                p2 = pollo
            elif x2 == 820:
                p2 = mago
            elif x2 == 1260:
                p2 = espada
                
                
            Game.battle(p1,p2, screen)
            
            screen.fill((0,0,0))
            
            selected = False
            selected2 = False
            selection = False
        
    
            
        pygame.display.update()






        
   
    
   
