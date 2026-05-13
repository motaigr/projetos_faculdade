#adicionado a opção de compra e registro do número de telefone no arquivo volumes.txt, caso o usuário queira comprar os pneus.

from datetime import datetime
import math

largura_pneu = float(input("Digite a largura do pneu em mm: "))
proporcao_pneu = float(input("Digite a proporção do pneu: "))
diametro_pneu = float(input("Digite o diâmetro da roda em polegadas: "))

# Calcula o volume do pneu
volume = (math.pi * largura_pneu**2 * proporcao_pneu * (largura_pneu * proporcao_pneu + 2540 * diametro_pneu)) / 10000000000

data_atual = datetime.now()

print(f"O volume aproximado é de {volume:.2f} litros")

with open("volumes.txt", "at", encoding="utf-8") as arquivo:
    print(f"{data_atual:%Y-%m-%d}, {largura_pneu}, {proporcao_pneu}, {diametro_pneu}, {volume:.2f}", file=arquivo)

compra = input("Deseja comprar os pneus? (sim/não): ")
with open("volumes.txt", "at", encoding="utf-8") as arquivo:
    if compra.lower() == 'sim':
        numero_de_telefone = input("Digite seu número de telefone para contato: ")
        print(f"{data_atual:%Y-%m-%d}, {largura_pneu}, {proporcao_pneu}, {diametro_pneu}, {volume:.2f}, {numero_de_telefone}", file=arquivo)
    else:
        print(f"{data_atual:%Y-%m-%d}, {largura_pneu}, {proporcao_pneu}, {diametro_pneu}, {volume:.2f}", file=arquivo)