# Fatiamento de string
# Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando início (start), fim (stop) e passo (step): 
# [start: stop[, step]]

nome = "Chrystine Martins de Oliveira Vasconcelos"

prtint(nome[0])        # 'C' → primeiro caractere da string
prtint(nome[:9])       # 'Chrystine' → do início até o índice 8
prtint(nome[10:])      # 'Martins de Oliveira Vasconcelos' → do índice 10 até o fim
prtint(nome[10:16])    # 'Martin' → do índice 10 até 15
prtint(nome[10:16:2])  # 'Mri' → do índice 10 até 15, pulando de 2 em 2
prtint(nome[:])        # 'Chrystine Martins de Oliveira Vasconcelos' → retorna a string inteira
prtint(nome[::-1])     # 'solecnocsaV arievilO ed snitraM enitsyhrC' → string invertida - espelhamento da sting