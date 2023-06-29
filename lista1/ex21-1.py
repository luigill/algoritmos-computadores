# Leitura dos dados
comprimento_pista = float(input("Digite o comprimento da pista (em metros): "))
numero_voltas_total = int(input("Digite o número total de voltas a serem percorridas no grande prêmio: "))
numero_reabastecimentos = int(input("Digite o número de reabastecimentos desejados: "))
consumo_carro = float(input("Digite o consumo de combustível do carro (em Km/L): "))

# Cálculo do número mínimo de litros necessários
distancia_total = comprimento_pista * numero_voltas_total
distancia_reabastecimento = distancia_total / (numero_reabastecimentos + 1)
litros_necessarios = distancia_reabastecimento / consumo_carro

# Exibição do resultado
print("Número mínimo de litros necessários até o primeiro reabastecimento: {:.2f} litros".format(litros_necessarios))
