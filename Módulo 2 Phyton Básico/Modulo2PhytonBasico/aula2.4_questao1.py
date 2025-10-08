# Solicita ao usuário o comprimento do terreno (em metros)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Solicita ao usuário a largura do terreno (em metros)
largura = int(input("Digite a largura do terreno (em metros): "))

# Solicita ao usuário o preço do metro quadrado (em reais)
preco_m2 = float(input("Digite o preço do metro quadrado (em reais): "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura
# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Exibe o resultado formatado conforme o exemplo
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")