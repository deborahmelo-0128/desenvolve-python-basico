# pede dois números decimais e calcula a diferença absoluta arredondada
try:
    a = float(input("Digite o primeiro número decimal: ").strip().replace(',', '.'))
    b = float(input("Digite o segundo número decimal: ").strip().replace(',', '.'))
except ValueError:
    print("Entrada inválida. Por favor, insira números decimais.")
else:
    diff = round(abs(a - b), 2)
    print(f"A diferença absoluta arredondada é: {diff:.2f}")
    