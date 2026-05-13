# isdisjoint

conjunto_a = {1, 2, 3, 4 , 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))  # True
print(conjunto_a.isdisjoint(conjunto_c))  # False

# verifica se dois conjuntos não têm nenhum elemento em comum.

# conjunto_a.isdisjoint(conjunto_b) → True  
# Porque a e b não compartilham nenhum elemento.

# conjunto_a.isdisjoint(conjunto_c) → False  
# Porque a e c têm o elemento 1 em comum.

# Alternativa com operador
# Não existe um operador direto para isdisjoint, mas você pode simular com interseção:


print(conjunto_a & conjunto_b == set())  # True
print(conjunto_a & conjunto_c == set())  # False