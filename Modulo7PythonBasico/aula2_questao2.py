# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Substitui cada vogal por '*'
nova_frase = ""
for letra in frase:
    if letra in vogais:
        nova_frase += "*"
    else:
        nova_frase += letra

# Exibe o resultado
print("Frase criptografada:", nova_frase)
