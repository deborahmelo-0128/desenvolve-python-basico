#entrada de dados
#idade de Juliana
#idade de Cris
juliana_idade = int(input("Digite a idade de Juliana: "))
cris_idade = int(input("Digite a idade de Cris: "))
#processamento
#True se pelo menos um dos dois for maior de 17 anos
#False em qualquer outro caso
pode_entrar = juliana_idade >= 17 or cris_idade > 17
#saida de dados
print(pode_entrar)