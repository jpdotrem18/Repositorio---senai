class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")

carro1 = Carro("Volkswagen", "Gol", 2022)
carro2 = Carro("Fiat", "Uno", 2015)

carro1.exibir()
carro2.exibir()