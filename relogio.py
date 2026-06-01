import pygame


class Relogio:

    def __init__(self, *groups):
        super().__init__(*groups)
        self.tempo = 0

    def update(self, dt):

        self.tempo += dt

    def reset(self):

        self.tempo = 0