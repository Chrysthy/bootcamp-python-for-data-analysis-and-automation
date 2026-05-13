# intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))  # {2, 3}


# retorna os elementos que estão presentes nos dois conjuntos ao mesmo tempo.

# O 2 e o 3 aparecem em ambos os conjuntos.

# O 1 só está em conjunto_a, e o 4 só em conjunto_b, então ficam de fora.

# Você também pode usar o operador &, que é equivalente:


print(conjunto_a & conjunto_b)  # {2, 3}