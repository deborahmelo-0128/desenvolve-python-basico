import random
import os
import unicodedata
import re

# Nomes dos arquivos (mesmo diretório)
ARQ_PALAVRAS = "gabarito_forca.txt"
ARQ_ENFORCADO = "gabarito_enforcado.txt"

# === util: abrir arquivo tentando várias codificações ===
def ler_texto_com_fallback(caminho, encs=("utf-8", "latin-1")):
    last_exc = None
    for enc in encs:
        try:
            with open(caminho, "r", encoding=enc) as f:
                return f.read()
        except FileNotFoundError:
            raise
        except Exception as e:
            last_exc = e
            continue
    # se chegou aqui, nenhuma codificação funcionou
    raise last_exc

# === util: parsear estágios do enforcado de modo tolerante ===
def parsear_estagios_enforcado(texto):
    """
    Separa por blocos separados por uma linha em branco (ou mais).
    Retorna lista de blocos (cada bloco é string).
    """
    linhas = texto.splitlines()
    blocos = []
    buffer = []
    for ln in linhas:
        if ln.strip() == "":
            if buffer:
                blocos.append("\n".join(buffer))
                buffer = []
        else:
            buffer.append(ln.rstrip())
    if buffer:
        blocos.append("\n".join(buffer))
    # se não foram encontrados blocos, tenta dividir por '=========' (fallback)
    if not blocos:
        parts = [p.strip() for p in texto.split("=========") if p.strip()]
        blocos = [p + "\n=========" for p in parts]
    return blocos

# === util: remover acentos e normalizar para comparação ===
def normalizar(s):
    nfkd = unicodedata.normalize("NFKD", s)
    sem = "".join(ch for ch in nfkd if not unicodedata.combining(ch))
    return sem.casefold()

# === imprime enforcado com clamp de índice ===
def imprime_enforcado(estagios, erros):
    """
    Recebe lista de estagios e número de erros (0..6).
    Garante que não dê IndexError — se erros > último índice, mostra último estágio.
    """
    if not estagios:
        print("(enforcado: estágios não carregados)")
        return
    idx = max(0, min(erros, len(estagios) - 1))
    print(estagios[idx])

# === carrega palavras do arquivo (uma por linha) ===
def carregar_palavras(caminho):
    texto = ler_texto_com_fallback(caminho)
    palavras = [ln.strip().lower() for ln in texto.splitlines() if ln.strip()]
    return palavras

# === carrega enforcado do arquivo ===
def carregar_estagios(caminho):
    texto = ler_texto_com_fallback(caminho)
    estagios = parsear_estagios_enforcado(texto)
    # strip final/ inicial de cada bloco
    estagios = [e.strip("\n") for e in estagios]
    return estagios

# === jogo principal ===
def jogar_forca():
    # verificar existência dos arquivos
    for caminho in (ARQ_PALAVRAS, ARQ_ENFORCADO):
        if not os.path.exists(caminho):
            print(f"❌ Arquivo não encontrado: '{caminho}'. Coloque-o no mesmo diretório do script.")
            return

    try:
        palavras = carregar_palavras(ARQ_PALAVRAS)
    except FileNotFoundError:
        print(f"❌ '{ARQ_PALAVRAS}' não encontrado.")
        return
    except Exception as e:
        print(f"❌ Erro ao ler '{ARQ_PALAVRAS}': {e}")
        return

    try:
        estagios = carregar_estagios(ARQ_ENFORCADO)
    except FileNotFoundError:
        print(f"❌ '{ARQ_ENFORCADO}' não encontrado.")
        return
    except Exception as e:
        print(f"❌ Erro ao ler '{ARQ_ENFORCADO}': {e}")
        return

    if not palavras:
        print(f"❌ Lista de palavras vazia em '{ARQ_PALAVRAS}'. Coloque pelo menos uma palavra.")
        return

    # garantir que há pelo menos 1 estágio; se houver menos que 7, avisar (mas ainda joga)
    if len(estagios) < 2:
        print("⚠️  Arquivo do enforcado parece mal formatado (poucos estágios). Verifique 'gabarito_enforcado.txt'.")
    max_erros = 6  # conforme enunciado
    # se o arquivo tiver menos estágios que max_erros, usaremos o último estágio repetidamente
    # (imprime_enforcado já clampa o índice)

    palavra = random.choice(palavras).strip()
    letras_descobertas = ["_"] * len(palavra)
    letras_tentadas = set()
    erros = 0

    print("\n🎯 Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")
    print(" ".join(letras_descobertas))

    # loop principal
    while erros < max_erros and "_" in letras_descobertas:
        tentativa = input("\nDigite uma letra: ").strip().lower()
        if tentativa == "":
            print("⚠️  Entrada vazia. Digite uma letra.")
            continue
        if len(tentativa) != 1:
            print("⚠️  Digite apenas UMA letra por vez.")
            continue
        if not tentativa.isalpha():
            print("⚠️  Digite apenas letras (a-z).")
            continue
        if tentativa in letras_tentadas:
            print("🔁 Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.add(tentativa)

        # comparar normalizando ambos (para lidar com acentos se quiser)
        # porém: se a palavra tiver acentos, queremos revelar a letra exatamente (ex: 'í' com 'i'?)
        # Neste exemplo, exige-se correspondência exata (i != í). Se preferir que 'i' revele 'í', descomente a normalização abaixo.
        # Para manter comportamento clássico, vou comparar sem normalização de acentos por padrão.
        if tentativa in palavra:
            print("✅ Acertou!")
            for i, ch in enumerate(palavra):
                if ch == tentativa:
                    letras_descobertas[i] = ch
        else:
            print("❌ Errou!")
            erros += 1
            imprime_enforcado(estagios, erros)

        print("\nPalavra: " + " ".join(letras_descobertas))
        print("Letras tentadas: " + ", ".join(sorted(letras_tentadas)))
        print(f"Erros: {erros}/{max_erros}")

    # resultado
    if "_" not in letras_descobertas:
        print("\n🎉 Parabéns! Você venceu!")
        print(f"A palavra era: {palavra}")
    else:
        print("\n💀 Você foi enforcado!")
        imprime_enforcado(estagios, max_erros)
        print(f"A palavra era: {palavra}")

if __name__ == "__main__":
    jogar_forca()
