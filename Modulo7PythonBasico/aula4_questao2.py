import re

# Nome dos arquivos
arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

# Lê o conteúdo do arquivo 'frase.txt'
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Remove caracteres não alfabéticos e divide em palavras
# re.findall() captura apenas sequências de letras (a-z ou A-Z)
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", conteudo)

# Salva cada palavra em uma linha no arquivo 'palavras.txt'
with open(arquivo_saida, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# Lê novamente o arquivo 'palavras.txt' e imprime o conteúdo
with open(arquivo_saida, "r", encoding="utf-8") as f:
    print(f.read())
