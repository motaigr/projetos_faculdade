# Jogo de adivinhação de palavras, onde é gerada uma palavra aleatoria e o jogador precisa adivinhar qual é ela. O jogador recebe dicas conforme acerta as letras da palavra.
# O jogo sorteia uma palavra aleatória a cada partida a partir de uma lista de palavras.
import random

palavras = ["mosias", "nefi", "helama", "moroni", "alma"]
palavra_secreta = random.choice(palavras)

print("Bem-vindo ao jogo de adivinhação de palavras!")
print()

dica = ""
for i in range(len(palavra_secreta)):
    dica += "_ "
print("Sua dica é: " + dica)

tentativas = 0

while True:
    palpite = input("Qual é o seu palpite? ").lower()
    tentativas += 1

    if len(palpite) != len(palavra_secreta):
        print("Desculpe, o palpite precisa ter o mesmo número de letras que a palavra secreta.")
        print()
    elif palpite == palavra_secreta:
        print("Parabéns! Você adivinhou!")
        print(f"Você precisou de {tentativas} palpites.")
        break
    else:
        dica = ""
        for i in range(len(palpite)):
            letra = palpite[i]
            if letra == palavra_secreta[i]:
                dica += letra.upper() + " "
            elif letra in palavra_secreta:
                dica += letra.lower() + " "
            else:
                dica += "_ "
        print("Sua dica é: " + dica)