# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#correspondente em graus Celsius:

print("Digite a temperatura em Fahrenheit:")
tempF = int(input())
tempC = ((tempF - 32) / 9) * 5
print("Temperatura em Celsius: ", tempC)