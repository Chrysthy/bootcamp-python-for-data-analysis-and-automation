# issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) #False

# verifica se todos os elementos de um conjunto estão contidos em outro.

# conjunto_a.issubset(conjunto_b) → True  
# Porque todos os elementos de a (1, 2, 3) estão dentro de b.

# conjunto_b.issubset(conjunto_a) → False  
# Porque b tem elementos (4, 5, 6) que não estão em a.

# Alternativa com operador
# Você também pode usar <= para verificar subconjunto:

print(conjunto_a <= conjunto_b)  # True
print(conjunto_b <= conjunto_a)  # False