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
# .copy
lista = [1, 'Python', [40, 30, 20]]

copia = lista.copy()

print(lista)
print(copia)

# lista e copia são duas listas diferentes na memória.
# Se você adicionar ou remover elementos da lista original, a cópia não muda
# É útil para trabalhar com uma versão independente da lista original.
# Mas lembre-se: objetos internos (como listas dentro da lista) continuam sendo compartilhados.

# Se você mudar elementos simples (números, strings, adicionar/remover itens), a cópia e a original ficam independentes.
# Se você mudar elementos internos mutáveis (como listas dentro da lista), a alteração aparece nas duas, porque é uma cópia rasa.

copia[2].append(99)
print(lista)  # [1, 'Python', [40, 30, 20, 99]]
print(copia)  # [1, 'Python', [40, 30, 20, 99], 'Novo']