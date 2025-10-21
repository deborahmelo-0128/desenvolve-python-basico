import random

def main():
    numero = random.randint(1, 10)
    while True:
        try:
            palpite = int(input("Adivinhe o número entre 1 e 10: ").strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro entre 1 e 10.")
            continue

        if palpite < 1 or palpite > 10:
            print("Por favor, digite um número entre 1 e 10.")
        elif palpite > numero:
            print("Muito alto, tente novamente!")
        elif palpite < numero:
            print("Muito baixo, tente novamente!")
        else:
            print(f"Correto! O número é {numero}.")
            break

if __name__ == "__main__":
    main()
    