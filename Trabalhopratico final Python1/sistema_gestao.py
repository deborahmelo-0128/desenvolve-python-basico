import csv
import os
from rich.console import Console
from rich.table import Table

console = Console()

ARQUIVO_USUARIOS = "usuarios.csv"
ARQUIVO_PRODUTOS = "produtos.csv"

# ========================================================
# FUNÇÃO: Carregar usuários
# ========================================================
def carregar_usuarios():
    usuarios = {}
    try:
        with open(ARQUIVO_USUARIOS, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuarios[row["username"]] = {
                    "nome_completo": row["nome_completo"],
                    "senha": row["senha"],
                    "role": row["role"]
                }
        console.print(f"[green]Carregados {len(usuarios)} usuários.[/green]")
    except FileNotFoundError:
        console.print("[yellow]Arquivo de usuários não encontrado. Será criado ao salvar.[/yellow]")
    return usuarios

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "nome_completo", "senha", "role"])
        writer.writeheader()
        for u, dados in usuarios.items():
            writer.writerow({"username": u, **dados})

# ========================================================
# FUNÇÃO: Carregar produtos
# ========================================================
def carregar_produtos():
    produtos = []

    if not os.path.exists(ARQUIVO_PRODUTOS):
        console.print(f"[yellow]Arquivo '{ARQUIVO_PRODUTOS}' não encontrado. Será criado ao salvar.[/yellow]")
        return produtos

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                produtos.append({
                    "id": row["id"],
                    "nome": row["nome"],
                    "preco": float(row["preco"]),
                    "estoque": int(row["estoque"])
                })
            except KeyError as e:
                console.print(f"[red]Erro: campo {e} não encontrado em produtos.csv[/red]")
                return []
    console.print(f"[green]Carregados {len(produtos)} produtos de '{ARQUIVO_PRODUTOS}'[/green]")
    return produtos

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nome", "preco", "estoque"])
        writer.writeheader()
        for p in produtos:
            writer.writerow({
                "id": p["id"],
                "nome": p["nome"],
                "preco": f"{p['preco']:.2f}",
                "estoque": p["estoque"]
            })
    console.print(f"[green]Arquivo '{ARQUIVO_PRODUTOS}' salvo com sucesso.[/green]")

# ========================================================
# LOGIN
# ========================================================
def login():
    usuarios = carregar_usuarios()
    console.print("\n[bold cyan]=== Sistema de Gestão - Login ===[/bold cyan]\n")

    while True:
        username = console.input("👤 Usuário: ").strip()
        senha = console.input("🔑 Senha: ").strip()

        if username in usuarios and usuarios[username]["senha"] == senha:
            console.print(f"\n[green]Login bem-sucedido![/green] Bem-vindo(a), [bold]{usuarios[username]['nome_completo']}[/bold].")
            return usuarios[username]
        else:
            console.print("[red]Usuário ou senha incorretos. Tente novamente.[/red]\n")

# ========================================================
# CRUD DE USUÁRIOS
# ========================================================
def gerenciar_usuarios():
    usuarios = carregar_usuarios()
    while True:
        console.print("\n[bold green]=== Gestão de Usuários ===[/bold green]")
        console.print("1. Listar usuários")
        console.print("2. Adicionar usuário")
        console.print("3. Atualizar usuário")
        console.print("4. Remover usuário")
        console.print("0. Voltar")

        opcao = console.input("Escolha: ")

        if opcao == "1":
            tabela = Table(title="Usuários Cadastrados")
            tabela.add_column("Usuário")
            tabela.add_column("Nome completo")
            tabela.add_column("Função")
            for u, dados in usuarios.items():
                tabela.add_row(u, dados["nome_completo"], dados["role"])
            console.print(tabela)

        elif opcao == "2":
            username = console.input("Novo usuário: ")
            if username in usuarios:
                console.print("[red]Usuário já existe![/red]")
            else:
                nome = console.input("Nome completo: ")
                senha = console.input("Senha: ")
                role = console.input("Função (gerente/funcionario/cliente): ")
                usuarios[username] = {"nome_completo": nome, "senha": senha, "role": role}
                salvar_usuarios(usuarios)
                console.print("[green]Usuário adicionado com sucesso![/green]")

        elif opcao == "3":
            username = console.input("Usuário a atualizar: ")
            if username in usuarios:
                nome = console.input(f"Novo nome ({usuarios[username]['nome_completo']}): ") or usuarios[username]['nome_completo']
                senha = console.input("Nova senha (ou Enter p/ manter): ") or usuarios[username]['senha']
                role = console.input(f"Nova função ({usuarios[username]['role']}): ") or usuarios[username]['role']
                usuarios[username] = {"nome_completo": nome, "senha": senha, "role": role}
                salvar_usuarios(usuarios)
                console.print("[green]Usuário atualizado![/green]")
            else:
                console.print("[red]Usuário não encontrado![/red]")

        elif opcao == "4":
            username = console.input("Usuário a remover: ")
            if username in usuarios:
                del usuarios[username]
                salvar_usuarios(usuarios)
                console.print("[green]Usuário removido![/green]")
            else:
                console.print("[red]Usuário não encontrado![/red]")

        elif opcao == "0":
            break
        else:
            console.print("[red]Opção inválida![/red]")

