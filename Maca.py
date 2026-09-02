import math
import pygame
import os

caminho = os.path.join(os.path.dirname(__file__), 'maca.png')

class Maca(pygame.sprite.Sprite):
    

    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.posy = 0
        self.vely = 0
        self.acely = 0
        self.caiu = False
        #Vairiaveis de movimento
        
        
        self.sprits=[]
        self.sprits.append(pygame.image.load(caminho))
        self.image = self.sprits[0]
        #A maca vira um sprit
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (30,30))
        
        '''posicao inicial da maca'''
        self.rect.x = 850
        self.rect.y = 0
        
    
    def movimento(self, dt):
        self.vely += self.acely * dt
        self.posy += self.vely * dt
        self.rect.y = int(self.posy) #a posicao em y deve sempre ser um inteiro, os pixels são discretos
        
        '''Usa dt para escrever a funcao horaria da velocidade e da posicao da maca'''
        

    
    def queda(self, gravidade):
        if self.caindo:
            self.acely = gravidade #gravidade ligada
        if self.rect.y > 800:
            self.caindo = False #gravidade desligada
            self.acely = 0
            self.rect.y = 0
            self.vely = 0
            self.posy = 0
        
        '''avisa que a maca comecou a cair, e quando chega ao final da tela retorna as condicoes iniciais'''
            
            
    
    def update(self, dt, gravidade):
        self.queda(gravidade)
        self.movimento(dt)
        
        '''atualiza o movimento da maca'''
        