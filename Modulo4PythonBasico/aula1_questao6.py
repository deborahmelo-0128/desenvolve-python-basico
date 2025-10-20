n = int(input()) # quantidade de experimentos
cont= 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0
while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == 'S':
        soma_sapo = soma_sapo + quantia
    elif tipo == 'R':
        soma_rato = soma_rato + quantia     
    elif tipo == 'C':
        soma_coelho = soma_coelho + quantia
    cont = cont + 1
total = soma_sapo + soma_rato + soma_coelho
print("Total:", total, "cobaias")
print("Total de sapos:", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos:", soma_coelho)
print("Percentual de sapos: %.2f %%" % ((soma_sapo/total)*100))
print("Percentual de ratos: %.2f %%" % ((soma_rato/total)*100))
print("Percentual de coelhos: %.2f %%" % ((soma_coelho/total)*100)) 

