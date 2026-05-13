def main():
    odometro_inicial = int(input("Digite o odômetro inicial em quilometros: "))
    odometro_final = int(input("Digite o odômetro final em quilometros: "))
    litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))

    mpg = milhas_por_galao(odometro_final, odometro_inicial, litros_consumidos)
    kpl = quilometros_por_litro(odometro_final, odometro_inicial, litros_consumidos)

    print(f"Consumo em quilômetros por litro: {kpl:.1f}") 
    print(f"Consumo em milhas por galão: {mpg:.2f}")
  

def milhas_por_galao (km_final, km_inicial, litros):
    consumo =  km_final - km_inicial
    milhas = consumo / 1.609
    galoes = litros * 0.26417
    return milhas / galoes

def quilometros_por_litro (km_final, km_inicial, litros):
    consumo =  km_final - km_inicial
    consumo_por_litro = consumo / litros
    return consumo_por_litro


main()