# Cria um arquivo CSV com informações sobre livros

# Abrir o arquivo para escrita (modo 'w')
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escrever o cabeçalho da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escrever os dados dos livros (um por linha)
    arquivo.write("O Caçador de Pipas,Khaled Hosseini,2003,368\n")
    arquivo.write("Torto Arado,Itamar Vieira Junior,2019,264\n")
    arquivo.write("Cem Anos de Solidão,Gabriel García Márquez,1967,368\n")
    arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
    arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    arquivo.write("1984,George Orwell,1949,416\n")
    arquivo.write("A Menina que Roubava Livros,Markus Zusak,2005,480\n")
    arquivo.write("A Revolução dos Bichos,George Orwell,1945,152\n")
    arquivo.write("Ensaio Sobre a Cegueira,José Saramago,1995,312\n")
    arquivo.write("Orgulho e Preconceito,Jane Austen,1813,416\n")

print("✅ Arquivo 'meus_livros.csv' criado com sucesso!")
