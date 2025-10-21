# 1. Inicializar a lista vazia
lista_de_tarefas = []

print("--- Meu Planejador de Tarefas ---")

# 2. Iniciar um loop que, a princípio, é infinito
while True:
    # 3. Pedir a tarefa ao usuário, informando como sair
    nova_tarefa = input("Digite uma nova tarefa (ou 'fim' para terminar): ")

    # 4. Verificar se o usuário quer sair ANTES de adicionar à lista
    # Usamos .lower() para ignorar se foi digitado 'fim', 'Fim', 'FIM', etc.
    if nova_tarefa.lower() == 'fim':
        print("Finalizando a lista...")
        break  # Este comando quebra o loop e pula para a linha de código fora dele

    # 5. Se não for 'fim', adiciona a tarefa normalmente
    lista_de_tarefas.append(nova_tarefa)
    
    print("-> Tarefa adicionada!")

# 6. Exibir a lista final, somente depois que o loop for quebrado
print("--- Sua lista de tarefas para hoje ---")

# Adicionamos uma verificação para o caso de o usuário não ter adicionado nenhuma tarefa
if not lista_de_tarefas:
    print("Você não adicionou nenhuma tarefa. Dia livre!")
else:
    for tarefa in lista_de_tarefas:
        print(tarefa)

print("-------------------------------------")