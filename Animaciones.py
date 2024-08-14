# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 04:59:58 2020

@author: santi
"""

import sys, pygame
from pygame.locals import *
pygame.init()

#importa el "asset" de burbuja para la animacion de defensa
escudo1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Escudo.png")
escudo1 = pygame.transform.scale(escudo1, (350,350))

escudo2 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Escudo.png")
escudo2 = pygame.transform.scale(escudo2, (350,350))

#FONDOS
fondo_pelea = pygame.image.load("IMAGENES/Fondo_Pelea.png")

#TEXTO
mytext = pygame.font.Font("FUENTES/fuente1.ttf", 50) #Importa las fuente de los textos

#SONIDOS
congratulations = pygame.mixer.Sound("Sonidos/congratulations1.mp3")
chance_time = pygame.mixer.Sound("Sonidos/chance_time1.mp3")
golpe = pygame.mixer.Sound("Sonidos/golpe_sonido1.mp3")


#Animación del ataque especial o básico cuando el jugador 1 elige la opción
def AtaqueS1(player1,player2,a,b,c,d,corazon,corazon2,n,n2, screen):
    #Recibe los dos objetos, las barras de vida y las opciones de cada personaje como argumento de entrada. 
    speed = 550  #Velocidad del personaje
    y = 1 #Variable usada para determinar la duracion de la función 


    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Toma la imagen jugador 1 y lo mueve hasta el jugador 2 y luego lo devuelve  a
        #la poscicion inicial
        screen.blit(fondo_pelea, (0,0))
        
        
        screen.blit(player1.sprite,(speed,370))
        screen.blit(player2.reversedSprite,(1340,360))

        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(n, (330,470))   #LO QUE ELIGIO CADA JUAGDOR
        screen.blit(n2, (920,470))

        if y == 1:
            speed += 40 
        if speed >= 1340: 
            pygame.mixer.Sound.play(golpe)
            player1.sprite = pygame.transform.flip(player1.sprite, True, False)
            y = 0   
        if y == 0: 
            speed -= 40
        if speed < 550 and y == 0: 
            player1.sprite = pygame.transform.flip(player1.sprite, True, False)
            ok = False
        
        pygame.display.update() 


def AtaqueS2(player1,player2,a,b,c,d,corazon,corazon2,n,n2, screen):
    #Recibe los dos objetos, las barras de vida y 
    #las opciones de cada personaje como argumento de 
    #entrada.

    speed = 1340 #Velocidad del personaje
    y = 1 #Variable usada para determinar la duracion de la función 


    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
      #Toma la imagen jugador 2 y lo mueve hasta el jugador 1 y luego lo devuelve  a
      # la poscicion inicial
        screen.blit(fondo_pelea, (0,0))
         
        screen.blit(player2.reversedSprite,(speed,360))
        screen.blit(player1.sprite,(550, 370))

        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(n, (330,470))
        screen.blit(n2, (920,470))

        if y == 1:
            speed -= 40 
        if speed <= 550: 
            pygame.mixer.Sound.play(golpe)
            player2.reversedSprite = pygame.transform.flip(player2.reversedSprite, True, False)
            y = 0   
        if y == 0: 
            speed += 40
        if speed > 1340 and y == 0: 
            player2.reversedSprite = pygame.transform.flip(player2.reversedSprite, True, False)
            ok = False
        
        pygame.display.update() 
        
        
        
#Funcioón cuando el jugador 1 elige defensa y el 2 ataque        
def Defensa1(player1,player2,a,b,c,d,corazon,corazon2,n,n2, screen): #Recibe los dos objetos, las barras de vida y 
                                           #las opciones de cada personaje como argumento de 
                                           #entrada.
    #p2 ataca

    speed = 1340 #Velocidad del personaje 
    y = 1 #Variable usada para determinar la duracion de la función 


    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #Funciona como las funciones de ataque, pero 
        #le coloca el ecudo a quien halla elejido defensa
        screen.blit(fondo_pelea, (0,0))
        
        screen.blit(player2.reversedSprite,(speed,360))
        screen.blit(player1.sprite,(550, 370))

        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(escudo1,(535, 350))   #ESCUDO EN EL JUGADOR 1
        
        screen.blit(n, (330,470))
        screen.blit(n2, (920,470))

        if y == 1:
            speed -= 40 
        if speed <= 550: 
            player2.reversedSprite = pygame.transform.flip(player2.reversedSprite, True, False)
            y = 0
        if y == 0: 
            speed += 40 
        if speed > 1340 and y == 0: 
            player2.reversedSprite = pygame.transform.flip(player2.reversedSprite, True, False)
            ok = False
        
        pygame.display.update() 
    
    

#Funcioón cuando el jugador 2 elige defensa y el 1 ataque 
def Defensa2(player1,player2,a,b,c,d,corazon,corazon2,n,n2, screen): #Recibe los dos objetos, las barras de vida y 
                                           #las opciones de cada personaje como argumento de 
                                           #entrada.
    #p1 ataca 

    speed = 550 #Velocidad del personaje
    y = 1 #Variable usada para determinar la duracion de la función 


    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


  
        #Funciona como las funciones de ataque, pero 
        #le coloca el ecudo a quien halla elejido defensa
        screen.blit(fondo_pelea, (0,0)) 
        
        screen.blit(player1.sprite,(speed,370))
        screen.blit(player2.reversedSprite,(1340,360))
        
        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(escudo1,(1325,340))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(n, (330,470))
        screen.blit(n2, (920,470))

        if y == 1:
            speed += 40 
        if speed >= 1340: 
            player1.sprite = pygame.transform.flip(player1.sprite, True, False)
            y = 0   
        if y == 0: 
            speed -= 40
        if speed < 550 and y == 0: 
            player1.sprite = pygame.transform.flip(player1.sprite, True, False)
            ok = False
        
        pygame.display.update() 
    

#Funcion para cuando ambos elijen defensa 
def Defensa3(player1,player2,a,b,c,d,corazon,corazon2,n,n2, screen):
    #Recibe los dos objetos, las barras de vida y 
    #las opciones de cada personaje como argumento de 
    #entrada.

    y = 1 #Variable usada para determinar la duracion de la función 


    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         #Coloca el escudo a ambos jugadores
        screen.blit(fondo_pelea, (0,0))
        
        screen.blit(player1.sprite,(550, 370))
        screen.blit(player2.reversedSprite,(1340,360))
        
        #Escudo en los jugadores
        screen.blit(escudo1,(535, 350))
        screen.blit(escudo2,(1325,340))
        
        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(n, (330,470))
        screen.blit(n2, (920,470))


        
        y += 1
        if y == 100:
            ok = False
            
        pygame.display.update()
        
    
#Cuando alguien elige chance time    
def Defensa4(player1,player2,a,b,c,d,corazon,corazon2,n,n2,A2,A1,screen):
    #Recibe los dos objetos, las barras de vida y 
    #las opciones y el valor de la opcion de cada personaje  
    #como argumento de entrada.

     
    y = 1 #Variable usada para determinar la duracion de la función 
    if A2 == 4:  #Utiliza las variablea A1 y A2 para determinar quien lleva el escudo
        x = 535
    elif A1 == 4:
        x = 1325
    ok = True
    while ok:   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
         
        screen.blit(fondo_pelea, (0,0))
        
        screen.blit(player1.sprite,(550, 370))
        screen.blit(player2.reversedSprite,(1340,360))
        
        screen.blit(escudo1,(x,345))
        
        screen.blit(a, (51,100)) #se muestran barras de vida 
        screen.blit(b, (51,100))
        screen.blit(c, (1391,100))
        screen.blit(d, (1391,100))
        
        screen.blit(corazon, (51,100))
        screen.blit(corazon2, (1391,100))
        
        screen.blit(n, (330,470))
        screen.blit(n2, (920,470))
        


        
        y += 1
        if y == 100: #Al llegar a 100 finaliza la función. 
            ok = False
            
        pygame.display.update()
        


#Cuando ambos elijen Chance Time
def ChanceTimeA(player1,player2,num, screen): #Recibe los objetos y un numero aleatorio como argumento
                
        y = 0 #Variable usada para determinar la duracion de la función 
        
        
        Titulo = mytext.render("Chance Time", True, (0,0,200)) #Indica que entraron a Chance Time
        good1 = mytext.render("Receved HP", True, (0,200,0)) #Indica que alguno recibe vida
        good2 = mytext.render("Receved Damage", True, (200,0,0)) #Indica que alguno recibe daño
        bad = mytext.render("No Changes", True, (0,0,200)) #Indica que alguno no hubo cambios
        
        ok = True #Permite que funcione el while 
        while ok:
            y += 1 #Empieza a aumentar la variable 
 
            screen.fill((0,0,0))
            screen.blit(Titulo,(75,50))
            
            screen.blit(player1.sprite, (170,200))
            screen.blit(player2.sprite, (170,740))
                
            if y > 400 and y < 800: #Rota rapidamente entre los dos textos para dale un efecto de suspenso 
                
                pygame.mixer.Sound.play(chance_time)
                
                if y%2 == 1:
                    screen.blit(good1, (410,300))

                elif y%2 == 0: 
                    screen.blit(good2, (410,840))
                                    
            elif y > 800:  #Muestra el resultado según el numero aleatorio que se obtiene previamente 
                               
                if num == 1:
                    screen.blit(good1, (410,300))
                elif num == 2:
                    screen.blit(good2, (410,840))
                    
                elif num == 5: 
                    screen.blit(good1,(410,840))
                elif num == 6:
                    screen.blit(good2, (410,300))
                    
                else:
                    screen.blit(bad,(860, 360))
                  
            if y == 1200: #Cuando se alcanza 1200, la función finaliza
                ok = False 
                 
            pygame.display.update()
                
                
    

#Pantalla final 
def finito(player1,player2,screen): #Toma los objetos y sus valores de x de cada personaje

        pygame.mixer.Sound.play(congratulations)

        
        y = 0  #Variable usada para determinar la duracion de la función 
        
        mytext = pygame.font.Font("FUENTES/fuente1.ttf", 50)
        good1 = mytext.render("GANASTE!!!", True, (255, 255, 255))
        
        ok = True #Variable que perimte el while 
        while ok:
                y += 1
                screen.blit(fondo_pelea, (0,0)) 
                if player1.health > player2.health:
                    screen.blit(player1.sprite,(860,440))
                    screen.blit(good1,(150,130))
                    
                elif player1.health < player2.health:
                    screen.blit(player2.sprite,(860,440))  
                    screen.blit(good1,(150,130))

                if y == 800:
                        ok = False
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
                        
                pygame.display.update()
                
        
                
    










