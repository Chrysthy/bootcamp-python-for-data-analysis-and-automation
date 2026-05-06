# Métodos da classe list

# .append 
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

# .append() sempre adiciona um único elemento ao final da lista.
# Esse elemento pode ser de qualquer tipo: número, string, outra lista, objeto etc.
# Quando você faz append([40, 30, 20]), está colocando a lista inteira como um item só, não espalhando os valores.


# ====================================================================================================
# .clear
lista = [1, 'Python', [40, 30, 20]]

print(lista)
lista.clear()
print(lista) # []

# Serve para remover todos os elementos da lista de uma vez, deixando-a vazia.
# .clear() não apaga a lista em si, apenas os elementos dentro dela.
# Depois de usar .clear(), a lista continua existindo, só que vazia.
# Isso é útil quando você quer reaproveitar a mesma lista sem precisar criar uma nova.


# ====================================================================================================