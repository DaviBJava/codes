# Lista de itens dentro de cada baú que o herói vai abrir
conteudo_dos_baus = ["Moedas de Cobre", "Adaga Velha", "Coroa Lendária", "Mapa Rasgado", "Elmo Enferrujado"]
item_procurado = "Coroa Lendária"

print("Iniciando a busca pela Coroa Lendária!")
print("---------------------------------------")

# O herói começa a abrir os baús, um por um
for item_encontrado in conteudo_dos_baus:
    
    print(f"Você abriu um baú e encontrou... {item_encontrado}!")

    # Verificamos se o item encontrado é o que procuramos
    if item_encontrado == item_procurado:
        print("\nACHEI! É a Coroa Lendária! Missão cumprida!")
        # O comando BREAK interrompe o loop imediatamente.
        # Os outros baús ("Mapa Rasgado", "Elmo Enferrujado") não serão abertos.
        break

print("---------------------------------------")
print("Você sai da sala do tesouro com seu prêmio.")