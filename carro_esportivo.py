from carro import Carro

class CarroSportivo(Carro):
    def __inir__(self, velocidade_inicial):
      super().__init__(velocidade_inicial)

    def turbo(self):
        self.velocidade += 10
        print("turbo ativado| A velocidade aumentou em 10 km/h")