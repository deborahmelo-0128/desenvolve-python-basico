import random

# Gera duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria a lista de interseção (sem duplicatas)
interseccao = sorted(list(set(lista1) & set(lista2)))

# Exibe as listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista interseção (ordenada e sem duplicatas):", interseccao)
print()

# Mostra a quantidade de vezes que cada elemento da interseção aparece em cada lista
print("Contagem de ocorrências:")
for elemento in interseccao:
    print(f"Valor {elemento}: aparece {lista1.count(elemento)} vez(es) na lista1 e {lista2.count(elemento)} vez(es) na lista2")
