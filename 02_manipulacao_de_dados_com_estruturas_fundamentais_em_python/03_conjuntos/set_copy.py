# copy

sorteio = {1, 23}
print(sorteio)  # {1, 23}

copia = sorteio.copy()   # cria uma cópia
print(copia)             # {1, 23}

# Alterando o original
sorteio.add(99)
print(sorteio)  # {1, 23, 99}
print(copia)    # {1, 23}  -> a cópia não foi afetada


# cria uma cópia independente do conjunto

# copy → retorna um novo conjunto com os mesmos elementos.

# Se você não guardar o retorno (copia = sorteio.copy()), o resultado é descartado.

# A cópia é independente: alterações no conjunto original não afetam a cópia.