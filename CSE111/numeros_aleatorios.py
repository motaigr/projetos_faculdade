import random

lista_palavras = ["casa", "carro", "computador", "celular", "livro"]

def main():
    lista = [12.5, 1.99, 50.7, 99.9]
    print(lista)

    anexar_numeros_aleatorios(lista)
    print(lista)

    anexar_numeros_aleatorios(lista, 4)
    print(lista)

    lista_palavras2 = []
    print(lista_palavras2)

    anexar_palavras_aleatorias(lista_palavras2)
    print(lista_palavras2)

    anexar_palavras_aleatorias(lista_palavras2, 3)
    print(lista_palavras2)

    quantidade_usuario = int(input("Quantos números aleatórios deseja adicionar? "))
    anexar_numeros_aleatorios(lista, quantidade_usuario)
    print(lista)


def anexar_numeros_aleatorios(lista_de_numeros, quantidade = 1):
    for x in range(quantidade):
        lista_de_numeros.append(round(random.uniform(1, 100),2))
    
def anexar_palavras_aleatorias(lista_de_palavras, quantidade = 1):
    for x in range(quantidade):
        lista_de_palavras.append(random.choice(lista_palavras))

if __name__ == "__main__":
    main()