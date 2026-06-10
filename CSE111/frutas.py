def main():
    # Cria e exibe uma lista chamada frutas.
    lista_de_frutas = ["pêra", "banana", "maçã", "manga"]
    print(f"original: {lista_de_frutas}")

    lista_de_frutas.sort()
    print(f"ordenada: {lista_de_frutas}")

    lista_de_frutas.append("laranja")
    print(f"com laranja: {lista_de_frutas}")

    indice = lista_de_frutas.index("maçã")
    lista_de_frutas.insert(indice, "cereja")
    print(f"índice da maçã: {indice}")
    print(f"com cereja: {lista_de_frutas}")

    lista_de_frutas.remove("banana")
    print(f"sem banana: {lista_de_frutas}")

    lista_de_frutas.pop()
    print(f"sem o ultimo: {lista_de_frutas}")

    lista_de_frutas.sort()
    print(f"classificada: {lista_de_frutas}")

    lista_de_frutas.clear()
    print(f"limpa: {lista_de_frutas}")

if __name__ == "__main__":
    main()