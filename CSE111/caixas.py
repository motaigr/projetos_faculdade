import math

itens = int(input("Digite o número de itens fabricados: "))
itens_por_caixa = int(input("Digite o número de itens que cabem em cada caixa: "))

caixas_necessarias = math.ceil(itens / itens_por_caixa)
print(f"Para {itens} itens, empacontando {itens_por_caixa} por caixas, você precisará de {caixas_necessarias} caixas.")
