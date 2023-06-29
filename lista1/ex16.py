# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. 

print("Digite a primeira nota:")
nota1 = int(input())
print("Digite a segunda nota:")
nota2 = int(input())
print("Digite a terceira nota:")
nota3 = int(input())

mediaFinal = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
print("Média Final: ", mediaFinal)