import pygame

# Inicializando o Pygame
pygame.init()

# Definindo as cores (estilo NEON)
PRETO = (0, 0, 0)
CIANO_NEON = (0, 255, 255)
MAGENTA_NEON = (255, 0, 255)
VERDE_NEON = (57, 255, 20)

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Guerra de Naves Neon")

# --- Configurações do Jogador ---
largura_jogador = 50
altura_jogador = 30
jogador_rect = pygame.Rect(largura / 2 - largura_jogador / 2, altura - altura_jogador - 10, largura_jogador, 
                           altura_jogador)
velocidade_jogador = 7

# --- Configurações dos Tiros ---
tiros = []
velocidade_tiro = 7

# Para controlar a taxa de quadros (FPS)
relogio = pygame.time.Clock()

# Loop Principal do Jogo
rodando = True
while rodando:
    # Garante que o jogo rode a no máximo 60 quadros por segundo
    relogio.tick(60)

    # Checando Eventos (ações do jogador)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tiro_rect = pygame.Rect(jogador_rect.centerx - 2, jogador_rect.top, 4, 10)
                tiros.append(tiro_rect)

    # --- Lógica do Jogo ---
    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_rect.left > 0:
        jogador_rect.x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_rect.right < largura:
        jogador_rect.x += velocidade_jogador

    # Movimenta os tiros
    for tiro in tiros[:]:
        tiro.y -= velocidade_tiro
        if tiro.bottom < 0:
            tiros.remove(tiro)

    # --- Desenho na tela ---
    tela.fill(PRETO)
    pygame.draw.rect(tela, CIANO_NEON, jogador_rect)

    for tiro in tiros:
        pygame.draw.rect(tela, MAGENTA_NEON, tiro)

    # Atualizando a tela
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()