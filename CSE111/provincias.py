def main():
    print("Lista de Províncias:")
    ler_provincias()

def ler_provincias():
    with open("provincias.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.read().splitlines()
  
    lista.pop(0)  # Remove o cabeçalho
    lista.pop()    
    

    for i in range(len(lista)):
        if lista[i] == "AB":
            lista[i] = "Alberta"

    contador = lista.count("Alberta")

    print(lista) 
    print(f"Alberta aparece {contador} vezes na lista.")

if __name__ == "__main__":
    main()