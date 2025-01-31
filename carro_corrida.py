from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)
    
    # Override do método acelerar	
    def acelera(self):
        self.velocidade += 5
        print("Aceleração de corrida! A velocidade aumentouu em 5 km/h")
