import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        # Se a palavra tiver 3 letras ou menos, não embaralha
        if len(palavra) <= 3:
            nova_frase.append(palavra)
        else:
            # Mantém primeira e última letra fixas
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]
            nova_frase.append(palavra_embaralhada)

    return ' '.join(nova_frase)


# ---------- Exemplo de uso ----------
frase = "Programar em Python é divertido"
nova = embaralhar_palavras(frase)

print("Frase original:", frase)
print("Frase embaralhada:", nova)
