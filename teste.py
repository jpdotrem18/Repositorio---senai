while True:
    expr = input("Digite a conta (ou 'sair'): ")
    if expr.lower() == 'sair':
        break
    try:
        print("Resultado:", eval(expr))
    except Exception:
        print("Conta inválida!")