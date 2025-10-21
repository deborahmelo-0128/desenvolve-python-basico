import random, math
quantidade = int(input("Digite a quantidade de valores a serem gerados: ")) 
soma = 0
for i in range(quantidade):
    soma += random.randint(0, 100)

print("A raiz quadrada da soma dos valores gerados é:", math.sqrt(soma))

