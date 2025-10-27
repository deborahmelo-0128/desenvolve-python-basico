import random

# 1. Criar lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# 2. Dividir a lista em intervalos (vamos usar intervalos de 5 elementos)
tamanho_intervalo = 5
intervalos = [lista[i:i+tamanho_intervalo] for i in range(0, len(lista), tamanho_intervalo)]

# 3. Contar quantos números negativos há em cada intervalo
contagens_negativos = [sum(1 for n in intervalo if n < 0) for intervalo in intervalos]

# 4. Encontrar o índice do intervalo com mais números negativos
indice_maior = contagens_negativos.index(max(contagens_negativos))

# 5. Apagar o intervalo correspondente da lista original com 'del'
inicio = indice_maior * tamanho_intervalo
fim = inicio + tamanho_intervalo
del lista[inicio:fim]

# 6. Mostrar resultado
print("Lista após deletar o intervalo com mais negativos:", lista)
