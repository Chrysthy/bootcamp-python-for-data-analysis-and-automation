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


# ====================================================================================================
# .count
cores = ['vermelho', 'azul', 'verde', 'azul']

cores.count('vermelho') # retorna 1, porque 'vermelho' aparece uma vez
cores.count('azul')  # retorna 2, porque 'azul' aparece duas vezes
cores.count('verde') # retorna 1, porque 'verde' aparece uma vez

# Ele conta quantas vezes um determinado elemento aparece dentro da lista.
# Se o elemento não existir, o resultado será 0.
# .count() é útil para saber a frequência de um item em uma lista.
# Funciona com qualquer tipo de dado: números, strings, até listas ou objetos.


# ====================================================================================================
# .extend
linguagens = ['python', 'js', 'c']   # lista inicial com 3 linguagens

print(linguagens)                    # imprime a lista original -> ['python', 'js', 'c']

linguagens.extend(['java', 'csharp']) # adiciona 'java' e 'csharp' separadamente ao final da lista

print(linguagens)                    # imprime a lista atualizada -> ['python', 'js', 'c', 'java', 'csharp']


# Diferente de .append(), que adiciona um único item (mesmo que seja uma lista inteira), o .extend() desempacota os elementos e coloca cada um separadamente.
# Não remove valores duplicados
# Ele pega a lista original e coloca tudo que passar entre ([]) no final da lista linguagens
# Sintaxe:
# lista.extend([elemento1, elemento2, ...])


# ====================================================================================================
# .index
linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.index('java') #3
linguagens.index('python') #0

 
# Serve para localizar a posição de um elemento dentro de uma lista. Ele retorna o índice da primeira ocorrência encontrada.
# Quando existem elementos repetidos, .index() não mostra todos os índices, apenas o primeiro.


# ====================================================================================================
# .pop
linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.pop()    # remove 'csharp'
linguagens.pop()    # remove 'java'
linguagens.pop()    # remove 'c'
linguagens.pop(0)   # remove 'python'


# é usado para remover elementos. Por padrão, ele remove o último item da lista, mas você também pode passar um índice específico para remover outro elemento.
# Se você tentar remover um índice que não existe, o Python gera um IndexError.