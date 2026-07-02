nome = input("Digite o nome do aluno: ")

notas = []

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n===== RELATÓRIO =====")
print("Aluno:", nome)
print("Notas:", notas)
print("Média:", round(media, 2))
print("Situação:", situacao)
