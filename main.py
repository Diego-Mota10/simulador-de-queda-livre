import pygame
import planeta
import sys
import Maca
import relogio

pygame.init()

tela = pygame.display.set_mode((1366,900))
fonte = pygame.font.SysFont("Arial", 40)
fonte_informe = pygame.font.SysFont("Arial", 20)
'''A altura inicial é de 2 metros'''



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

    dt = clock.tick(120)/1000
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and planetaAtual != "nao selecionado":
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
    tela.fill((0, 30, 0))
    informes = fonte_informe.render(f"A altura inicial é de 2 metros", True, (255,255,255))
    tela.blit(informes, (50, 780))
    informes2 = fonte_informe.render(f"Selecione o planeta com os botões de 0 a 9 e pressione espaço", True, (255,255,255))
    tela.blit(informes2, (50, 800))
    if maca.caindo:
        Relogio.update(dt)
        contagem = Relogio.tempo
    tela.blit(maca.image, maca.rect)
    texto = fonte.render(f"Planeta: {planetaAtual}", True, (255,255,255))
    tela.blit(texto, (50, 50))


    tempo = fonte.render(f"Tempo: {contagem:.2f}", True, (255, 255, 255))
    tela.blit(tempo, (50, 100))
    pygame.display.update()
    