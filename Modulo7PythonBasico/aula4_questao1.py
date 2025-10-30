import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Abre (ou cria) o arquivo e grava a frase nele
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo
caminho_completo = os.path.abspath(nome_arquivo)

# Exibe o caminho completo
print(f"Arquivo salvo em: {caminho_completo}")
