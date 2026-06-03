import csv


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
    dicionario = ler_dicionario('produtos.csv', 0)
    print(dicionario)

    with open('pedido.csv', mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)  # Pula o cabeçalho
        for linha in leitor_csv:
            id_produto = linha[0]
            quantidade = int(linha[1])
            
            if id_produto in dicionario:
                nome_produto, preco_unitario = dicionario[id_produto]
                total = quantidade * preco_unitario
                print(f"Produto: {nome_produto}, Quantidade: {quantidade}, Preço Unitário: R${preco_unitario:.2f}")

if __name__ == "__main__":
    main()