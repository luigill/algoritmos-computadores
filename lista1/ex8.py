ANO = 365
MES = 30

print("Digite os anos:")
anos = int(input())
print("Digite os meses:")
meses = int(input())
print("Digite os dias:")
dias = int(input())

anosEmDias = anos * ANO
mesesEmDias = meses * MES

diasDeVida = anosEmDias + mesesEmDias + dias
print("Dias Vividos")
print(diasDeVida)