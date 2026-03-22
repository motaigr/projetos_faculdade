print("Bem-vindo ao sistema de empréstimos!")

print("Para solicitar um empréstimo, por favor responda às seguintes perguntas classificando de 1 a 10:")

#perguntas para avaliar o perfil do solicitante de 1 a 10
emprestimo = int(input("Qual o valor do empréstimo que você deseja solicitar? "))
historia_credito = int(input("Você tem uma boa história de crédito? "))
renda = int(input("Qual a sua renda? "))
entrada = int(input("Qual o valor da entrada que você pode dar? "))


if emprestimo >= 5:
    if historia_credito >= 7 and renda >= 7:
        pode_emprestar = True
    elif historia_credito >= 7 or renda >= 7:
        if entrada >= 5:
            pode_emprestar = True
        else:
            pode_emprestar = False
    else:
        pode_emprestar = False
else:
    if historia_credito < 4:
        pode_emprestar = False
    else:
        if renda >= 7 or entrada >= 7:
            pode_emprestar = True
        elif renda >= 4 and entrada >= 4:
            pode_emprestar = True
        else:
            pode_emprestar = False

if pode_emprestar:
    print("Parabéns! Seu empréstimo foi aprovado.")
else:
    print("Infelizmente, seu empréstimo foi negado.")