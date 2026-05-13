# symmetric difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# retorna os elementos que estão em um conjunto ou no outro, mas não nos dois ao mesmo tempo.

# O 2 e o 3 aparecem nos dois conjuntos → ficam de fora.

# O 1 aparece só em conjunto_a.
# O 4 aparece só em conjunto_b.
# Resultado: {1, 4}.

# Alternativa com operador
# Você também pode usar o operador ^ (circunflexo):

python
print(conjunto_a ^ conjunto_b)  # {1, 4}