#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
#brancos, nulos e válidos. 
#Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

print("Digite o número total de eleitores:")
totalEleitores = int(input())

print("Digite o número de votos brancos:")
brancos = int(input())

print("Digite o número de votos nulos:")
nulos = int(input())

print("Digite o número de votos válidos:")
validos = int(input())

print("Votos Totais: ", totalEleitores)
print("Votos Brancos:", brancos, "Porcentagem:", brancos/totalEleitores)
print("Votos Nulos:", nulos, "Porcentagem:", nulos/totalEleitores)
print("Votos Válidos", validos, "Porcentagem:", validos/totalEleitores)
