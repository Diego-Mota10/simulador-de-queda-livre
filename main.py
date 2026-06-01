import pygame
import planeta
import sys
import Maca
import relogio
import time

pygame.init()

tela = pygame.display.set_mode((1366,900))
fonte = pygame.font.SysFont("Arial", 40)

maca = Maca.Maca()
planeta = planeta.planeta()
Relogio = relogio.Relogio()
maca.caindo = False
gravidade = 0
inicio = 0
planetaAtual = "nao selecionado"
contagem = 0

clock = pygame.time.Clock()

while True:

    dt = clock.tick(60)/1000
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                maca.caindo = True
                Relogio.reset()
            if evento.key == pygame.K_1:
                gravidade = planeta.Mercurio
                planetaAtual = "Mercurio"
            if evento.key == pygame.K_2:
                gravidade = planeta.Venus
                planetaAtual = "Venus"
            if evento.key == pygame.K_3:
                gravidade = planeta.Terra
                planetaAtual = "Terra"
            if evento.key == pygame.K_4:
                gravidade = planeta.Lua
                planetaAtual = "Lua"
            if evento.key == pygame.K_5:
                gravidade = planeta.Marte
                planetaAtual = "Marte"
            if evento.key == pygame.K_6:
                gravidade = planeta.Jupiter
                planetaAtual = "Jupiter"
            if evento.key == pygame.K_7:
                gravidade = planeta.Saturno
                planetaAtual = "Saturno"
            if evento.key == pygame.K_8:
                gravidade = planeta.Urano
                planetaAtual = "Urano"
            if evento.key == pygame.K_9:
                gravidade = planeta.Netuno
                planetaAtual = "Netuno"
            if evento.key == pygame.K_0:
                gravidade = planeta.Sol
                planetaAtual = "Sol"
        
            
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
            
      
    maca.update(dt, gravidade)
    tela.fill((0,0,0))
    if maca.caindo:
        Relogio.update(dt)
        contagem = Relogio.tempo
    tela.blit(maca.image, maca.rect)
    texto = fonte.render(f"Planeta: {planetaAtual}", True, (255,255,255))
    tela.blit(texto, (50, 50))

    tempo = fonte.render(f"tempo: {contagem}", True, (255, 255, 255))
    tela.blit(tempo, (50, 300))
    pygame.display.update()
    