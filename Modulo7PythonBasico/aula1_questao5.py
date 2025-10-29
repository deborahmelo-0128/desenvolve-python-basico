# Lê a frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais (minúsculas e maiúsculas)
vogais = "aeiouAEIOU"

# Cria uma lista para armazenar os índices das vogais
indices = []

# Percorre a frase com seus índices
for i in range(len(frase)):
    if frase[i] in vogais:
        indices.append(i)

# Exibe a quantidade de vogais e os índices
print(f"\n{len(indices)} vogais")
print(f"Índices {indices}")
