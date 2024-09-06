
import pygame # type: ignore

class Character:
    def __init__(self, attribute,sprite, weakness):
        self.attribute = attribute
        self.sprite = pygame.image.load(sprite)
        self.reversedSprite = pygame.transform.flip(self.sprite, True, False)
        self.lifeContainerSprite = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_roja_1.png")
        self.lifeBarSprite = pygame.image.load("IMAGENES/Elementos_Juego_Prueba/Barra_vida_verde_1.png")
        self.weakness = weakness
        self.health = 500
    def __str__(self):
        texto = "soy un {0}".format(self.attribute)
        return texto
    

#---------------State Machine For Trun Battle System--------------------#
class State:
    def enter():
        pass
    def exit():
        pass
    def input(event):
        pass

    def update(character):
        pass

class AnimationState(State):

    def enter():
        #going to character attack animation
        pass

    def exit():
        #going back from attack animation
        pass
    def input(event):
        print("hola")
        return playerTurnState

    def update(character):
        return playerTurnState



class playerTurnState(State):

    def __init__(self):
        self.sound = pygame.mixer.Sound("Sonidos/seleccion_ataque.wav")

    def enter():
        #going to character attack animation
        pass

    def exit():
        #going back from attack animation
        pass
    def input(self,event):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:    #Elije el ataque especial 
                    A1 = 1                   
                elif event.key == pygame.K_w:   #Elije el ataque básico 
                    A1 = 2                        
                elif event.key == pygame.K_e:  #Elije defensa
                    A1 = 3                      
                elif event.key == pygame.K_r:   #Elije Chance time 
                    A1 = 4   
                pygame.mixer.Sound.play(self.sound)

        return 
                 
    def update(character):
        character.health -= 1

class Player:
    active_state = playerTurnState()
   
    def __init__(self, attribute,sprite, weakness):
        self.character = Character(attribute,sprite, weakness)
    #    super().__init__(attribute, sprite, weakness)

    def changingState(self,new_state):
        self.active_state.exit()
        self.active_state = new_state
        self.active_state.enter()

    def input(self,event):
        new_state = self.active_state.input(event)
        if new_state:
            self.active_state = new_state

    def update(self,character):
        new_state = self.active_state.update(character)
        if new_state:
            self.active_state = new_state




