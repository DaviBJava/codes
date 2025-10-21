import pygame

# 1. Inicializando o Pygame
pygame.init()

# 2. Definindo as cores (estilo NEON)
# Usamos o padrão RGB (Red, Green, Blue)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CIANO_NEON = (0, 255, 255)
MAGENTA_NEON = (255, 0, 255)

# 3. Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Guerra de Naves Neon")

# 4. Loop Principal do Jogo
rodando = True
while rodando:
    # 5. Checando Eventos (ações do jogador)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Se o jogador clicar no 'X' da janela
            rodando = False


 
    # 6. Lógica do Jogo (ainda não temos)

    # 7. Desenho na tela
    tela.fill(PRETO) # Pinta o fundo de preto

    # 8. Atualizando a tela para mostrar o que foi desenhado
    pygame.display.flip()

# 9. Finalizando o Pygame
pygame.quit()