nota = float(input("Insira sua nota: "))
if nota >= 6.0:
    print("Você passou!")
else:
    print("Você não passou!")

recuperacao = input("Você está de recuperação? (s/n) ")
if recuperacao.lower() == 's':
    nota_recuperacao = float(input("Insira sua nota de recuperação: "))
    if (nota + nota_recuperacao) / 2 >= 5.0:
        print("Você passou na recuperação!")
    else:
        print("Você não passou na recuperação.")