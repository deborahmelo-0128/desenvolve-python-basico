# aula1_questao2.py
# Interpretação do fluxograma: ler n, contar de 1 até n, imprimir cada contagem e ao final "Fim".

def main():
    try:
        n = int(input("Leia n: "))
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    cont = 0
    while n > cont:  # enquanto cont for menor que n
        cont += 1
        print(cont)
    print("Fim")

if __name__ == "__main__":
    main()