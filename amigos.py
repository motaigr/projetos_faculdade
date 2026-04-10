amigos = []


nome_amigos = ""

while nome_amigos.lower() != "sair":
    nome_amigos = input("Digite o nome do amigo ou 'sair' para encerrar: ")
    if nome_amigos.lower() != "sair":
        amigos.append(nome_amigos)

print("Lista de amigos:")
for amigo in amigos:
    print(f"- {amigo}")