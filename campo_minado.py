import pygame
pygame.init()

# Estrutura

CELULA = 50
LINHAS = 8
COLUNAS = 8

janela= pygame.display.set_mode((400,400))
pygame.display.set_caption("Campo Minado")

tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
revelado = [[False for _ in range(COLUNAS)] for _ in range(LINHAS)]

# Desenho do tabuleiro

def desenhar(janela):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                rect = pygame.Rect(coluna * CELULA, linha * CELULA, CELULA, CELULA)
        
                pygame.draw.rect(janela, (200,200,200), rect)
                pygame.draw.rect(janela, (0,0,0), rect, 1)

#loop

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((255,255,255))

    desenhar(janela)

    pygame.display.flip()
    
pygame.quit()
