import csv

# Abrir o arquivo CSV para leitura com o encoding correto
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)

    # Ler o cabeçalho (primeira linha)
    cabecalho = next(leitor)

    # Índices das colunas que queremos
    idx_nome = cabecalho.index("track_name")
    idx_artista = cabecalho.index("artist(s)_name")
    idx_artista_count = cabecalho.index("artist_count")
    idx_ano = cabecalho.index("released_year")
    idx_streams = cabecalho.index("streams")

    # Dicionário para guardar a música mais tocada de cada ano
    mais_tocadas = {}

    # Processar cada linha do arquivo
    for linha in leitor:
        try:
            # Extrair valores
            nome = linha[idx_nome]
            artista = linha[idx_artista]
            ano = int(linha[idx_ano])
            streams = int(linha[idx_streams])
            artist_count = int(linha[idx_artista_count])

            # Ignorar linhas problemáticas
            if '"' in nome or '"' in artista:
                continue

            # Filtrar apenas anos entre 2012 e 2022
            if 2012 <= ano <= 2022:
                # Se ainda não temos uma música para o ano OU se esta tem mais streams, atualiza
                if ano not in mais_tocadas or streams > mais_tocadas[ano][3]:
                    mais_tocadas[ano] = [nome, artista, ano, streams]

        except Exception:
            # Ignora linhas com dados ausentes ou mal formatados
            continue

# Criar lista final ordenada por ano
lista_final = [mais_tocadas[ano] for ano in sorted(mais_tocadas.keys())]

# Imprimir resultado
print(lista_final)
