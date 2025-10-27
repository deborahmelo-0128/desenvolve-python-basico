# Lista de URLs
URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Usando fatiamento para extrair o nome do domínio
dominios = [url[4:-4] for url in URLs]

print(dominios)
