# O usuário digita 15
idade_texto = float(input("Digite sua idade: "))

# O que acontece se tentarmos somar?
# idade_texto + 5  <-- ISSO VAI DAR ERRO!

print(type(idade_texto)) # Vai mostrar <class 'str'>
# Para corrigir, precisamos converter a string para inteiro
idade = int(idade_texto)
print(type(idade)) # Vai mostrar <class 'int'>