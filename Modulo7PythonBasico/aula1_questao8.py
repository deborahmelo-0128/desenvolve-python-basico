def validar_cpf(cpf):
    # Remove pontos e traço
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"

    # Se todos os dígitos forem iguais, é inválido
    if cpf == cpf[0] * 11:
        return "Inválido"

    # ---------- Cálculo do primeiro dígito ----------
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # ---------- Cálculo do segundo dígito ----------
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # ---------- Verificação final ----------
    if cpf[-2:] == f"{digito1}{digito2}":
        return "Válido"
    else:
        return "Inválido"


# ---------- Programa principal ----------
cpf_usuario = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_usuario)
print(resultado)
