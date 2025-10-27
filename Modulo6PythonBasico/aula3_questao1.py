# Solicita uma quantidade indefinida de números inteiros do usuário
numeros = []

print("Digite números inteiros (digite 'fim' para encerrar):")

while True:
    entrada = input("Número: ")
    if entrada.lower() == 'fim':
        break
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

# Verifica se há pelo menos 4 números
if len(numeros) < 4:
    print("\nÉ necessário digitar pelo menos 4 números para prosseguir.")
else:
    print("\nLista original:", numeros)
    print("3 primeiros elementos:", numeros[:3])
    print("2 últimos elementos:", numeros[-2:])
    print("Lista invertida:", numeros[::-1])
    print("Elementos de índice par (0, 2, 4...):", numeros[::2])
    print("Elementos de índice ímpar (1, 3, 5...):", numeros[1::2])
