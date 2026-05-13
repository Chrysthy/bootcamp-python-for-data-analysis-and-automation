# discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

numeros    # {2, 3, 4, 5, 6, 7, 8, 9, 0}


# remove um elemento de um conjunto (set) sem gerar erro se o elemento não existir.

# numeros.discard(1) remove o número 1.

# numeros.discard(45) não faz nada, pois 45 não está no conjunto
