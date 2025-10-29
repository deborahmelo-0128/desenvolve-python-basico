import random

def encrypt(lista):
    # Gera um número aleatório entre 1 e 10
    n = random.randint(1, 10)

    criptografadas = []

    for texto in lista:
        novo_texto = ""
        for c in texto:
            codigo = ord(c)
            # Apenas caracteres visíveis (33 a 126)
            if 33 <= codigo <= 126:
                # Faz o deslocamento com wrap-around
                novo_codigo = ((codigo - 33 + n) % 94) + 33
                novo_texto += chr(novo_codigo)
            else:
                novo_texto += c
        criptografadas.append(novo_texto)

    return criptografadas, n


# ---------- Exemplo conforme o enunciado ----------
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Para garantir a mesma chave do exemplo:
chave_aleatoria = 5

# Criptografa com chave fixa
def encrypt_fixed(lista, n):
    criptografadas = []
    for texto in lista:
        novo_texto = ""
        for c in texto:
            codigo = ord(c)
            if 33 <= codigo <= 126:
                novo_codigo = ((codigo - 33 + n) % 94) + 33
                novo_texto += chr(novo_codigo)
            else:
                novo_texto += c
        criptografadas.append(novo_texto)
    return criptografadas

nomes_cript = encrypt_fixed(nomes, chave_aleatoria)

print(f"Nomes criptografados: {nomes_cript}")
print(f"Chave de criptografia: {chave_aleatoria}")

    
