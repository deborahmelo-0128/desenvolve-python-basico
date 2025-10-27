# Recebe as listas do usuário (valores separados por espaço)
lista1 = [int(x) for x in input("Digite os valores da primeira lista separados por espaço: ").split()]
lista2 = [int(x) for x in input("Digite os valores da segunda lista separados por espaço: ").split()]

# Combina as listas de forma alternada
lista_combinada = []
tamanho_maior = max(len(lista1), len(lista2))

for i in range(tamanho_maior):
    if i < len(lista1):
        lista_combinada.append(lista1[i])
    if i < len(lista2):
        lista_combinada.append(lista2[i])

# Exibe o resultado
print("\nPrimeira lista:", lista1)
print("Segunda lista:", lista2)
print("Lista combinada:", lista_combinada)
