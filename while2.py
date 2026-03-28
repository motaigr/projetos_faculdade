pedir_doce = input("Posso pegar um doce? (sim/não): ").lower()

while pedir_doce != "sim":
    print("Não pode pegar um doce.")
    pedir_doce = input("Posso pegar um doce? (sim/não): ").lower()

print("Você pode pegar um doce!")