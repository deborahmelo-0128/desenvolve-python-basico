# 1. Todos os números pares entre 20 e 50
pares = [n for n in range(20, 51) if n % 2 == 0]

# 2. Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [n**2 for n in [1,2,3,4,5,6,7,8,9]]

# 3. Todos os números entre 1 e 100 que sejam divisíveis por 7
div7 = [n for n in range(1, 101) if n % 7 == 0]

# 4. Para todos os valores em range(0,30,3), escreva "par" ou "ímpar"
paridade = ["par" if n % 2 == 0 else "ímpar" for n in range(0, 30, 3)]

# Exibindo os resultados
print("1) Pares entre 20 e 50:", pares)
print("2) Quadrados de 1 a 9:", quadrados)
print("3) Números divisíveis por 7 entre 1 e 100:", div7)
print("4) Paridade de range(0,30,3):", paridade)
