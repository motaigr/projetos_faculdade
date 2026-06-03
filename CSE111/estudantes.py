import os; os.system('cls')
import csv

def criar_dicionario_estudantes(arquivo_csv, chave_id, nome):
    dicionario = {}
    with open(arquivo_csv, "rt", encoding="utf-8") as arquivo_estudantes:
        leitor_de_arquivo = csv.reader(arquivo_estudantes)
        next(leitor_de_arquivo)  # Pula o cabeçalho

        for linha in leitor_de_arquivo:
            id_estudante = linha[chave_id]
            dicionario[id_estudante] = linha[nome]
    return dicionario

def main():
    INDICE_ID = 0
    INDICE_NOME = 1

    d_estudante = criar_dicionario_estudantes("estudantes.csv", INDICE_ID, INDICE_NOME)

    id = input("Digite o ID do estudante: ")
    id = id.replace("-", "")  # Remove hífens do ID, se houver

    if id in d_estudante:
        print(f"Nome do estudante é: {d_estudante[id]}")
    elif not id.isdigit():
        print("Número de identificação invalido.")
    elif len(id) != 9:
        print("Número de identificação invalido, digitos insuficientes.")
    elif len(id) > 9:
        print("Número de identificação invalido, digitos excedentes.")    
    else:        
        print("Estudante inexistente.")

if __name__ == "__main__":
    main()