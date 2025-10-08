# Sistema de validação de ficha de personagem RPG

classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Atribua os pontos de força: "))
magia = int(input("Atribua os pontos de magia: "))

valido = False

if classe == "guerreiro":
    if forca >= 15 and magia <= 10:
        valido = True
elif classe == "mago":
    if forca <= 10 and magia >= 15:
        valido = True
elif classe == "arqueiro":
    if 5 < forca <= 15 and 5 < magia <= 15:
        valido = True

print(valido)