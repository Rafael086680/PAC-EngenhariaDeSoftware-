nome = input("Seu nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classif = "Abaixo do peso"
elif imc < 25:
    classif = "Normal"
elif imc < 30:
    classif = "Sobrepeso"
else:
    classif = "Obesidade"

print(f"{nome}, seu IMC é {imc:.1f} - {classif}")
