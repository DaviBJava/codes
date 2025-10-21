contador = 5

while contador > 0:
  print(f"Contagem regressiva: {contador}")
  contador = contador - 1  # Decrementa o contador para evitar um laço infinito

print("Lançar!")

# Saída:
# Contagem regressiva: 5
# Contagem regressiva: 4
# Contagem regressiva: 3
# Contagem regressiva: 2
# Contagem regressiva: 1
# Lançar!




import Ed

Ed.EdisonVersion = Ed.V2

# O laço 'for' irá repetir o bloco de código abaixo 4 vezes.
# Uma vez para cada lado do quadrado.
for i in range(5):
  # 1. Anda para frente por 1 segundo
  Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 1)

  # 2. Vira para a direita por um curto período para fazer um ângulo de 90 graus
  Ed.Drive(Ed.RIGHT, Ed.SPEED_5, 0.245)

# Após o laço terminar, o programa para.




# É necessário importar a biblioteca do Edison para usar seus comandos
import Ed

# Configura o programa para a versão correta do robô (V2.0)
Ed.EdisonVersion = Ed.V2

# Comando para mover o robô
# Parâmetros: (Direção, Velocidade, Duração em segundos)
Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 2)

# O robô vai parar automaticamente após os 2 segundos.
# O programa termina aqui.



import Ed

Ed.EdisonVersion = Ed.V2

# Comando para virar para a esquerda
# A duração de 0.245 segundos é um bom ponto de partida para um giro de 90 graus
Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 0.245)

# O robô para automaticamente após o giro




import Ed

Ed.EdisonVersion = Ed.V2

# Comando para virar para a direita
# Usamos o mesmo tempo, mas na direção oposta
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 0.245)

# O robô para automaticamente após o giro




import Ed

Ed.EdisonVersion = Ed.V2

# Para fazer uma meia-volta (180 graus), dobramos o tempo do giro de 90 graus
# 0.245 * 2 = 0.49 segundos
Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 0.49)

# O robô para após completar a meia-volta