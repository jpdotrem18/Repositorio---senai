def calcular_area_retangulo(base, altura):
    "Calcula e retorna a área de um retângulo."
    return base * altura

def ler_medida(mensagem):
    "Lê um número positivo digitado pelo usuário, aceitando ponto ou vírgula."
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor <= 0:
                print("A medida deve ser maior que zero. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def main():
    print("=== CALCULADORA DE ÁREA DE RETÂNGULO ===\n")
    
    base = ler_medida("Digite o valor da base: ")
    altura = ler_medida("Digite o valor da altura: ")
    
    area = calcular_area_retangulo(base, altura)
    
    print(f"\nResultado: A área do retângulo é {area:.2f}")

if __name__ == "__main__":
    main()                                                                                                               