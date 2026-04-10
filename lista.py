mercado = []

itens_mercado = ""

while itens_mercado != "sair":
    itens_mercado = input("Digite o nome do item ou 'sair' para encerrar: ")
    if itens_mercado.lower() != "sair":
        mercado.append(itens_mercado)

print("Lista de itens do mercado:")
for item in mercado:
    print(f"- {item}")

# Loop 2 - for com range e índice
print("\nLista com índices:")
for i in range(len(mercado)):
    item = mercado[i] 
    print(f"{i}. {item}")

# Pede o índice e o novo item
indice = int(input("Digite o índice do item que deseja substituir: "))
novo_item = input("Digite o novo item: ")

# Substitui diretamente
mercado[indice] = novo_item

# Exibe a lista atualizada
print("\nLista atualizada:")
for item in mercado:
    print(f"- {item}")