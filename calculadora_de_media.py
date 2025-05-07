#  Calcular média de um aluno e ver se está aprovado ou não 
# Solicita as notas das provas 1 e 2 para calcular a média do aluno
nota1 = float(input("Digite a nota da 1º prova: "))
nota2 = float(input("Digite a nota da 2º prova: "))
media = (nota1 + nota2) / 2

print("\n==== NOTAS ====")

print(f"Nota da 1º prova: {nota1}")
print(f"Nota da 2º prova: {nota2}")

print(f"Sua média é: {media}")

print("\n==== STATUS ====")
# irá imprimir baseado nos dados inseridos pelo usuário o status do aluno
if 10 > media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")