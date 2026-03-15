primeiro_numero = int(input("Escolha um numero entre 1 e 10: "))
segundo_numero = int(input("Escolha outro numero entre 1 e 10: "))

if primeiro_numero > segundo_numero:
    print("O primeiro numero é maior")

elif primeiro_numero < segundo_numero:
    print("O primeiro numero é menor")

else:
    print("Você escolheu um numero igual")


animal = input("Qual seu animal favorito? ")
animal = animal.lower()

if animal == "cachorro":
    print("Esse também é o meu animal favorito!")
else:
    print("esse não é o meu animal favorito.")
