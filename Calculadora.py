#adicionado por mim para dar uma melhor visualização do programa, não é necessário para o funcionamento da calculadora
print("=" * 50)
print("Bem-vindo à calculadora de refeições!")
print("=" * 50)

preco_crianca = float(input("Qual o preço da refeição para uma criança? "))
preco_adulto = float(input("Qual o preço da refeição para um adulto? "))
qtd_criancas = int(input("Há quantas crianças? "))
qtd_adultos = int(input("Há quantos adultos? "))
valor_total = (preco_crianca * qtd_criancas) + (preco_adulto * qtd_adultos)

print(f"Subtotal: R$ {valor_total:.2f}")

imposto_vendas = float(input("Qual a taxa de imposto sobre vendas? "))
imposto_final = valor_total * (imposto_vendas / 100)
print(f"Imposto sobre vendas: R$ {imposto_final:.2f}")
total_com_imposto = valor_total + imposto_final
print(f"Valor total com imposto: R$ {total_com_imposto:.2f}")

valor_pago = float(input("Qual o valor de pagamento? "))
print(f"Seu troco será de: R$ {valor_pago - total_com_imposto:.2f}")


print("=" * 50) #adicionado por mim para dar uma melhor visualização do programa, não é necessário para o funcionamento da calculadora
print("Obrigado por usar a calculadora de refeições!")
print("=" * 50)