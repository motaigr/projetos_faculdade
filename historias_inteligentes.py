#"""Coleta as informações necessárias do usuário"""
print("=" * 50)
print("BEM-VINDO ÀS HISTÓRIAS INTELIGENTES!")
print("=" * 50)
print("\nInsira as seguintes informações:\n")
   
adjetivo = input("Um adjetivo: ")
animal = input("Um animal: ")
verbo1 = input("Um verbo (1º): ")
exclamacao = input("Uma exclamação: ")
verbo2 = input("Um verbo (2º): ")
verbo3 = input("Um verbo (3º): ")

 #"""Gera a história usando as informações coletadas"""   
print("Sua história:")
print(f"""Outro dia, eu estava em apuros. Tudo começou quando vi um {animal}
muito {adjetivo} {verbo1} no corredor. "{exclamacao.upper()}!" Eu gritei. Mas tudo
que consegui pensar foi em {verbo2} várias vezes. Por um milagre,
isso fez com que a criatura parasse, mas não antes de tentar {verbo3}
bem na frente da minha família.""")
   



