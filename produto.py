class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
 
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade: {self.quantidade}")

    def valor_total(self):
        return self.preco * self.quantidade
    def aplicar_desconto(self, pecentual):
        self.preco *= (1-percentual / 100)
        print(f"Desconto aplicado! Novo preco: R${self.preco}")

    def vender(self, quantidade):
        if quantidade > self.quantidade:
            print ("Estoque insuficiente!")
        else:
            self.quantidade -= quantidade
            print(f"Vendido {quantidade} x {self.nome}.Estoque restante: {self.quantidade}")   

    def repor_quantidade(self,quantidade):
        self.quantidade += quantidade
        print(f"Novo estoque: {self.quantidade}")          

        p1 = produto("fubá", "alimentos", 2.99, 20)
        p2 = produto("caneta", "papelaria", 1.99, 30)

        p1.exibir()
        p2.exibir()

        p1.vender(5) 