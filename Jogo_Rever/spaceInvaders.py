import pygame
import os
import random

# --- 1. Inicialização ---
pygame.init()
pygame.font.init()
pygame.mixer.init()

# --- 2. Configurações da Tela e Cores ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CIANO_NEON = (0, 255, 255)
MAGENTA_NEON = (255, 0, 255)
VERDE_NEON = (57, 255, 20)
LARANJA_NEON = (255, 165, 0)

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Guerra de Naves Neon")

# --- 3. Caminhos dos Arquivos ---
caminho_script = os.path.dirname(os.path.realpath(__file__))
caminho_pasta_sons = os.path.join(caminho_script, 'sons')
caminho_pasta_imagens = os.path.join(caminho_script, 'pixel_art')
ARQUIVO_HIGHSCORE = os.path.join(caminho_script, 'highscore.txt')

# --- 4. Carregamento de Sons ---
# (O código de carregamento de som permanece o mesmo)
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

# --- Funções de High Score ---
# (O código de High Score permanece o mesmo)
def carregar_high_score():
    try:
        with open(ARQUIVO_HIGHSCORE, 'r') as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def salvar_high_score(nova_pontuacao):
    try:
        with open(ARQUIVO_HIGHSCORE, 'w') as f:
            f.write(str(nova_pontuacao))
    except IOError as e:
        print(f"Erro ao salvar high score: {e}")

# --- 5. Configurações de Fontes ---
pontuacao = 0
high_score = carregar_high_score()
fonte = pygame.font.Font(None, 36)
fonte_titulo = pygame.font.Font(None, 72)
fonte_instrucao = pygame.font.Font(None, 30)

# --- 6. Configurações das Entidades ---
largura_jogador, altura_jogador = 50, 40
largura_inimigo, altura_inimigo = 40, 30

vidas_jogador = 3
nivel = 1
descida_inimigo = 10

jogador_rect = pygame.Rect(largura / 2 - largura_jogador / 2, altura - altura_jogador - 10, largura_jogador, altura_jogador)
velocidade_jogador = 7

tiros = []
velocidade_tiro = 10

tiros_inimigos = []
velocidade_tiro_inimigo = 5

inimigos = []

# MODIFICADO: Lógica de Velocidade
VELOCIDADE_INIMIGO_BASE = 2
CHANCE_TIRO_INIMIGO_BASE = 100 

velocidade_inimigo_mag = VELOCIDADE_INIMIGO_BASE # Magnitude da velocidade
direcao_inimigo = 1 # 1 = direita, -1 = esquerda
chance_tiro_inimigo = CHANCE_TIRO_INIMIGO_BASE

# NOVO: Precisamos armazenar a posição X dos inimigos como float
# pois o Rect arredonda. Usaremos uma lista de "posições x reais".
posicoes_x_inimigos = []

def criar_inimigos():
    inimigos.clear()
    posicoes_x_inimigos.clear() # Limpa as posições reais
    for linha in range(5):
        for coluna in range(10):
            x = coluna * (largura_inimigo + 15) + 50
            y = linha * (altura_inimigo + 15) + 50
            inimigos.append(pygame.Rect(x, y, largura_inimigo, altura_inimigo))
            posicoes_x_inimigos.append(float(x)) # Armazena o x real

criar_inimigos()

# --- 7. Carregamento de Imagens (Sprites) ---
# (O código de carregamento de imagens permanece o mesmo)
nave_img = None
alien_img = None
nave_icone_img = None
try:
    nave_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Nave.png')).convert_alpha()
    alien_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Alien.png')).convert_alpha()
    print("Imagens carregadas com sucesso!")
    
    nave_img = pygame.transform.scale(nave_img_original, (largura_jogador, altura_jogador))
    alien_img = pygame.transform.scale(alien_img_original, (largura_inimigo, altura_inimigo))
    nave_icone_img = pygame.transform.scale(nave_img_original, (25, 20))

except pygame.error as e:
    print(f"Erro ao carregar imagem: {e}")

# --- 8. Loop Principal do Jogo ---
relogio = pygame.time.Clock()
rodando = True
estado_jogo = "jogando"
tempo_inicio_nivel = 0

