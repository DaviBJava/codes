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

# --- 5. Configurações de Fontes ---
pontuacao = 0
fonte = pygame.font.Font(None, 36)
fonte_titulo = pygame.font.Font(None, 72)
fonte_instrucao = pygame.font.Font(None, 30)

# --- 6. Configurações das Entidades ---
largura_jogador, altura_jogador = 50, 40
largura_inimigo, altura_inimigo = 40, 30

vidas_jogador = 3 # NOVO: Vidas do jogador

jogador_rect = pygame.Rect(largura / 2 - largura_jogador / 2, altura - altura_jogador - 10, largura_jogador, altura_jogador)
velocidade_jogador = 7

tiros = []
velocidade_tiro = 10

tiros_inimigos = []
velocidade_tiro_inimigo = 5

inimigos = []
velocidade_inimigo_x = 2
descida_inimigo = 10

def criar_inimigos():
    inimigos.clear()
    for linha in range(5):
        for coluna in range(10):
            x = coluna * (largura_inimigo + 15) + 50
            y = linha * (altura_inimigo + 15) + 50
            inimigos.append(pygame.Rect(x, y, largura_inimigo, altura_inimigo))

criar_inimigos()

# --- 7. Carregamento de Imagens (Sprites) ---
nave_img = None
alien_img = None
nave_icone_img = None # NOVO: Ícone para mostrar as vidas
try:
    nave_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Nave.png')).convert_alpha()
    alien_img_original = pygame.image.load(os.path.join(caminho_pasta_imagens, 'Alien.png')).convert_alpha()
    print("Imagens carregadas com sucesso!")
    
    nave_img = pygame.transform.scale(nave_img_original, (largura_jogador, altura_jogador))
    alien_img = pygame.transform.scale(alien_img_original, (largura_inimigo, altura_inimigo))
    # NOVO: Cria um ícone de vida pequeno (25x20 pixels)
    nave_icone_img = pygame.transform.scale(nave_img_original, (25, 20))

except pygame.error as e:
    print(f"Erro ao carregar imagem: {e}")

