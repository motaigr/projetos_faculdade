import csv
import datetime

# Melhoria adicionada: cálculo do ticket médio da compra,
# exibindo o valor médio gasto por tipo de produto no pedido.

def ler_dicionario(arquivo_csv, INDICE_PRODUTO):
    dicionario = {}
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            id_chave = linha[INDICE_PRODUTO]
            dicionario[id_chave] = [linha[1], float(linha[2])]
    return dicionario

def main():
    try:
        dicionario = ler_dicionario('produtos.csv', 0)
    

        with open('pedido.csv', mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv)  # Pula o cabeçalho

            numero_itens = 0
            subtotal = 0
            numero_linhas = 0

            print("Emporio Inkom")

            for linha in leitor_csv:
                id_produto = linha[0]
                quantidade = int(linha[1])
                
                nome_produto, preco_unitario = dicionario[id_produto]
                preco_unitario = quantidade * preco_unitario
                print(f"{nome_produto}: {quantidade} @ {preco_unitario:.2f}")

                numero_itens += quantidade
                subtotal += preco_unitario
                numero_linhas += 1

            imposto = subtotal * 0.06
            total = subtotal + imposto
            ticket_medio = subtotal / numero_linhas

            print(f"Numero de itens: {numero_itens}")
            print(f"Subtotal: R${subtotal:.2f}")
            print(f"Imposto: R${imposto:.2f}")
            print(f"Total: R${total:.2f}")
            print(f"Ticket médio da compra: R${ticket_medio:.2f}")
            print(f"Obrigado por comprar conosco!")
            print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")



    except KeyError:
        print(f"Error: unknown product ID in the request.csv file {id_produto}.")        
    except FileNotFoundError:
            print("Error: missing file.")
            
if __name__ == "__main__":
    main()