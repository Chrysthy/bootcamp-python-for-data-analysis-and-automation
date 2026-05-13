# pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)       # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.pop()        # remove um elemento qualquer
numeros.pop()        # remove outro elemento qualquer

print(numeros)       # resultado depende de quais foram removidos


# remove e retorna um elemento aleatório de um conjunto. Como os sets não têm ordem fixa, você não controla qual elemento será removido — pode variar a cada execução.

# O conjunto elimina duplicatas automaticamente, então numeros começa como {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.

# Cada chamada de pop() remove um item arbitrário.

# O resultado final pode ser diferente a cada vez que você roda o código.