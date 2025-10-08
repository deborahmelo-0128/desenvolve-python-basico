valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
resultado = []

restante = valor
for nota in notas:
    quantidade = restante // nota
    resultado.append(quantidade)
    restante = restante % nota

for i in range(len(notas)):
    print(f"{resultado[i]} nota(s) de R${notas[i]},00")