# difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_b)) # {4}


# # mostra os elementos que estão em um conjunto mas não estão no outro.
# pega os elementos de a que não estão em  b
# pega os elementos de b que não estão em  a
# Você também pode usar o operador -:


print(conjunto_a - conjunto_b)  # {1}
print(conjunto_b - conjunto_a)  # {4}