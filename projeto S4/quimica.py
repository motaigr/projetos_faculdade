from formula import interpretar_formula

def main():
    #Adicionei um loop para permitir que o usuário faça várias consultas sem precisar reiniciar o programa
    while True:
        formula = input("Digite a fórmula química (ou 'sair' para encerrar): ")
        if formula == "sair":
            break
        amostra = float(input("Digite o tamanho da amostra em gramas: "))
        tabela_periodica = criar_tabela_periodica()
        interpretacao = interpretar_formula(formula, tabela_periodica)
        massa_molar = calcular_massa_molar(interpretacao, tabela_periodica)
        print(f"Massa molar: {massa_molar} g/mol")
        print(f"Quantidade de mols: {amostra / massa_molar:.5f} mol")


def calcular_massa_molar(lista_quantidade_simbolos, dic_tabela_periodica):
    massa_molar = 0
    for simbolo, quantidade in lista_quantidade_simbolos:
        if simbolo in dic_tabela_periodica:
            massa_molar += dic_tabela_periodica[simbolo][1] * quantidade
        else:
            print(f"Elemento {simbolo} não encontrado na tabela periódica.")
    return massa_molar

def criar_tabela_periodica():
    tabela_periodica = open('elementos.csv', 'r', encoding='utf-8')
    next(tabela_periodica)  # Pula o cabeçalho
    dic_tabela_periodica = {}
    for linha in tabela_periodica:
        partes = linha.strip().split(',')
        dic_tabela_periodica[partes[0].strip('"')] = [partes[1].strip('"'), float(partes[2])]
    return dic_tabela_periodica

if __name__ == "__main__":
    main()