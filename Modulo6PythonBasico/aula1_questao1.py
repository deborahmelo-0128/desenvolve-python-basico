import random

# Gera 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Mostra a lista ordenada (sem modificar a original)
print("Lista ordenada:", sorted(valores))

# Mostra a lista original
print("Lista original:", valores)

# Encontra o índice do maior e do menor valor
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

# Exibe os índices
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)




