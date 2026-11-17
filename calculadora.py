def somar(a,b): return a + b
def subtrair(a,b): return a -b
def multiplicar(a,b): return a * b
def dividir (a,b):
    if b == 0: return "erro!"
    return a/b
while True:
    op = input("Operaçao (+-*/0)")
    if op == "0": break 
    a = float(input("num 1:"))
    b = float(input("num 2:"))
   