import pygame
from recursos.basicos import limparTela, aguarde
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man do Marcão")
relogio = pygame.time.Clock()
branco = (255, 255, 255)
preto = (0, 0, 0)
iron = pygame.image.load("assets/iron.png")
fundoJogo = pygame.image.load("assets/fundoJogo.png")

largura_iron = iron.get_width()
altura_iron = iron.get_height()

posicaoXIron = 275
posicaoYIron = 400
movimentoXIron = 0
movimentoYIron = 0
velocidadeIron = 10
while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
            movimentoXIron = -velocidadeIron  
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_d:
            movimentoXIron = velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_w:
            movimentoYIron = -velocidadeIron
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_s: 
            movimentoYIron = velocidadeIron
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_a:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_d:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_w:
            movimentoYIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_s:
            movimentoYIron = 0

    posicaoXIron = posicaoXIron + movimentoXIron
    posicaoYIron = posicaoYIron + movimentoYIron

    # Limitar a posição X do Iron Man
    if posicaoXIron < 0:
        posicaoXIron = False
    elif posicaoXIron + largura_iron > tamanho[0]:
        posicaoXIron = tamanho[0] - largura_iron

    # Limitar a posição Y do Iron Man
    if posicaoYIron < 0:
        posicaoYIron = False
    elif posicaoYIron + altura_iron > tamanho[1]:
        posicaoYIron = tamanho[1] - altura_iron
            
    
    posicaoXIron = posicaoXIron + movimentoXIron
    posicaoYIron = posicaoYIron + movimentoYIron
    tela.fill(branco)
    tela.blit(fundoJogo, (0,0))
    tela.blit(iron, (posicaoXIron,posicaoYIron))
    
    
    pygame.display.update()
    relogio.tick(60)
    
    