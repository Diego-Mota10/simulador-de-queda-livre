import math
import pygame
import os

caminho = os.path.join(os.path.dirname(__file__), 'maca.png')

class Maca(pygame.sprite.Sprite):
    

    
    def __init__(self, *groups):
        super().__init__(*groups)
        self.posy_inicial = 0
        self.posy = 0
        self.vely_inicial = 0
        self.vely = 0
        self.acely = 0
        self.caiu = False
        
        
        self.sprits=[]
        self.sprits.append(pygame.image.load(caminho))
        self.image = self.sprits[0]
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect.x = 650
        self.rect.y = self.posy_inicial
    
    def movimento(self, dt):
        self.vely += self.acely * dt
        self.posy += self.vely * dt
        self.rect.y = int(self.posy)

    
    def queda(self, gravidade):
        if self.caindo:
            self.acely = gravidade
        if self.rect.y > 700:
            self.caiu = True
            self.caindo = False
            self.acely = 0
            self.rect.y = 0
            self.vely = 0
            self.posy = 0
            
    
    def update(self, dt, gravidade):
        self.queda(gravidade)
        self.caiu = False
        self.movimento(dt)