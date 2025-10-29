def validador_senha(senha):
    # Critério 1: pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Critérios 2, 3 e 4
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in "@#$%&*!_-" for c in senha)

    # Retorna True somente se todos os critérios forem atendidos
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial


# ---------- Exemplos de uso ----------
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # ✅ True
print(validador_senha(senha2))  # ❌ False
print(validador_senha(senha3))  # ❌ False
print(validador_senha("SenhaForte1!"))  # ✅ True
print(validador_senha("Curta1!"))  # ❌ False