import csv


def ler_dicionario(arquivo_csv, chave_id, nome):
    dicionario = {}
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            id_chave = linha[chave_id]
            dicionario[id_chave] = linha[nome]
    return dicionario

def main():
    dicionario = ler_dicionario('pedido.csv', 'produtos.csv', 'id', 'nome')
    print(dicionario)

if __name__ == "__main__":
    main()