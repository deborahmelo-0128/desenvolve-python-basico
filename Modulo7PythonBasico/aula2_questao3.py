import string  # para remover pontuação

while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")

    # Encerra o programa se o usuário digitar "Fim"
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break

    # Converte para minúsculas
    frase_limpa = frase.lower()

    # Remove espaços e pontuação
    for char in string.punctuation + " ":
        frase_limpa = frase_limpa.replace(char, "")

    # Verifica se é palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print("É um palíndromo!\n")
    else:
        print("Não é um palíndromo.\n")
