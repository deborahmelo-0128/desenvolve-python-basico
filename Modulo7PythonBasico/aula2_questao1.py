# Solicita a data de nascimento
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Separa a string em dia, mês e ano
dia, mes, ano = data.split("/")

# Lista com os nomes dos meses
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Converte o número do mês para o nome correspondente
mes_extenso = meses[int(mes) - 1]

# Exibe a data formatada
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
