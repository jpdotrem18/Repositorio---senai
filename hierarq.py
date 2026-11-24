class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        return f"O veículo {self.marca} está se movendo a até {self.velocidade_max} km/h."

class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas

    def mover(self):
        return f"O carro {self.marca} ({self.num_portas} portas) está dirigindo a até {self.velocidade_max} km/h."


class Bicicleta(Veiculo):
    def mover(self):
        return f"A bicicleta {self.marca} está sendo pedalada a até {self.velocidade_max} km/h."

veiculos = [
    Carro("Toyota", 180, 4),
    Bicicleta("Caloi", 35)
]

for v in veiculos:
    print(v.mover())