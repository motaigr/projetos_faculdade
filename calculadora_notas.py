media = int(input("Digite a média final do aluno: (1-100) "))
nota  = ""
modificador = ""
ultimo_digito = media % 10

if ultimo_digito >= 7:
    modificador = "+"
elif ultimo_digito <= 3:
    modificador = "-"

if media >= 90:
    if ultimo_digito < 3:
        nota = "A" + modificador
    else:
        nota = "A"
elif media >= 80:
    nota = "B" + modificador
elif media >= 70:
    nota = "C" + modificador
elif media >= 60:
    nota = "D" + modificador
else:
    nota = "F"

print(f"A nota do aluno é {nota}")