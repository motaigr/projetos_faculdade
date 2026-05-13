from math import pi

def carregar_modelos_das_latas():

    modelo = [
        ["#1 Piquenique", 6.83, 10.16, 0.28],
        ["#1 Grande", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cilindro", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z pequena", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]
    return modelo


def main():
    
    lista_modelos_latas = carregar_modelos_das_latas()

    melhor_armazenamento = 0
    melhor_custo = 0

    dados_melhor_armazenamento = []
    dados_melhor_custo = []

    print("-" * 50)  
    #print("Modelo da lata \t|  Armazenamento \t|  Custo" )
    print(f"{'Modelo da lata':<20} | {'Armazenamento':>13} | {'Custo':>10}")

    for modelo in lista_modelos_latas:
        eficiencia_armazenamento = calcular_eficiencia_de_armazenamento(modelo[0], modelo[1], modelo[2])
        eficiencia_custo = calcular_eficiencia_de_custo(modelo[0], modelo[1], modelo[2], modelo[3])

        if eficiencia_armazenamento > melhor_armazenamento:
            dados_melhor_armazenamento = modelo
            melhor_armazenamento = eficiencia_armazenamento
            

        if eficiencia_custo > melhor_custo:
            dados_melhor_custo = modelo
            melhor_custo = eficiencia_custo

        print(f"{modelo[0]:<20} | {eficiencia_armazenamento:>13.2f} | {eficiencia_custo:>10.2f}")
    print("-" * 50)      
    print(f"Melhor eficiencia de armazenamento é da lata: {dados_melhor_armazenamento[0]}")
    print(f"Melhor eficiencia de custo é da lata: {dados_melhor_custo[0]}")


def calcular_volume(p_raio, p_altura):
    volume = pi * (p_raio ** 2) * p_altura
    return volume

def calcular_area_da_superficie(p_raio, p_altura):
    area = 2 * pi * p_raio * (p_raio + p_altura)
    return area

def calcular_eficiencia_de_armazenamento(nome_lata, raio, altura):
    volume = calcular_volume(raio, altura)
    area = calcular_area_da_superficie(raio, altura)
    eficiencia = volume / area
    return eficiencia

def calcular_eficiencia_de_custo(nome_lata, raio, altura, custo):
    volume = calcular_volume(raio, altura)
    eficiencia = volume / custo
    return eficiencia
    
    
main()