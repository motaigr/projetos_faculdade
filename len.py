palavra = "compromisso"

for letra in palavra:
    if letra.lower() == "o":
        print(letra.upper())
    else:
        print(letra.lower())



palavra = "compromisso"
letra_favorita = input("Digite sua letra favorita: ")

for letra in palavra:
    if letra.lower() == letra_favorita.lower():
        print(letra.upper(), end="")
    else:
        print(letra.lower(), end="")

print()  # Para adicionar uma nova linha após o loop


palavra = "compromisso"
letra_favorita = input("Digite sua letra favorita: ")

for letra in palavra:
    if letra.lower() == letra_favorita.lower():
        print("_", end="")
    else:
        print(letra.lower(), end="")