from carro_inteligente import CarroInteligente
from carro_esportivo import CarroSportivo

if __name__ == "__main__":
    # Testando CarroInteligente
    carro_inteligente = CarroInteligente(10)  # Inicializando com velocidade 10
    print("Carro Inteligente:")
    carro_inteligente.acelera()  # Aumenta a velocidade
    carro_inteligente.exibe_velocidade()  # Exibe a velocidade atual
    carro_inteligente.estaciona()  # Estaciona o carro (velocidade deve ser 0)
    print()

    # Testando CarroEsportivo
    carro_sportivo = CarroSportivo(50)  # Inicializando com velocidade 50
    print("Carro Sportivo:")
    carro_sportivo.turbo()  # Ativa o turbo, provavelmente aumenta a velocidade
    carro_sportivo.exibe_velocidade()  # Exibe a velocidade após o turbo
    carro_sportivo.freia()  # Diminui a velocidade
    carro_sportivo.exibe_velocidade()  # Exibe a velocidade após frear
