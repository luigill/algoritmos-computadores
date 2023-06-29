# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço
# do combustível é de R$ 4.90, escreva um algoritmo para ler: a marcação do odômetro (Km) no início
# do dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total
# (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido)
# do dia.

PRECO_COMBUSTIVEL = 4.90

print("Digite a marcação do odômetro no começo do dia:")
comecoDia = int(input())
print("Digite a marcação do odômetro no final do dia:")
finalDia = int(input())
print("Digite quantos litros de gasolina foram gastos:")
litrosGasolina = int(input())
print("Digite o valor total recebido dos passageiros:")
valorTotalRecebido = int(input())

kmAndados = finalDia - comecoDia

mediaConsumo = kmAndados / litrosGasolina
gastoGasolina = litrosGasolina * PRECO_COMBUSTIVEL
lucro = valorTotalRecebido - gastoGasolina

print("Média de consumo do carro: ", mediaConsumo)
print("Lucro do dia: R$",lucro)