# --- 8. Loop Principal do Jogo ---
relogio = pygame.time.Clock()
rodando = True
estado_jogo = "jogando"

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
            
            elif estado_jogo == "game_over" or estado_jogo == "vitoria":
                if evento.key == pygame.K_r:
                    # --- REINICIAR O JOGO ---
                    estado_jogo = "jogando"
                    pontuacao = 0
                    vidas_jogador = 3 # NOVO: Reseta as vidas
                    tiros.clear()
                    tiros_inimigos.clear()
                    jogador_rect.x = largura / 2 - largura_jogador / 2
                    jogador_rect.y = altura - altura_jogador - 10
                    criar_inimigos()


    # --- 8b. Lógica e Desenho (Baseado no Estado do Jogo) ---

    if estado_jogo == "jogando":
        # --- Lógica do Jogo ---
        # Movimento do Jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_rect.left > 0:
            jogador_rect.x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_rect.right < largura:
            jogador_rect.x += velocidade_jogador

        # Movimento dos Tiros do Jogador
        for tiro in tiros[:]:
            tiro.y -= velocidade_tiro
            if tiro.bottom < 0:
                tiros.remove(tiro)

        # Movimento dos Inimigos
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

        # Lógica de Tiro Inimigo
        if inimigos and random.randint(0, 100) < 1: 
            inimigo_atirador = random.choice(inimigos)
            tiro_inimigo_rect = pygame.Rect(inimigo_atirador.centerx - 2, inimigo_atirador.bottom, 4, 10)
            tiros_inimigos.append(tiro_inimigo_rect)

        # Movimento dos Tiros Inimigos
        for tiro in tiros_inimigos[:]:
            tiro.y += velocidade_tiro_inimigo
            if tiro.top > altura:
                tiros_inimigos.remove(tiro)

        # --- Colisões ---
        # Tiro do Jogador acerta Inimigo
        for tiro in tiros[:]:
            for inimigo in inimigos[:]:
                if tiro.colliderect(inimigo):
                    tiros.remove(tiro)
                    inimigos.remove(inimigo)
                    pontuacao += 10
                    if som_explosao:
                        som_explosao.play()
                    break 

        # MODIFICADO: Tiro Inimigo acerta Jogador
        for tiro in tiros_inimigos[:]:
            if tiro.colliderect(jogador_rect):
                tiros_inimigos.remove(tiro)
                vidas_jogador -= 1 # Perde uma vida
                if som_explosao:
                    som_explosao.play()
                print(f"Atingido! Vidas restantes: {vidas_jogador}")
                
                # Reseta posição e limpa tiros para dar chance
                jogador_rect.x = largura / 2 - largura_jogador / 2
                tiros_inimigos.clear()

                if vidas_jogador <= 0:
                    estado_jogo = "game_over"
                    print(f"GAME OVER! Sem vidas! Pontuação final: {pontuacao}")
                break
        
        # MODIFICADO: Inimigo (a nave) acerta Jogador
        if estado_jogo == "jogando": # Garante que não foi game over no loop anterior
            for inimigo in inimigos:
                if inimigo.colliderect(jogador_rect):
                    inimigos.remove(inimigo) # Remove o inimigo que bateu
                    vidas_jogador -= 1 # Perde uma vida
                    if som_explosao:
                        som_explosao.play()
                    print(f"Colisão! Vidas restantes: {vidas_jogador}")

                    jogador_rect.x = largura / 2 - largura_jogador / 2
                    tiros_inimigos.clear()
                    
                    if vidas_jogador <= 0:
                        estado_jogo = "game_over"
                        print(f"GAME OVER! Invasão! Pontuação final: {pontuacao}")
                    break
        
        # Checagem de Vitória
        if not inimigos and estado_jogo == "jogando":
            print(f"VOCÊ VENCEU! Pontuação final: {pontuacao}")
            estado_jogo = "vitoria"

        # --- Desenho na Tela (Jogando) ---
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

        # Desenha a Pontuação
        texto_surface = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_surface, (10, 10))

        # NOVO: Desenha as Vidas
        if nave_icone_img:
            for i in range(vidas_jogador):
                # Desenha os ícones no canto superior direito
                tela.blit(nave_icone_img, (largura - (i + 1) * 35, 10))
        else:
            # Texto alternativo se a imagem falhar
            vidas_surface = fonte.render(f"Vidas: {vidas_jogador}", True, BRANCO)
            tela.blit(vidas_surface, (largura - 150, 10))


    # --- Telas de Fim de Jogo ---
    elif estado_jogo == "game_over":
        tela.fill(PRETO)
        texto_go = fonte_titulo.render("GAME OVER", True, MAGENTA_NEON)
        texto_go_rect = texto_go.get_rect(center=(largura / 2, altura / 2 - 40))
        tela.blit(texto_go, texto_go_rect)
        
        texto_pontos = fonte.render(f"Pontuação Final: {pontuacao}", True, BRANCO)
        texto_pontos_rect = texto_pontos.get_rect(center=(largura / 2, altura / 2 + 20))
        tela.blit(texto_pontos, texto_pontos_rect)
        
        texto_reset = fonte_instrucao.render("Pressione R para jogar novamente", True, BRANCO)
        texto_reset_rect = texto_reset.get_rect(center=(largura / 2, altura / 2 + 70))
        tela.blit(texto_reset, texto_reset_rect)

    elif estado_jogo == "vitoria":
        tela.fill(PRETO)
        texto_vitoria = fonte_titulo.render("VOCÊ VENCEU!", True, CIANO_NEON)
        texto_vitoria_rect = texto_vitoria.get_rect(center=(largura / 2, altura / 2 - 40))
        tela.blit(texto_vitoria, texto_vitoria_rect)
        
        texto_pontos = fonte.render(f"Pontuação Final: {pontuacao}", True, BRANCO)
        texto_pontos_rect = texto_pontos.get_rect(center=(largura / 2, altura / 2 + 20))
        tela.blit(texto_pontos, texto_pontos_rect)
        
        texto_reset = fonte_instrucao.render("Pressione R para jogar novamente", True, BRANCO)
        texto_reset_rect = texto_reset.get_rect(center=(largura / 2, altura / 2 + 70))
        tela.blit(texto_reset, texto_reset_rect)

    # --- 8d. Atualização da Tela ---
    pygame.display.flip()

# --- 9. Finalização ---
pygame.quit()