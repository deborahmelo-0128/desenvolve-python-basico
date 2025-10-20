# aula1_questao1.py
def main():
    try:
        x = float(input("Leia x: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if x > 5:
        print("Maior que 5")
    print("Fim")

if __name__ == "__main__":
    main()