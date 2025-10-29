# Solicita o número de celular
numero = input("Digite o número de celular (somente números): ")

# Verifica o tamanho do número
if len(numero) == 8:
    # Adiciona o 9 na frente
    numero = "9" + numero
    print("Número ajustado para 9 dígitos.")

elif len(numero) == 9:
    # Verifica se começa com 9
    if numero[0] != "9":
        print("Atenção: o número de 9 dígitos não começa com 9.")
else:
    print("Número inválido! Digite 8 ou 9 dígitos.")

# Adiciona o separador "-" antes dos últimos 4 dígitos
if len(numero) == 9:
    numero_formatado = numero[:5] + "-" + numero[5:]
    print(f"Número formatado: {numero_formatado}")
