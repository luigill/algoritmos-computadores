# A equipe Red Bull Racing de Fórmula 1 deseja calcular o número mínimo de litros que deverá
# colocar no tanque de seu carro para que ele possa percorrer um determinado número de voltas até o
# primeiro reabastecimento. Escreva um algoritmo que leia o comprimento da pista (em metros), o
# número total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos
# desejados e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de
# litros necessários para percorrer até o primeiro reabastecimento. Observação: Considere que o
# número de voltas entre os reabastecimentos é o mesmo.

print("Digite o comprimento da pista:")
comprimentoPista = int(input())
print("Digite o número total de voltas do GP:")
totalVoltas = int(input())
print("Digite o número de reabastecimentos desejados:")
reabastecimentosDesejados = int(input())
print("Digite o consumo do carro: (Km/L)")
consumoCarro = int(input())


comprimentoTotal = comprimentoPista * totalVoltas
numVoltasPorReabastecimento = comprimentoTotal / reabastecimentosDesejados
numMinimoLitros = numVoltasPorReabastecimento / consumoCarro

print("Número mínimo de litros: ", numMinimoLitros)
