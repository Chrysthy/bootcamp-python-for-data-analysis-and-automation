# .reverse
linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.reverse()

# serve para inverter a ordem dos elementos da lista, modificando-a diretamente (não cria uma nova lista).
# .reverse() não retorna nada (None), ele apenas altera a lista original.

# Se você quiser obter uma lista invertida sem modificar a original, pode usar slicing.
# Diferença: .reverse() é um método in-place (modifica a lista), enquanto [::-1] cria uma cópia invertida.