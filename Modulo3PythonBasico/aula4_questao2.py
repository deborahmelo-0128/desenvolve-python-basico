rating = int(input("Insira a avaliação do filme (1 a 5): "))

if rating == 5:
    print("Excelente!")
elif rating == 4:
    print("Muito Bom!")
elif rating == 3:
    print("Bom!")
elif rating == 2:
    print("Regular.")
elif rating == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um número de 1 a 5.")