# add

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# serve para inserir novos elementos em um conjunto.

# O 25 foi adicionado na primeira vez.

# Quando você tentou adicionar 25 de novo, nada aconteceu, porque sets não permitem duplicatas.

# O 42 foi adicionado normalmente.