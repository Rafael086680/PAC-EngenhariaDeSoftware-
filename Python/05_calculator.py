print("=== Calculadora Python ===")

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
op = input("Operação (+, -, *, /): ")

if op == "+":
    resultado = a + b
elif op == "-":
    resultado = a - b
elif op == "*":
    resultado = a * b
elif op == "/":
    resultado = a / b
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)
