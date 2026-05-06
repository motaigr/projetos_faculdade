"""
Quando você se exercita fisicamente para fortalecer seu coração,
deve manter sua frequência cardíaca dentro de uma faixa por pelo menos 20
minutos. Para encontrar essa faixa, subtraia sua idade de 220. Essa
diferença é sua frequência cardíaca máxima por minuto. Seu coração
simplesmente não baterá mais rápido que esse máximo (220 - idade).
Ao se exercitar para fortalecer seu coração, você deve manter sua
frequência cardíaca entre 65% e 85% da frequência cardíaca máxima.
""" 
idade = int(input("Digite sua idade: "))
frequencia_cardiaca_maxima = 220 - idade
frequencia_cardiaca_minima = frequencia_cardiaca_maxima * 0.65
frequencia_cardiaca_maxima_exercicio = frequencia_cardiaca_maxima * 0.85
print(f"Ao se exercitar para fortalecer seu coração, você deve manter sua frequência cardíaca entre {frequencia_cardiaca_minima:.2f} e {frequencia_cardiaca_maxima_exercicio:.2f} batimentos por minuto.")