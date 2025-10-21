ano_nascimento_texto = input("Em que ano você nasceu? ")

# Convertendo para inteiro
ano_nascimento_numero = int(ano_nascimento_texto)

# Agora sim!
idade = 2025 - ano_nascimento_numero
print("Em 2025, você terá", idade, "anos!")