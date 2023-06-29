# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
# reajuste. Calcular e escrever o valor do novo salário.

print("Digite o salário atual:")
salario = int(input())
print("Digite o percentual de reajuste:")
reajuste = int(input())
reajusteCalculo = reajuste / 100
salarioNovo = salario + (salario * reajusteCalculo)
print("Novo Salário: R$",salarioNovo )
