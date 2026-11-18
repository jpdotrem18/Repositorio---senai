def maior_de_tres(num1, num2, num3):
    "Recebe três números e retorna o maior deles sem usar max()."
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def ler_numero(mensagem):
    "Lê um número válido digitado pelo usuário, aceitando ponto ou vírgula."
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def main():
    print("=== ENCONTRAR O MAIOR DE TRÊS NÚMEROS ===\n")
    
    n1 = ler_numero("Digite o primeiro número: ")
    n2 = ler_numero("Digite o segundo número: ")
    n3 = ler_numero("Digite o terceiro número: ")
    
    maior = maior_de_tres(n1, n2, n3)
    
    print(f"\nResultado: O maior número entre os três é {maior:g}")

if __name__ == "__main__":
    main()