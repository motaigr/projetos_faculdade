from datetime import datetime

VALOR_BASE_DESCONTO = 50
TAXA_DESCONTO = 0.1
TAXA_IMPOSTO = 0.06
DIAS_DESCONTO = [1, 2]  # Terça-feira (1) e quarta-feira (2)
hoje = datetime.today()

subtotal = 0
qtd = -1
while qtd != 0:
    qtd = int(input("informe a quantidade: "))
    if qtd != 0:
        preco = float(input("informe o preço: "))
        subtotal += preco * qtd   
    
valor_desconto = 0
if hoje.weekday() in DIAS_DESCONTO:
    if subtotal >= VALOR_BASE_DESCONTO:
        valor_desconto = subtotal * TAXA_DESCONTO
        print(f"Desconto: R$ {valor_desconto:.2f}")
    else:
        valor_sugestão = VALOR_BASE_DESCONTO - subtotal
        print(f"Faltam R$ {valor_sugestão:.2f} para atingir o valor minimo para o desconto.")
        
valor_devido = subtotal - valor_desconto
valor_imposto = valor_devido * TAXA_IMPOSTO
print(f"Imposto: R$ {valor_imposto:.2f}")
valor_devido += valor_imposto
print(f"Total: R$ {valor_devido:.2f}")
