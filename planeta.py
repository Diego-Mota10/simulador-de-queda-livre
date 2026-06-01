import math
import pygame
import os
tamanho = 400

'''a maca tem 30 px de altura, assumindo que a altura média de uma maca seja de 7,5 cm , posso assumir que 400 px valem por 1 metro'''

class planeta():
    
    

    def __init__(self, *groups):
        self.Terra = 9.8066 * tamanho
        self.Lua = 1.62 * tamanho
        self.Mercurio = 3.7030 * tamanho
        self.Venus = 8.8720 * tamanho
        self.Marte = 3.7210 * tamanho
        self.Jupiter = 24.79 * tamanho
        self.Saturno = 10.44 * tamanho
        self.Urano = 8.6999 * tamanho
        self.Netuno = 11.15 * tamanho
        self.Sol = 274 * tamanho
        
        super().__init__(*groups)
        
    