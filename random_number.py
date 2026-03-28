import random

continuar_jogando = "sim"
while continuar_jogando == "sim":

    numero_aleatorio = random.randint(1, 100)
    quantidade_tentativas = 0

    errou = True
    while errou:
        palpite = int(input("Digite seu palpite: "))
        quantidade_tentativas += 1
        if palpite > numero_aleatorio:
            print("Menor")
        elif palpite < numero_aleatorio:
            print("Maior")
        else:
            print("Parabéns! Você acertou!")
            print(f"Quantidade de tentativas: {quantidade_tentativas}")
            errou = False
    continuar_jogando = input("Deseja jogar novamente? (sim/não): ").lower()