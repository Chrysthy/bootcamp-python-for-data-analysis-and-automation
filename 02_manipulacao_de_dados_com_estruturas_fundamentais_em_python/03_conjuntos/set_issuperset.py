# issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True


# verifica se um conjunto contém todos os elementos de outro

# conjunto_a.issuperset(conjunto_b) → False  
# Porque a não contém todos os elementos de b (faltam 4, 5 e 6).

# conjunto_b.issuperset(conjunto_a) → True  
# Porque b contém todos os elementos de a (1, 2, 3) e ainda outros extras.

# Alternativa com operador
# Você também pode usar >= para verificar superconjunto:


print(conjunto_a >= conjunto_b)  # False
print(conjunto_b >= conjunto_a)  # True