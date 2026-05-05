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


# ===============================================================================

# Listas aninhadas
# Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais 
# (tabelas), e acessar informando os índices de linha e coluna.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]       # [1, "a", 2]
matriz[0][0]    # 1
matriz[0][-1]   # 2
matriz[-1][-1]  # "c"


# ===============================================================================

# Fatiamento
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. 
# Podemos ainda informar quantas posições o cursor deve "pular" no acesso.


lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]    # começa no índice 2 até o final → ["t", "h", "o", "n"]
lista[:2]    # do início até o índice 2 (sem incluir) → ["p", "y"]
lista[1:3]   # do índice 1 ao 3 (sem incluir o 3) → ["y", "t"]
lista[0:3:2] # do índice 0 ao 3, pulando de 2 em 2 → ["p", "t"]
lista[::]    # lista inteira (cópia completa) → ["p", "y", "t", "h", "o", "n"]
lista[::-1]  # passo -1, percorre ao contrário → ["n", "o", "h", "t", "y", "p"]