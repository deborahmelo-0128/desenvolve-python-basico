🧾 DOCUMENTO DESCRITIVO — Sistema de Gestão Empresarial (CRUD Completo)
💡 1. Introdução

O Sistema de Gestão Empresarial foi desenvolvido em Python, com o objetivo de gerenciar de forma simples e eficiente o cadastro de usuários e produtos de uma empresa fictícia.
O sistema permite que diferentes tipos de usuários (gerente, funcionário e cliente) interajam com as informações de acordo com seus níveis de permissão.

A aplicação foi construída em modo terminal (CLI), utilizando recursos de leitura e gravação em arquivos CSV para persistência de dados, e a biblioteca Rich para proporcionar uma interface textual moderna e organizada.

⚙️ 2. Objetivos

O sistema busca demonstrar o uso prático dos conceitos de CRUD (Create, Read, Update, Delete), aplicados à gestão de informações de uma empresa, além de promover a prática de:

Estruturação de programas em Python;

Manipulação de arquivos CSV;

Controle de acesso por tipo de usuário;

Boas práticas de código e modularização.

🧱 3. Estrutura do Projeto

A estrutura de diretórios é simples e organizada:

sistema_gestao/
│
├── sistema_gestao.py        → Código principal do sistema
├── usuarios.csv              → Banco de dados de usuários
└── produtos.csv              → Banco de dados de produtos

👥 4. Perfis de Usuário e Níveis de Acesso
Tipo de Usuário	Permissões
Gerente	Acesso total: gerenciar usuários e produtos (CRUD completo)
Funcionário	Pode listar e consultar produtos
Cliente	Pode apenas visualizar produtos
🧮 5. Funcionalidades Implementadas
🔐 Login

O usuário se autentica informando nome de usuário e senha.

O sistema valida os dados com base no arquivo usuarios.csv.

Após login, o sistema exibe o menu de acordo com o tipo de usuário.

👥 Gestão de Usuários (Gerente)

Listar Usuários: exibe tabela com nome, login e função.

Adicionar Usuário: cria novos registros.

Atualizar Usuário: altera dados de nome, senha ou função.

Remover Usuário: exclui usuários existentes.

Todos os dados são salvos automaticamente no arquivo usuarios.csv.

📦 Gestão de Produtos (Gerente e Funcionário)

Listar Produtos: mostra tabela com ID, nome, preço e estoque.

Adicionar Produto (gerente): insere novos produtos no estoque.

Atualizar Produto (gerente): altera nome, preço ou quantidade.

Remover Produto (gerente): exclui itens do catálogo.

As alterações são registradas no arquivo produtos.csv.

👁️ Visualização de Produtos (Cliente)

O cliente tem acesso somente à listagem de produtos disponíveis.

🧰 6. Tecnologias Utilizadas

Linguagem: Python 3

Bibliotecas:

csv — leitura e escrita de dados tabulares

os — manipulação de arquivos e diretórios

rich — interface visual aprimorada no terminal

🧩 7. Conceitos Aplicados

CRUD (Create, Read, Update, Delete)

Controle de fluxo (condições e laços)

Dicionários e listas aninhadas

Modularização de código

Tratamento de erros e exceções

Entrada e saída de dados com persistência (CSV)

🖥️ 8. Exemplo de Execução
=== Sistema de Gestão - Login ===

👤 Usuário: deborah
🔑 Senha: 4444

Login bem-sucedido! Bem-vindo(a), Déborah Cliente.

=== Menu de Cliente ===
1. Listar produtos
0. Sair

📊 9. Estrutura dos Arquivos CSV

usuarios.csv

sername,nome_completo,senha,role
deborah,Déborah Cliente,4444,gerente
joao,João Funcionário,1234,funcionario
ana,Ana Gerente,8765,cliente
elena,Elena Cliente,4321,cliente
maria,Maria Funcionária,5678,funcionario
wagner,Wagner Gerente,0000,gerente



produtos.csv

id,nome,preco,estoque
1,Camiseta Básica,49.90,25
2,Calça Jeans,129.90,15
3,Tênis Esportivo,249.00,10
4,Boné Estiloso,39.90,20
5,Relógio Digital,199.90,8
6,Mochila Escolar,89.90,12
7,Fone de Ouvido,99.00,18
8,Jaqueta Jeans,179.00,7
9,Cinto de Couro,69.90,14
10,Óculos de Sol,149.90,9
11,Camiseta neon,85.00,20
12,Shorts esportivo,75.00,30
13,Meias coloridas,25.00,50
14,Chapéu de palha,60.00,15
15,Bolsa de mão,120.00,10
16,Carteira masculina,80.00,25
17,Relógio de pulso,220.00,5
18,Jaqueta de couro,300.00,8
19,Tênis casual,150.00,12
20,Calça de moletom,90.00,20
21,Camiseta polo,70.00,30
22,Regata básica,40.00,40
23,Blusa de frio,110.00,10
24,Sandália confortável,55.00,18
25,Bota de couro,250.00,6
26,Chinelo de praia,30.00,25
27,Calça social,130.00,14
28,Camisa social,95.00,22
29,Gravata elegante,45.00,30

🧭 10. Conclusão

O projeto Sistema de Gestão Empresarial consolida os principais conceitos de programação estruturada em Python e manipulação de dados persistentes em arquivos.
Ele demonstra de forma prática o funcionamento de um sistema CRUD com níveis de acesso, autenticação e persistência, aproximando o aprendizado das rotinas reais de uma aplicação empresarial.

Esse trabalho representa um exemplo funcional e didático de como pequenas soluções em Python podem automatizar processos de negócios e organização interna de empresas.