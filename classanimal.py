class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "..."

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} diz: au au!"

class Gato(Animal):
    def fazer_som(self):
        s = super().fazer_som()
        return f"{self.nome}: miau! ({s})"

animais = [Cachorro("Rex"), Gato("Yuumi")]
for a in animais:
    print(a.fazer_som())