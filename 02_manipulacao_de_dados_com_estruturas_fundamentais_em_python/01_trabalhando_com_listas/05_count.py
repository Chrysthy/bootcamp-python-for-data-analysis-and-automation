# .count
cores = ['vermelho', 'azul', 'verde', 'azul']

cores.count('vermelho') # retorna 1, porque 'vermelho' aparece uma vez
cores.count('azul')  # retorna 2, porque 'azul' aparece duas vezes
cores.count('verde') # retorna 1, porque 'verde' aparece uma vez

# Ele conta quantas vezes um determinado elemento aparece dentro da lista.
# Se o elemento não existir, o resultado será 0.
# .count() é útil para saber a frequência de um item em uma lista.
# Funciona com qualquer tipo de dado: números, strings, até listas ou objetos.