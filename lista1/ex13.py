# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, 
# escrever um algoritmo para ler o custo de fábrica de um carro, 
# calcular e escrever o custo final ao consumidor.

print("Digite o custo de fábrica do carro:")
custoFabrica = int(input())
percentDistribuidor = 28 / 100
impostos = 45 / 100

print("Custo final do carro: ", (custoFabrica + (custoFabrica * percentDistribuidor) + (custoFabrica * impostos)))