import pygame
import os

# --- 1. Inicialização ---
# Inicializa todos os módulos do Pygame (pygame, font, mixer)
pygame.init()
pygame.font.init()

# --- 2. Configurações da Tela e Cores ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CIANO_NEON = (0, 255, 255)
MAGENTA_NEON = (255, 0, 255)
VERDE_NEON = (57, 255, 20)
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Guerra de Naves Neon")

# --- 3. Caminhos dos Arquivos (CORREÇÃO DE ERRO) ---
# Encontra o caminho absoluto para a pasta onde o script está
caminho_script = os.path.dirname(os.path.realpath(__file__))
caminho_pasta_sons = os.path.join(caminho_script, 'sons')
# ATUALIZADO: Nome da pasta de imagens
caminho_pasta_imagens = os.path.join(caminho_script, 'pixel_art')

# --- 4. Carregamento de Sons ---
som_tiro = None
som_explosao = None
try:
    caminho_som_tiro = os.path.join(caminho_pasta_sons, 'mixkit-short-laser-gun-shot-1670.wav')
    caminho_som_explosao = os.path.join(caminho_pasta_sons, 'mixkit-arcade-game-explosion-2759.wav')
    som_tiro = pygame.mixer.Sound(caminho_som_tiro)
    som_explosao = pygame.mixer.Sound(caminho_som_explosao)
    print("Sons carregados com sucesso!")
except pygame.error as e:
    print(f"Erro ao carregar som: {e}")
    print(f"Verifique a pasta: {caminho_pasta_sons}")

# --- 5. Configurações de Pontuação e Fonte ---
pontuacao = 0
fonte = pygame.font.Font(None, 36) # Fonte padrão, tamanho 36

# --- 6. Configurações das Entidades (Jogador, Inimigos) ---
# Tamanhos - ajuste se suas imagens ficarem desproporcionais
largura_jogador, altura_jogador = 50, 40
largura_inimigo, altura_inimigo = 40, 30

# Jogador
jogador_rect = pygame.Rect(largura / 2 - largura_jogador / 2, altura - altura_jogador - 10, largura_jogador, altura_jogador)
velocidade_jogador = 7

# Tiros
tiros = []
velocidade_tiro = 10

# Inimigos
inimigos = []
velocidade_inimigo_x = 2
descida_inimigo = 10
# Loop para criar a grade de inimigos
for linha in range(5):
    for coluna in range(10):
        x = coluna * (largura_inimigo + 15) + 50
        y = linha * (altura_inimigo + 15) + 50
        inimigos.append(pygame.Rect(x, y, largura_inimigo, altura_inimigo))

# --- 7. Carregamento de Imagens (Sprites) ---
nave_img = None
alien_img = None
try:
    # ATUALIZADO: Nomes dos arquivos de imagem
    nave_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Nave.png')).convert_alpha()
    alien_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Alien.png')).convert_alpha()
    print("Imagens carregadas com sucesso!")

    # Redimensiona as imagens para o tamanho dos nossos retângulos
    nave_img = pygame.transform.scale(nave_img_original, (largura_jogador, altura_jogador))
    alien_img = pygame.transform.scale(alien_img_original, (largura_inimigo, altura_inimigo))

except pygame.error as e:
    print(f"Erro ao carregar imagem: {e}")
    print(f"Verifique a pasta: {caminho_pasta_imagens}")
    print("Certifique-se que os arquivos 'Nave.png' e 'Alien.png' estão lá.")
    print("O jogo rodará com retângulos coloridos.")


# --- 8. Loop Principal do Jogo ---
relogio = pygame.time.Clock()
rodando = True
while rodando:
    # Controla o FPS (quadros por segundo)
    relogio.tick(60)

    # --- 8a. Checagem de Eventos (Input) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            # Evento de apertar ESPAÇO para atirar
            if evento.key == pygame.K_SPACE and len(tiros) < 5: # Limita tiros na tela
                tiro_rect = pygame.Rect(jogador_rect.centerx - 2, jogador_rect.top, 4, 10)
                tiros.append(tiro_rect)
                if som_tiro:
                    som_tiro.play()

    # --- 8b. Lógica do Jogo ---
    # Movimento do Jogador (teclas pressionadas)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_rect.left > 0:
        jogador_rect.x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_rect.right < largura:
        jogador_rect.x += velocidade_jogador

    # Movimento dos Tiros
    for tiro in tiros[:]: # Itera sobre uma cópia
        tiro.y -= velocidade_tiro
        if tiro.bottom < 0:
            tiros.remove(tiro)

    # Movimento dos Inimigos
    if inimigos: # Só executa se houver inimigos
        mudar_direcao = False
        for inimigo in inimigos:
            inimigo.x += velocidade_inimigo_x
            # Checa se *algum* inimigo tocou na borda
            if inimigo.right >= largura or inimigo.left <= 0:
                mudar_direcao = True
        
        # Se tocou na borda, inverte a direção e desce
        if mudar_direcao:
            velocidade_inimigo_x *= -1
            for inimigo in inimigos:
                inimigo.y += descida_inimigo

    # Detecção de Colisão
    # Tiro acerta Inimigo
    for tiro in tiros[:]:
        for inimigo in inimigos[:]:
            if tiro.colliderect(inimigo):
                tiros.remove(tiro)
                inimigos.remove(inimigo)
                pontuacao += 10
                if som_explosao:
                    som_explosao.play()
                break # A bala já foi usada

    # Inimigo acerta Jogador (Game Over)
    for inimigo in inimigos:
        if inimigo.colliderect(jogador_rect):
            print(f"GAME OVER! Pontuação final: {pontuacao}")
            rodando = False
            break

    # --- 8c. Desenho na Tela ---
    tela.fill(PRETO) # Limpa a tela

    # Desenha o Jogador (Imagem ou retângulo)
    if nave_img:
        tela.blit(nave_img, jogador_rect)
    else:
        pygame.draw.rect(tela, CIANO_NEON, jogador_rect)

    # Desenha os Tiros
    for tiro in tiros:
        pygame.draw.rect(tela, MAGENTA_NEON, tiro)

    # Desenha os Inimigos (Imagem ou retângulo)
    if alien_img:
        for inimigo in inimigos:
            tela.blit(alien_img, inimigo)
    else:
        for inimigo in inimigos:
            pygame.draw.rect(tela, VERDE_NEON, inimigo)

    # Desenha a Pontuação
    texto_surface = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(texto_surface, (10, 10))

    # --- 8d. Atualização da Tela ---
    pygame.display.flip()

# --- 9. Finalização ---
pygame.quit()