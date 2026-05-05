# Trabalhando com Listas em Python
# Criação e acesso aos dados

# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores 
# separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

# Em Python, tudo é objeto.

# forma mais comum de declarar uma lista
frutas = ['laranja', 'maça', 'uva']

frutas = [] # lista vazia


letras = list('python')
# A função list() pega cada caractere da string e transforma em elemento da lista:
# ['p', 'y', 't', 'h', 'o', 'n']


numeros = list(range(10))
# range(10) gera números de 0 até 9
# list() transforma isso em lista
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



carro = ['Ferrari', 'F8', 4_200_000.50, 2020, 2900, 'São Paulo', True]
# Lista com tipos mistos
# Tipos dentro da sua lista:
# 'Ferrari' → str
# 'F8' → str
# 4_200_000.50 → float (decimal)
# 2020 → int
# 2900 → int
# 'São Paulo' → str
# True → bool


# ===============================================================================

# Acesso direto
# Podemos acessar usando índices 
# Contamos o índice de determinada sequeência a partir do zero.

frutas = ['maça', 'laranja', 'uva', 'pera']

print(frutas[0]) # maçã
print(frutas[2]) # uva


# índices negativos
# Contagem começa com -1

print(frutas[-1]) # pera
print(frutas[-3]) # laranja


