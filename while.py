num_positivo = int(input("Digite um número positivo: "))
while num_positivo <= 0:
    print("Número inválido. Digite um número positivo.")
    num_positivo = int(input("Digite um número positivo: "))

print(f"O número é: {num_positivo}")