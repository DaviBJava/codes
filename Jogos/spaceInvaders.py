import pygame

# Inicializando o Pygame e o módulo de fontes
pygame.init()
pygame.font.init() # Adicionado para garantir que o módulo de fontes está pronto

# Definindo as cores (estilo NEON)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CIANO_NEON = (0, 255, 255)
MAGENTA_NEON = (255, 0, 255)
VERDE_NEON = (57, 255, 20)

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Guerra de Naves Neon")

# NOVO: Configurações de Pontuação e Texto
pontuacao = 0
fonte = pygame.font.Font(None, 36) # Fonte padrão, tamanho 36

# --- Configurações do Jogador ---
largura_jogador = 50
altura_jogador = 30
jogador_rect = pygame.Rect(largura / 2 - largura_jogador / 2, altura - altura_jogador - 10, largura_jogador, 
                           altura_jogador)
velocidade_jogador = 7

# --- Configurações dos Tiros ---
tiros = []
velocidade_tiro = 10

# --- Configurações dos Inimigos ---
inimigos = []
largura_inimigo = 40
altura_inimigo = 25
velocidade_inimigo_x = 2
descida_inimigo = 10

# Criando a grade de inimigos
num_linhas = 5
num_colunas = 10
espacamento = 15

for linha in range(num_linhas):
    for coluna in range(num_colunas):
        x = coluna * (largura_inimigo + espacamento) + 50
        y = linha * (altura_inimigo + espacamento) + 50
        inimigo_rect = pygame.Rect(x, y, largura_inimigo, altura_inimigo)
        inimigos.append(inimigo_rect)

# Para controlar a taxa de quadros (FPS)
relogio = pygame.time.Clock()

# Loop Principal do Jogo
rodando = True
while rodando:
    relogio.tick(60)

    # Checando Eventos (ações do jogador)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and len(tiros) < 5:
                tiro_rect = pygame.Rect(jogador_rect.centerx - 2, jogador_rect.top, 4, 10)
                tiros.append(tiro_rect)

    # --- Lógica do Jogo ---
    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_rect.left > 0:
        jogador_rect.x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_rect.right < largura:
        jogador_rect.x += velocidade_jogador

    # Movimenta os tiros e remove os que saem da tela
    for tiro in tiros[:]:
        tiro.y -= velocidade_tiro
        if tiro.bottom < 0:
            tiros.remove(tiro)

    # Lógica dos Inimigos
    if inimigos:
        mudar_direcao = False
        for inimigo in inimigos:
            inimigo.x += velocidade_inimigo_x
            if inimigo.right >= largura or inimigo.left <= 0:
                mudar_direcao = True

        if mudar_direcao:
            velocidade_inimigo_x *= -1
            for inimigo in inimigos:
                inimigo.y += descida_inimigo

    # Lógica de Colisão
    for tiro in tiros[:]:
        for inimigo in inimigos[:]:
            if tiro.colliderect(inimigo):
                tiros.remove(tiro)
                inimigos.remove(inimigo)
                pontuacao += 10 # Aumenta a pontuação
                break

    for inimigo in inimigos:
        if inimigo.colliderect(jogador_rect):
            print(f"GAME OVER! Pontuação final: {pontuacao}")
            rodando = False
            break

    # --- Desenho na tela ---
    tela.fill(PRETO)
    pygame.draw.rect(tela, CIANO_NEON, jogador_rect)

    for tiro in tiros:
        pygame.draw.rect(tela, MAGENTA_NEON, tiro)

    for inimigo in inimigos:
        pygame.draw.rect(tela, VERDE_NEON, inimigo)

    # NOVO: Desenha a pontuação
    texto_surface = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(texto_surface, (10, 10))

    # Atualizando a tela
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()