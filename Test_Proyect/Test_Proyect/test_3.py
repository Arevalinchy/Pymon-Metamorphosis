# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:37:46 2020

@author: Lonch
"""
import pygame, sys
from pygame.locals import *
pygame.init()

size = width,height = 1080,720


global x1
x1 = 450
global x2 
x2 = 450

def battle(player1, player2):

    screen = pygame.display.set_mode(size)
    a = pygame.image.load("Health_Bar.png")
    b = pygame.image.load("Health_Bar_2.png")
    c = pygame.image.load("health_Bar_3.png")
    d = pygame.image.load("Health_Bar_4.png")
    
    C1 = pygame.image.load("Controles_Q.png")
    C2 = pygame.image.load("Controles_W.png")
    C3 = pygame.image.load("Controles_E.png")
    C4 = pygame.image.load("Controles_R.png")
    
    C5 = pygame.image.load("Controles_U.png")
    C6 = pygame.image.load("Controles_I.png")
    C7 = pygame.image.load("Controles_O.png")
    C8 = pygame.image.load("Controles_P.png")
    

    prueba = False
    k = None
    l = None
    turno = True
    
    game_on = True
    action = False
    action2 = False
    while game_on:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                         

                    
        if x1 <= 0 or x2 <= 0:
            game_on = False  
            

        screen.fill((0,0,0))
        b = pygame.transform.scale(b,(x1,160))
        d = pygame.transform.scale(d,(x2,160))
        screen.blit(b, (51,100))
        screen.blit(a, (51,100))
        screen.blit(d, (591,100))
        screen.blit(c, (591,100))
        screen.blit(player1.imagen, (170,300))
        screen.blit(player2.imagen, (710,300))
        
        if turno:
        
            screen.blit(C1,(20,430))
            screen.blit(C2,(560,430))
            screen.blit(C3,(20,550))
            screen.blit(C4,(560,550))
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        l = 1        
                        turno = False
                    elif event.key == K_w:   
                       l = 2
                       turno = False                               
                    elif event.key == K_e:

                       l = 3
                       turno = False
                    elif event.key == K_r:
                       l = 4   
                       turno = False 
                
        
        if turno == False:
            
            screen.blit(C5,(20,430))
            screen.blit(C6,(560,430))
            screen.blit(C7,(20,550))
            screen.blit(C8,(560,550))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_u:  
                        k = 1
                        prueba = True
                    elif event.key == K_i:
                        k = 2
                        prueba = True
                    elif event.key ==K_o: 
                        k = 3
                        prueba = True
                    elif event.key == K_p:
                        k = 4 
                        prueba = True
            
            
        if prueba: 
            if k == 1 and l == 1:
                Special1(player1,player2)
                Special2(player1,player2)
                prueba = False
                turno = True
                k = None
            elif k == 1 and l == 2:
                Basic1()
                Special2(player1,player2)
                prueba = False
                turno = True
                k = None
            elif k == 1 and l == 3:
                Defence1()
                Special2(player1,player2)
                prueba = False
                turno = True
                k = None
            elif k == 1 and l == 4:
                Special2(player1,player2)
                prueba = False
                turno = True
                k = None
                
            elif k == 2 and l == 1:
                Special1(player1,player2)
                Basic2()
                prueba = False
                turno = True
                k = None
            elif k == 2 and l == 2:
                Basic1()
                Basic2()
                prueba = False
                turno = True
                k = None
            elif k == 2 and l == 3:
                Special2(player1,player2)
                Basic2()
                prueba = False
                turno = True
                k = None
            elif k == 2 and l == 4:
                Basic2()
                prueba = False
                turno = True
                k = None
                
            elif k == 3 and l == 1:
                Special1(player1,player2)
                Defence2()
                prueba = False
                turno = True
                k = None
            elif k == 3 and l == 2:
                Basico1()
                Defence2()
                prueba = False
                turno = True
                k = None
            elif k == 3 and l == 3:
                Defence2()
                Defence1()
                prueba = False
                turno = True
                k = None
            elif k == 3 and l == 4:
                Defence2()
                prueba = False
                turno = True
                k = None
                
            elif k == 4 and l == 1:
                Special1(player1,player2)
                prueba = False
                turno = True
                k = None
                l = None
            elif k == 4 and l == 2:
                Basico1()
                prueba = False
                turno = True
                k = None
            elif k == 4 and l == 3:
                Defence1()
                prueba = False
                turno = True
                k = None
            elif k == 4 and l == 4:
                prueba = False
                turno = True
                k = None





                
                        
          
            
            
            
            
            
        pygame.display.update()
   

                  
    while game_on == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                  pygame.quit()
                  sys.exit()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                    
        screen.fill((0,0,0))
        mytext = pygame.font.SysFont("Times New Roman", 200)
        mytext = mytext.render("Game Over", True, (200,0,0))
        screen.blit(mytext, (75,210))
        pygame.display.update()
        
    pygame.quit()              
                     
 
    
def Special1(player1,player2):
        global x1
        global x2
        if player1.atributo != player2.atributo:
            if player1.atributo == "Pollo":
                if player2.atributo == "Mago":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Espada":
                    x2 -=25
                    return x2
            elif player1.atributo == "Mago":
                if player2.atributo == "Espada":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Pollo":
                    x2 -= 25
                    return x2           
            elif player1.atributo == "Espada":
                if player2.atributo == "Pollo":
                    x2 -= 50
                    return x2
                elif player2.atributo == "Mago":
                    x2 -=25
                    return x2
        elif player1.atributo == player2.atributo:
            x2 -= 25
            return x2
          

   
        
def Special2(player1,player2):
          global x1
          global x2
          if player2.atributo != player1.atributo:
            if player2.atributo == "Pollo":
                if player1.atributo == "Mago":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Espada":
                    x1 -=25
                    return x1
            elif player2.atributo == "Mago":
                if player1.atributo == "Espada":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Pollo":
                    x1 -= 25  
                    return x1                              
            elif player2.atributo == "Espada":
                if player1.atributo == "Pollo":
                    x1 -= 50
                    return x1
                elif player1.atributo == "Mago":
                    x1 -=25
                    return x1
          elif player2.atributo == player1.atributo:
                 x1 -= 25
                 return x1
    
    
    
    
    
def Basic1():
    global x2
    x2 -= 37
    return x2
    
def Basic2():
    global x1
    x1 -= 37
    return x1    



def Defence1():
    global x1
    x1 +=25
    return x1

def Defence2():
    global x2
    x2 +=25
    return x2




def Accion(result1,result2):
    return "e"






      
    
    
 