import random

# Gera aleatoriamente um número entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera uma lista com 'num_elementos' valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula a soma e a média dos valores
soma = sum(elementos)
media = soma / num_elementos

# Exibe os resultados
print("Quantidade de elementos:", num_elementos)
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", round(media, 2))
