# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
# mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
# efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
# vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
# vendedor.

print("Número de carros vendidos:")
numCarrosVendidos = int(input())
print("Valor total de vendas:")
totalVendas = int(input())
print("Salário fixo:")
salario = int(input())
print("Valor recebido por carro vendido:")
valorCarroVendido = int(input())

salarioFinal = salario + (valorCarroVendido * numCarrosVendidos) + (0.05 * totalVendas)
print("Salário Final: R$", salarioFinal)