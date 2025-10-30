import re
import unicodedata

# Caminho do arquivo
arquivo = "estomago.txt"

# === Função para abrir com codificação automática ===
def abrir_arquivo_com_fallback(caminho):
    """Tenta abrir o arquivo em UTF-8 e, se falhar, tenta Latin-1."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.readlines()
    except UnicodeDecodeError:
        with open(caminho, "r", encoding="latin-1") as f:
            return f.readlines()

# === Função auxiliar para remover acentos ===
def normalizar(texto):
    """Remove acentos e converte para minúsculas."""
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower()

# === Função principal ===
def analisar_roteiro():
    try:
        linhas = abrir_arquivo_com_fallback(arquivo)
    except FileNotFoundError:
        print(f"❌ Arquivo '{arquivo}' não encontrado no diretório atual.")
        return

    # 1️⃣ Primeiras 25 linhas
    print("=== Primeiras 25 linhas do roteiro ===\n")
    for i, linha in enumerate(linhas[:25], start=1):
        print(f"{i:03d}: {linha.strip()}")
    
    # 2️⃣ Número total de linhas
    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas: {num_linhas}")

    # 3️⃣ Linha com maior número de caracteres
    if num_linhas > 0:
        linha_maior = max(linhas, key=len)
        print("\n=== Linha com maior número de caracteres ===")
        print(linha_maior.strip())
        print(f"(Comprimento: {len(linha_maior)} caracteres)")
    else:
        print("\nO arquivo está vazio!")

    # 4️⃣ Contagem das menções a 'Nonato' e 'Íria'
    texto = "".join(linhas)
    
    # Captura apenas palavras compostas por letras (com acentos)
    palavras = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", texto)
    palavras_normalizadas = [normalizar(p) for p in palavras]

    cont_nonato = palavras_normalizadas.count("nonato")
    cont_iria = palavras_normalizadas.count("iria")

    print("\n=== Contagem de menções ===")
    print(f"Menções a 'Nonato': {cont_nonato}")
    print(f"Menções a 'Íria': {cont_iria}")

# === Execução ===
if __name__ == "__main__":
    analisar_roteiro()
