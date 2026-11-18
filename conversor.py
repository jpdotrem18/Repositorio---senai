def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def km_para_milhas(km):
    return km * 0.621371

def kg_para_libras(kg):
    return kg * 2.20462

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def iniciar_programa():
    while True:
        print("\n=== CONVERSOR DE UNIDADES ===")
        print("1. Celsius para Fahrenheit")
        print("2. Quilômetros para Milhas")
        print("3. Quilogramas para Libras")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        elif opcao == "1":
            val = ler_numero("Digite a temperatura em Celsius: ")
            print(f"Resultado: {val:.2f} °C = {celsius_para_fahrenheit(val):.2f} °F")
       
        elif opcao == "2":
            val = ler_numero("Digite a distância em Quilômetros: ")
            print(f"Resultado: {val:.2f} km = {km_para_milhas(val):.2f} milhas")
    
        elif opcao == "3":
            val = ler_numero("Digite o peso em Quilogramas: ")
            print(f"Resultado: {val:.2f} kg = {kg_para_libras(val):.2f} lbs")
       
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_programa()