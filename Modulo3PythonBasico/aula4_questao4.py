# Sistema de cálculo de frete expressa

distancia = float(input("Informe a distância da entrega em km: "))
peso = float(input("Informe o peso do pacote em kg: "))

# Determina o valor por kg conforme a distância
if distancia <= 100:
    valor_por_kg = 1.0
elif distancia <= 300:
    valor_por_kg = 1.5
else:
    valor_por_kg = 2.0

# Calcula o valor base do frete
valor_frete = peso * valor_por_kg

# Acrescenta taxa extra se o peso for superior a 10 kg
if peso > 10:
    valor_frete += 10.0

print(f"Valor do frete: R${valor_frete:.2f}")


