# union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))  # {1, 2, 3, 4}

# O método union retorna um novo conjunto com todos os elementos dos dois.

# Se houver elementos repetidos, eles aparecem apenas uma vez.

# Você também pode usar o operador | (pipe), que é equivalente:

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
