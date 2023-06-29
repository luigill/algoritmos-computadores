# Escreva um algoritmo para ler as dimensões de uma cozinha retangular (comprimento, largura e
# altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
# paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
# azulejos possui 1.5 m2.

print("Digite o comprimento da sala:")
comprimento = int(input())
print("Digite a largura da sala:")
largura = int(input())
print("Digite a altura da sala:")
altura = int(input())

parede1 = comprimento * altura
parede2 = largura * altura

totalParedeCoberta = (2*parede1) + (2*parede2)

caixasAzulejos = totalParedeCoberta / 1.5

print("Caixas de azulejos necessárias: ", caixasAzulejos)