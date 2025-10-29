# Solicita a frase e a palavra objetivo
texto = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ")

# Normaliza tudo para minúsculas e remove espaços extras
texto = texto.lower().split()
palavra = palavra.lower()

# Ordena os caracteres da palavra objetivo
anagrama_base = sorted(palavra)

# Lista para armazenar os anagramas encontrados
anagramas = []

# Verifica palavra por palavra na frase
for p in texto:
    if sorted(p) == anagrama_base:
        anagramas.append(p)

# Exibe o resultado
if anagramas:
    print(f"Anagramas encontrados: {anagramas}")
else:
    print("Nenhum anagrama encontrado.")
