# Solicita uma frase do usuário
frase = input("Digite uma frase: ").lower()

# Define vogais e consoantes
vogais = "aeiou"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# 1. Lista de vogais da frase, ordenada alfabeticamente
lista_vogais = sorted([letra for letra in frase if letra in vogais])

# 2. Lista de consoantes da frase (removendo espaços)
lista_consoantes = [letra for letra in frase if letra in alfabeto and letra not in vogais]

# Exibe os resultados
print("\nVogais (ordenadas):", lista_vogais)
print("Consoantes (sem espaços):", lista_consoantes)
