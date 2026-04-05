import pygame
import random
pygame.init()

#===============
# ⚒️Estrutura
#===============

CELULA = 50
LINHAS = 8
COLUNAS = 8

janela= pygame.display.set_mode((400,400))
pygame.display.set_caption("Campo Minado")

tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
revelado = [[False for _ in range(COLUNAS)] for _ in range(LINHAS)]

game_over = False

#======================
# ⚙️ Lógica do jogo
#======================

def gerar_bombas():
     quantidade_bombas = 10
     bombas_colocadas = 0

     while bombas_colocadas < quantidade_bombas:
        linha = random.randint(0, LINHAS - 1)
        coluna = random.randint(0, COLUNAS - 1)

        if tabuleir[linha][coluna] != -1:
            tabuleiro[linha][linha] = -1
            bombas_colocadas += 1

def revelar(linha, coluna):
    global game_over

    revelado[linha][coluna] = True
    print(f"Clicou em linha {linha}, coluna {coluna}")

    if tabuleiro[linha][coluna] == 1:
        game_over = True
        print("Bom!Você se explodiu!")


# 🎨Desenho do tabuleiro
#==========================


def desenhar(janela):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                rect = pygame.Rect(coluna * CELULA, linha * CELULA, CELULA, CELULA)
        
                if revelado[linha][coluna]:
                    pygame.draw.rect(janela, (100,180,255), rect)

                    if tabuleiro[linha][coluna] ==-1:
                        pygame.draw.circle(janela, (255,0,0), rect.center, 10)
                else:
                    pygame.draw.rect(janela, (200,200,200), rect)

                pygame.draw.rect(janela, (200,200,200), rect)
                pygame.draw.rect(janela, (0,0,0), rect, 1)

#==========
# 🔁loop
#==========


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
             x, y = evento.pos
             coluna = x // CELULA
             linha = y // CELULA

             revelar(linha, coluna)
             
      
    janela.fill((255,255,255))

    desenhar(janela)

    pygame.display.flip()
    
pygame.quit()
