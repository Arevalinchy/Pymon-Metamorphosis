# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:37:46 2020

@author: santi
"""
from curses import KEY_DOWN
from json.encoder import ESCAPE
from termios import CQUIT
import pygame, sys, Animaciones,random # type: ignore
from pygame.locals import * # type: ignore
pygame.init()


def battle(player1, player2, screen): #Se define la funcion que tiene todo el juego con dos argumentos de entrada
                              #Los argumentos son objetos siendo los personajes de ambos jugadoes 
 
    
    #Imagenes que demarcan las opciones/controles del jugador 1
    C_1 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_Q.png")
    C1 = pygame.transform.scale(C_1, (700, 600))
    
    C_2 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_W.png")
    C2 = pygame.transform.scale(C_2, (700, 600))
    
    C_3 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_E.png")
    C3 = pygame.transform.scale(C_3, (700, 600))
    
    C_4 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_R.png")
    C4 = pygame.transform.scale(C_4, (700, 600))
    
    
    #Imagenes que demarcan las opciones/controles del jugador 2   
    C_5 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_U.png")
    C5 = pygame.transform.scale(C_5, (700, 600))
    
    C_6 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_I.png")
    C6 = pygame.transform.scale(C_6, (700, 600))
    
    C_7 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_O.png")
    C7 = pygame.transform.scale(C_7, (700, 600))
    
    C_8 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Boton_P.png")
    C8 = pygame.transform.scale(C_8, (700, 600))
    
    #SONIDOS
    botton_ataque = pygame.mixer.Sound("Sonidos/seleccion_ataque.wav")
    
    
    #FONDO DEL JUEGO
    fondo_pelea = pygame.image.load("IMAGENES/Fondo_Pelea.png")
    
    #Texto
    letra_jugadores = pygame.font.Font("FUENTES/fuente1.ttf", 25)
    
    #Variables para determinar el turno de los jugadores y las acciones que se hacen en respestivo turno 
    turno = True  
    pelea = False

    #Variable que reciben las opciones de cada jugador
    A1 = None
    A2 = None
    
    #Variable que mantiene el juego en movimiento
    game_on = True
    

    barraVidaBackgroundP1 = player1.lifeContainerSprite
    barraVidaForegroundP1 = player1.lifeBarSprite
    barraVidaBackgroundP2 = player2.lifeContainerSprite
    barraVidaForegroundP2 = player2.lifeBarSprite
            
    corazon = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Corazon_1.png")
    corazon2 = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Corazon_1.png")
    while game_on: 
        
        #Eventos 
        for event in pygame.event.get():
            if event.type == CQUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEY_DOWN:
                if event.key == ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        #End of the game
        # It takes players health to determine the state.                 
        if player1.health <= 100 or player2.health <= 100: 
            game_on = False  
                  
          
        screen.blit(fondo_pelea, (0,0))  #Rendering background   
        
        barraVidaForegroundP1 = pygame.transform.scale(barraVidaForegroundP1,(player1.health,100)) #Esta es la barra que decrece cada ves que alguno pierde vida 
        barraVidaForegroundP2 = pygame.transform.scale(barraVidaForegroundP2,(player2.health,100)) 
                
        #Renders Player 1 and its life bar       
        screen.blits(((player1.sprite, (550, 370)) ,(barraVidaBackgroundP1, (51,100)),(barraVidaForegroundP1, (51,100)), (corazon, (51,100)) ))

        #Renders Player 2 and its life bar
        screen.blits(((player2.reversedSprite, (1340,360)), (barraVidaBackgroundP2, (1391,100)),(barraVidaForegroundP2, (1391,100)) , (corazon2, (1391,100))))
    
        
        if turno: #Turno del jugador 1
        
            jugador1 = letra_jugadores.render("Turno del jugador 1", True, (255, 255, 255))
            screen.blit(jugador1, (25,25))
        
            #Renders all the P1's attacks
            screen.blits(((C1,(360,470)), (C2,(800,470)), (C3,(360,650)),(C4,(800,650)) ))
            
            
            #Eventos de jugador 1, el programa verifica si se ha oprimido alguna tecla 
            #Cuando elige cualquier opción, habilita el turno del siguiente jugador y asigna un valor a A1
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:    #Elije el ataque especial 
                        A1 = 1                   
                    elif event.key == K_w:   #Elije el ataque básico 
                        A1 = 2                        
                    elif event.key == K_e:  #Elije defensa
                        A1 = 3                      
                    elif event.key == K_r:   #Elije Chance time 
                        A1 = 4   
                    pygame.mixer.Sound.play(botton_ataque)
                    turno = False 

            
        
        if not turno: #Turno del jugador 2

        
            jugador2 = letra_jugadores.render("Turno del jugador 2", True, (255, 255, 255))
            screen.blit(jugador2, (1350,25))
            
            #Renders all the P2's attacks
            screen.blits(((C5,(360,470)), (C6,(800,470)), (C7,(360,650)),(C8,(800,650)) ))
             
            #Eventos de jugador 2, el programa verifica si se ha oprimido alguna tecla 
            #Cuando elige cualquier opción, habilita la animacion de ataque y asigna un valor a A2
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_u:  #Elije el ataque especial 
                        A2 = 1
                    elif event.key == K_i: #Elije el ataque básico 
                        A2 = 2
                    elif event.key ==K_o:  #Elije defensa
                        A2 = 3                        
                    elif event.key == K_p: #Elije Chance time 
                        A2 = 4 
                    pygame.mixer.Sound.play(botton_ataque)
                    pelea = True


        if pelea: #Turno del jugador 2  
            if A2 == 1 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C5,screen) #Cada bloque es similar, invocan las funciones relacionadas
                Special(player1,player2)                      #con las desiciones de cada jugado, luego se reinician cada variable
                
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C5,screen) #para que vuelva a repetirse cada proceso.
                Special(player2,player1)
    
            elif A2 == 1 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C5,screen)
                Basic(player2)
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C5,screen)
                Special(player2,player1)
            
            elif A2 == 1 and A1 == 3:
                Animaciones.Defensa1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C3,C5,screen)
                Defence(player1)
            
            elif A2 == 1 and A1 == 4:
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C4,C5,screen)
                Special(player2,player1)
                pelea = False
            
            elif A2 == 2 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C6,screen)
                Special(player1,player2)
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C6,screen)
                Basic(player1)                
            
            elif A2 == 2 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C6,screen)
                Basic(player2)
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C6,screen)
                Basic(player1)
            
            elif A2 == 2 and A1 == 3:
                Animaciones.Defensa1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C3,C6,screen)
                Defence(player1)
            
            elif A2 == 2 and A1 == 4:
                Animaciones.AtaqueS2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C4,C6,screen)
                Basic(player1)
            
            elif A2 == 3 and A1 == 1:
                Animaciones.Defensa2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C7,screen)
                Defence(player2)

            elif A2 == 3 and A1 == 2:
                Animaciones.Defensa2(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C7,screen)
                Defence(player2)

            elif A2 == 3 and A1 == 3:
                Animaciones.Defensa3(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C3,C7,screen)
                Defence(player1)
                Defence(player2)

            elif A2 == 3 and A1 == 4:
                Animaciones.Defensa4(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C4,C7,A2,A1,screen)
                Defence(player2)

            elif A2 == 4 and A1 == 1:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C1,C8,screen)
                Special(player1,player2)

            elif A2 == 4 and A1 == 2:
                Animaciones.AtaqueS1(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C2,C8,screen)
                Basic(player2)
                
            elif A2 == 4 and A1 == 3:
                Animaciones.Defensa4(player1,player2,barraVidaBackgroundP1,barraVidaForegroundP1,barraVidaBackgroundP2,barraVidaForegroundP2,corazon,corazon2,C3,C8, A2,A1,screen)
                Defence(player1)

            elif A2 == 4 and A1 == 4:
                num = random.randrange(1,8,1) #Genera el numero aleatorio para el chance time
                ChanceTime(num,player1,player2)
                Animaciones.ChanceTimeA(player1,player2,num,screen)
            

            pelea = False
            turno = True
            A1 = None
            A2 = None
            
        pygame.display.update()
   

                  
    while game_on == False:  #Pantalla final del juego, simplemente muestra "Game Over" y se sale del codigo cuando se oprime alguna de las opciones
        
        Animaciones.finito(player1,player2,screen)
        
    pygame.quit()              
                     
 
    
def Special(player1,player2): #Función que retorna el resultado de vida del jugador 2 cuando el juegador 1 elije el ataque especial.
        #Compara los atributos de ambos objetos 

        if player1.attribute == player2.weakness:
            player2.health -= 50
        else:
            player2.health -=25
          

   
       
#Funciones que retorna el resultado del daño cuando alguno de los personajes eljie el ataque básico     
def Basic(player): 
    player.health -= 37
 

#Funciones que retorna el resultado del daño cuando alguno de los personajes eljie defensa  
def Defence(player):
    player.health += 0


#Funciones que retorna un efecto aleatorio para alguno de los personajes 
#recibe un numero aleatorio como argumento
def ChanceTime(num, player1,player2):    
    if num ==1:   
        if player1.health > 380 and player1.health <= 450:
            player1.health += 50
        elif player1.health <= 380:
            player1.health += 120            
    elif num == 2:
        player2.health -= 120
    elif num == 5:
        if player2.health > 380 and player2.health <= 450:
            player2.health += 50
        elif player2.health <= 380:
            player2.health += 120
    elif num == 6:
        player1.health -= 120
    
    return num
        

