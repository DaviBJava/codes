# 1. Inicializar a lista vazia
lista_de_tarefas = []

# 2. Mensagem inicial
print("--- Meu Planejador de Tarefas ---")
print("Organizando meu dia!")

# 3. Loop para pedir as tarefas 3 vezes
for i in range(3):
    nova_tarefa = input("Digite a tarefa " + str(i+1) + ": ")
    lista_de_tarefas.append(nova_tarefa)
    print("-> Tarefa adicionada!")

# 4. Exibir a lista final
print("Sua lista de tarefas para hoje ---")
for tarefa in lista_de_tarefas:
    print(f"- {tarefa}")
print("-------------------------------------")