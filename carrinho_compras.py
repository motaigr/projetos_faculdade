#como requisito de criatividade, adicionei a confirmação de remoção do item, para evitar que o usuário remova um item por engano.
nomes = []
precos = []

print("Bem-vindos ao Programa de Carrinho de Compras!")

while True:
    print("\nSelecione uma das seguintes ações:")
    print("1. Adicionar item")
    print("2. Ver carrinho")
    print("3. Remover item")
    print("4. Calcular o total")
    print("5. Sair")

    opcao = input("Digite o número da ação desejada: ")

    if opcao == "1":
        nome = input("Qual item você gostaria de adicionar? ")
        preco = float(input(f"Qual é o preço de '{nome}'? "))
        nomes.append(nome)
        precos.append(preco)
        print(f"O item '{nome}' foi adicionado ao carrinho.")

    elif opcao == "2":
        if len(nomes) == 0:
            print("O carrinho está vazio.")
        else:
            print("\nItens no carrinho:")
            for i in range(len(nomes)):
                print(f"{i + 1}. {nomes[i]}: R$ {precos[i]:.2f}")

    elif opcao == "3":
        if len(nomes) == 0:
            print("O carrinho está vazio.")
        else:
            print("\nItens no carrinho:")
            for i in range(len(nomes)):
                print(f"{i + 1}. {nomes[i]}: R$ {precos[i]:.2f}")
            
            numero = int(input("Qual item você gostaria de remover? "))
            indice = numero - 1

            if 0 <= indice < len(nomes):
                print(f"Tem certeza que deseja remover o item '{nomes[indice]}'? (s/n): ")
                confirmacao = input().lower()
                if confirmacao == "s":
                    nomes.pop(indice)
                    precos.pop(indice)
                    print("Item removido.")
                else:
                    print("Operação cancelada.")
            else:
                print("O número informado não é válido.")

    elif opcao == "4":
        if len(nomes) == 0:
            print("O carrinho está vazio.")
        else:
            total = sum(precos)
            print(f"\nO total da compra é: R$ {total:.2f}")

    elif opcao == "5":
        print("Obrigado por usar o Programa de Carrinho de Compras!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
