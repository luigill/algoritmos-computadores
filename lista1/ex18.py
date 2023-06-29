# Escreva um algoritmo para calcular e imprimir o número de lâmpadas necessárias para iluminar
# um determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em
# watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência
# necessária é de 18 watts por metro quadrado

print("Digite a potência da lâmpada: ")
pot = int(input())

print("Digite a largura do cômodo: ")
largura = int(input())

print("Digite a comprimento do cômodo: ")
comprimento = int(input())

areaTotalComodo = largura * comprimento

potenciaNecessaria = areaTotalComodo / 18

numLampadasNecessarias = potenciaNecessaria/pot

print("Número de lâmpadas necessárias: ", numLampadasNecessarias)