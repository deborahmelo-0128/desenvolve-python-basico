# aula1_questao3.py
# Lê três notas, calcula a média e imprime o resultado conforme o fluxograma.

def main():
    try:
        n1 = float(input("Leia n1: "))
        n2 = float(input("Leia n2: "))
        n3 = float(input("Leia n3: "))
    except ValueError:
        print("Entrada inválida. Digite números.")
        return

    m = (n1 + n2 + n3) / 3

    if m >= 60:
        print("Aprovado")
    elif m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")

    print("Fim")

if __name__ == "__main__":
    main()