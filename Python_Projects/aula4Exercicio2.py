# 1. Inicializar a lista vazia
lista_de_tarefas = []

print("--- Meu Planejador de Tarefas ---")

# 2. Perguntar ao usuário quantas tarefas ele quer adicionar
# Usamos int() para transformar a resposta (texto) em um número inteiro
numero_de_tarefas = int(input("Quantas tarefas você deseja adicionar à lista? "))

print(f"Ótimo! Por favor, insira suas {numero_de_tarefas} tarefas.")

# 3. Loop para pedir as tarefas o número de vezes que o usuário escolheu
# Trocamos o '3' pela variável 'numero_de_tarefas'
for i in range(numero_de_tarefas):
    # Usamos f-string para uma contagem mais amigável (1, 2, 3...)
    nova_tarefa = input(f"Digite a tarefa {i + 1}: ")
    lista_de_tarefas.append(nova_tarefa)
    print("-> Tarefa adicionada!")

# 4. Exibir a lista final, como antes
print("--- Sua lista de tarefas para hoje ---")
for tarefa in lista_de_tarefas:
    print(tarefa)
print("-------------------------------------")