while rodando:
    relogio.tick(60)

    # --- 8a. Checagem de Eventos (Input) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN:
            if estado_jogo == "jogando":
                if evento.key == pygame.K_SPACE and len(tiros) < 5:
                    tiro_rect = pygame.Rect(jogador_rect.centerx - 2, jogador_rect.top, 4, 10)
                    tiros.append(tiro_rect)
                    if som_tiro:
                        som_tiro.play()
            
            elif estado_jogo == "game_over":
                if evento.key == pygame.K_r:
                    # --- REINICIAR O JOGO ---
                    estado_jogo = "jogando"
                    pontuacao = 0
                    vidas_jogador = 3
                    nivel = 1 
                    # Reseta a dificuldade
                    velocidade_inimigo_mag = VELOCIDADE_INIMIGO_BASE
                    direcao_inimigo = 1 # Começa andando para a direita
                    chance_tiro_inimigo = CHANCE_TIRO_INIMIGO_BASE
                    
                    tiros.clear()
                    tiros_inimigos.clear()
                    jogador_rect.x = largura / 2 - largura_jogador / 2
                    jogador_rect.y = altura - altura_jogador - 10
                    criar_inimigos()


    # --- 8b. Lógica e Desenho (Baseado no Estado do Jogo) ---

    if estado_jogo == "jogando":
        # --- Lógica do Jogo ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_rect.left > 0:
            jogador_rect.x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_rect.right < largura:
            jogador_rect.x += velocidade_jogador

        for tiro in tiros[:]:
            tiro.y -= velocidade_tiro
            if tiro.bottom < 0:
                tiros.remove(tiro)

        # MODIFICADO: Lógica de movimento inimigo
        if inimigos:
            mudar_direcao = False
            # 1. Calcula o movimento usando a velocidade real (float)
            movimento_x = velocidade_inimigo_mag * direcao_inimigo
            
            # Usamos 'zip' para parear cada Rect de inimigo com sua posição X real
            for i, inimigo in enumerate(inimigos):
                # Atualiza a posição real (float)
                posicoes_x_inimigos[i] += movimento_x
                # Atualiza o Rect (int) para desenho e colisão
                inimigo.x = int(posicoes_x_inimigos[i])
                
                # Checa a colisão com a parede
                if inimigo.right >= largura or inimigo.left <= 0:
                    mudar_direcao = True
            
            if mudar_direcao:
                direcao_inimigo *= -1 # Apenas inverte a direção
                for i, inimigo in enumerate(inimigos):
                    inimigo.y += descida_inimigo
                    # Força a saída da parede para evitar o "stuck"
                    posicoes_x_inimigos[i] += (velocidade_inimigo_mag * direcao_inimigo)
                    inimigo.x = int(posicoes_x_inimigos[i])

        if inimigos and random.randint(0, chance_tiro_inimigo) < 1: 
            inimigo_atirador = random.choice(inimigos)
            tiro_inimigo_rect = pygame.Rect(inimigo_atirador.centerx - 2, inimigo_atirador.bottom, 4, 10)
            tiros_inimigos.append(tiro_inimigo_rect)

        for tiro in tiros_inimigos[:]:
            tiro.y += velocidade_tiro_inimigo
            if tiro.top > altura:
                tiros_inimigos.remove(tiro)

        # --- Colisões ---
        # (A lógica de colisão permanece a mesma)
        for tiro in tiros[:]:
            # Precisamos remover o inimigo E sua posição X da outra lista
            indices_para_remover = []
            for i, inimigo in reversed(list(enumerate(inimigos))):
                if tiro.colliderect(inimigo):
                    indices_para_remover.append(i)
                    tiros.remove(tiro)
                    pontuacao += 10
                    if som_explosao:
                        som_explosao.play()
                    break 
            
            for i in indices_para_remover:
                inimigos.pop(i)
                posicoes_x_inimigos.pop(i)

        jogador_atingido = False
        for tiro in tiros_inimigos[:]:
            if tiro.colliderect(jogador_rect):
                tiros_inimigos.remove(tiro)
                jogador_atingido = True
                break
        
        if not jogador_atingido:
            # Precisamos checar a colisão e remover o inimigo certo
            indice_colisao = -1
            for i, inimigo in enumerate(inimigos):
                if inimigo.colliderect(jogador_rect):
                    indice_colisao = i
                    jogador_atingido = True
                    break
            
            if indice_colisao != -1:
                inimigos.pop(indice_colisao)
                posicoes_x_inimigos.pop(indice_colisao)

        if jogador_atingido:
            vidas_jogador -= 1
            if som_explosao:
                som_explosao.play()
            print(f"Atingido! Vidas restantes: {vidas_jogador}")
            
            jogador_rect.x = largura / 2 - largura_jogador / 2
            tiros_inimigos.clear()

            if vidas_jogador <= 0:
                estado_jogo = "game_over"
                print(f"GAME OVER! Pontuação final: {pontuacao}")
                if pontuacao > high_score:
                    high_score = pontuacao
                    salvar_high_score(high_score)
        
        if not inimigos and estado_jogo == "jogando":
            print(f"Nível {nivel} concluído!")
            estado_jogo = "proximo_nivel"
            tempo_inicio_nivel = pygame.time.get_ticks()

        # --- Desenho na Tela (Jogando) ---
        # (A lógica de desenho permanece a mesma)
        tela.fill(PRETO)
        if nave_img:
            tela.blit(nave_img, jogador_rect)
        else:
            pygame.draw.rect(tela, CIANO_NEON, jogador_rect)

        for tiro in tiros:
            pygame.draw.rect(tela, MAGENTA_NEON, tiro)
            
        for tiro in tiros_inimigos:
            pygame.draw.rect(tela, LARANJA_NEON, tiro)

        if alien_img:
            for inimigo in inimigos:
                tela.blit(alien_img, inimigo)
        else:
            for inimigo in inimigos:
                pygame.draw.rect(tela, VERDE_NEON, inimigo)

        texto_surface = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_surface, (10, 10))
        
        nivel_surface = fonte.render(f"Nível: {nivel}", True, BRANCO)
        tela.blit(nivel_surface, (10, 45))

        if nave_icone_img:
            for i in range(vidas_jogador):
                tela.blit(nave_icone_img, (largura - (i + 1) * 35, 10))
        else:
            vidas_surface = fonte.render(f"Vidas: {vidas_jogador}", True, BRANCO)
            tela.blit(vidas_surface, (largura - 150, 10))

    # MODIFICADO: Lógica de Próximo Nível
    elif estado_jogo == "proximo_nivel":
        tela.fill(PRETO)
        texto_nivel = fonte_titulo.render(f"NÍVEL {nivel + 1}", True, CIANO_NEON)
        texto_nivel_rect = texto_nivel.get_rect(center=(largura / 2, altura / 2))
        tela.blit(texto_nivel, texto_nivel_rect)

        if pygame.time.get_ticks() - tempo_inicio_nivel > 3000:
            nivel += 1
            # Aumenta a magnitude da velocidade
            velocidade_inimigo_mag = VELOCIDADE_INIMIGO_BASE + (nivel - 1) * 0.5
            direcao_inimigo = 1 # Sempre começa indo para a direita
            chance_tiro_inimigo = max(20, CHANCE_TIRO_INIMIGO_BASE - nivel * 10)
            
            print(f"Iniciando Nível {nivel}. Vel: {velocidade_inimigo_mag}, Chance Tiro: {chance_tiro_inimigo}")

            criar_inimigos()
            tiros.clear()
            tiros_inimigos.clear()
            estado_jogo = "jogando"

    # --- Tela de Game Over ---
    # (A lógica de Game Over permanece a mesma)
    elif estado_jogo == "game_over":
        tela.fill(PRETO)
        texto_go = fonte_titulo.render("GAME OVER", True, MAGENTA_NEON)
        texto_go_rect = texto_go.get_rect(center=(largura / 2, altura / 2 - 100))
        tela.blit(texto_go, texto_go_rect)
        
        texto_pontos = fonte.render(f"Sua Pontuação: {pontuacao}", True, BRANCO)
        texto_pontos_rect = texto_pontos.get_rect(center=(largura / 2, altura / 2 - 20))
        tela.blit(texto_pontos, texto_pontos_rect)

        texto_hs = fonte.render(f"High Score: {high_score}", True, CIANO_NEON)
        texto_hs_rect = texto_hs.get_rect(center=(largura / 2, altura / 2 + 20))
        tela.blit(texto_hs, texto_hs_rect)
        
        texto_nivel = fonte.render(f"Nível Alcançado: {nivel}", True, BRANCO)
        texto_nivel_rect = texto_nivel.get_rect(center=(largura / 2, altura / 2 + 60))
        tela.blit(texto_nivel, texto_nivel_rect)

        texto_reset = fonte_instrucao.render("Pressione R para jogar novamente", True, BRANCO)
        texto_reset_rect = texto_reset.get_rect(center=(largura / 2, altura / 2 + 120))
        tela.blit(texto_reset, texto_reset_rect)

    pygame.display.flip()

# --- 9. Finalização ---
pygame.quit()