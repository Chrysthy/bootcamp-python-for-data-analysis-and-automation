# Fatiamento
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. 
# Podemos ainda informar quantas posições o cursor deve ‘pular’ no acesso.

tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:]    # ("t", "h", "o", "n")
tupla[:2]    # ("p", "y")
tupla[1:3]   # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[:]     # ("p", "y", "t", "h", "o", "n")
tupla[::-1]  # ("n", "o", "h", "t", "y", "p")


# Explicação dos casos:

# tupla[2:]: pega do índice 2 até o final.

# tupla[:2]: pega do início até o índice 2 (exclusivo).

# tupla[1:3]: pega do índice 1 até o 3 (exclusivo).

# tupla[0:3:2]: pega do índice 0 ao 3, pulando de 2 em 2.

# tupla[:]: retorna todos os elementos.

# tupla[::-1]: retorna os elementos em ordem inversa.