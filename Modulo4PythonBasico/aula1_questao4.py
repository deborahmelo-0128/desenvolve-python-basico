# aula1_questao4.py
def main():
    n = int(input("Digite a quantidade de números (n): "))
    maior = 0
    while n > 0:
        x = float(input("Digite um número: "))
        if x > maior:
            maior = x
        n -= 1
    print("Maior:", maior)

if __name__ == "__main__":
    main()