# ========================================================
# CRUD DE PRODUTOS
# ========================================================
def listar_produtos():
    produtos = carregar_produtos()
    if not produtos:
        console.print("[yellow]Nenhum produto encontrado![/yellow]")
        return

    tabela = Table(title="Produtos")
    tabela.add_column("ID")
    tabela.add_column("Nome")
    tabela.add_column("Preço")
    tabela.add_column("Estoque")

    for p in produtos:
        tabela.add_row(p["id"], p["nome"], f"R$ {p['preco']:.2f}", str(p["estoque"]))

    console.print(tabela)

def adicionar_produto():
    produtos = carregar_produtos()
    id_prod = console.input("ID do produto: ")
    nome = console.input("Nome: ")
    preco = float(console.input("Preço (use ponto ou vírgula): ").replace(",", "."))
    estoque = int(console.input("Estoque: "))
    produtos.append({"id": id_prod, "nome": nome, "preco": preco, "estoque": estoque})
    salvar_produtos(produtos)
    console.print("[green]Produto adicionado com sucesso![/green]")

def atualizar_produto():
    produtos = carregar_produtos()
    id_prod = console.input("ID do produto a atualizar: ")
    for p in produtos:
        if p["id"] == id_prod:
            novo_nome = console.input(f"Novo nome ({p['nome']}): ") or p["nome"]
            novo_preco = console.input(f"Novo preço ({p['preco']}): ")
            try:
                p["preco"] = float(novo_preco.replace(",", ".")) if novo_preco else p["preco"]
            except:
                console.print("[yellow]Preço inválido. Mantendo valor anterior.[/yellow]")
            novo_estoque = console.input(f"Novo estoque ({p['estoque']}): ")
            try:
                p["estoque"] = int(novo_estoque) if novo_estoque else p["estoque"]
            except:
                console.print("[yellow]Valor de estoque inválido. Mantendo anterior.[/yellow]")
            p["nome"] = novo_nome
            salvar_produtos(produtos)
            console.print("[green]Produto atualizado com sucesso![/green]")
            return
    console.print("[red]Produto não encontrado![/red]")

def remover_produto():
    produtos = carregar_produtos()
    id_prod = console.input("ID do produto a remover: ")
    produtos = [p for p in produtos if p["id"] != id_prod]
    salvar_produtos(produtos)
    console.print("[green]Produto removido com sucesso![/green]")

def gerenciar_produtos(role):
    while True:
        console.print("\n[bold yellow]=== Gestão de Produtos ===[/bold yellow]")
        console.print("1. Listar produtos")
        if role == "gerente":
            console.print("2. Adicionar produto")
            console.print("3. Atualizar produto")
            console.print("4. Remover produto")
        console.print("0. Voltar")
        opcao = console.input("Escolha: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2" and role == "gerente":
            adicionar_produto()
        elif opcao == "3" and role == "gerente":
            atualizar_produto()
        elif opcao == "4" and role == "gerente":
            remover_produto()
        elif opcao == "0":
            break
        else:
            console.print("[red]Opção inválida ou acesso negado![/red]")

# ========================================================
# MENU PRINCIPAL
# ========================================================
if __name__ == "__main__":
    usuario_logado = login()
    role = usuario_logado["role"]

    if role == "gerente":
        console.print("[bold cyan]\nAcesso total liberado (Gerente)[/bold cyan]")
        while True:
            console.print("\n=== Menu do Gerente ===")
            console.print("1. Gerenciar usuários")
            console.print("2. Gerenciar produtos")
            console.print("0. Sair")
            opcao = console.input("Escolha: ")
            if opcao == "1":
                gerenciar_usuarios()
            elif opcao == "2":
                gerenciar_produtos("gerente")
            elif opcao == "0":
                break

    elif role == "funcionario":
        console.print("[bold cyan]\nAcesso de funcionário (produtos apenas)[/bold cyan]")
        gerenciar_produtos("funcionario")

    else:
        console.print("[bold cyan]\nAcesso de cliente (visualização apenas)[/bold cyan]")
        listar_produtos()
    console.print("\n[bold green]Obrigado por usar o sistema! Até logo![/bold green]\n")
