# Primeiro, precisamos "chamar" a ferramenta de desenho
import turtle

# Criar a nossa "tartaruga" que vai desenhar
caneta = turtle.Turtle()

# Vamos deixar o desenho um pouco mais rápido
caneta.speed(5) 

# --- 1. Desenhando a base da casa (o quadrado) ---
print("Desenhando a base da casa...")
caneta.color("brown") # Define a cor da caneta para marrom
for i in range(4):  # Repetir 4 vezes para fazer um quadrado
    caneta.forward(150) # Anda 150 passos para frente
    caneta.left(90)     # Vira 90 graus para a esquerda

# --- 2. Desenhando o telhado (o triângulo) ---
print("Colocando o telhado...") # Mensagem para o usuário
caneta.color("red") # Muda a cor da caneta para vermelho
caneta.penup()      # Levanta a caneta para não riscar
caneta.goto(0, 150) # Move a caneta para o topo do quadrado
caneta.pendown()    # Abaixa a caneta para voltar a desenhar

caneta.left(45)     # Vira 45 graus
caneta.forward(106) # Desenha um lado do telhado
caneta.right(90)    # Vira para o outro lado
caneta.forward(106) # Desenha o outro lado do telhado

# --- 3. Desenhando a porta ---
print("Fazendo a porta...") # Mensagem para o usuário
caneta.color("black") # Muda a cor da caneta para preto
caneta.penup()     # Levanta a caneta para não riscar
caneta.goto(60, 0) # Posiciona para o início da porta
caneta.pendown() # Abaixa a caneta para desenhar

caneta.setheading(90) # Aponta a caneta para cima
caneta.forward(70)    # Altura da porta
caneta.right(90)   # Vira para a direita
caneta.forward(30)    # Largura da porta
caneta.right(90) # Vira para baixo
caneta.forward(70)    # Outro lado da porta

# Esconde a "tartaruga" no final para vermos só o desenho
caneta.hideturtle()

# Mantém a janela aberta até que a gente clique para fechar
turtle.done()