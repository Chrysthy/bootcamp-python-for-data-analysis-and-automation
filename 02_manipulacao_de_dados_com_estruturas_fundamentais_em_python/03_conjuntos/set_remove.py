# remove

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros    # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0)    # 0
numeros    # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# remove um elemento específico de um conjunto (set).

# Se o elemento existe, ele é removido.

# Se o elemento não existe, o Python lança um erro KeyError.

# Diferença com .discard():

# .remove() → dá erro se o item não existir.

# .discard() → ignora silenciosamente se o item não existir.