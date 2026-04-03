import pygame
pygame.init()

janela= pygame.display.set_mode((400,400))
pygame.display.set_caption("Campo Minado")

#Desenhar quadrados

CELULA = 50
for linha in range(8):
    for coluna in range(8):
        react = pygame.Rect(coluna*CELULA, linha*CELULA, CELULA, CELULA)
        pygame.draw.react(janela, (200,200,200), rect)

        pygame.draw.rect(janela(0,0,0), rect, 1)

#loop

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    pygame.display.flip()