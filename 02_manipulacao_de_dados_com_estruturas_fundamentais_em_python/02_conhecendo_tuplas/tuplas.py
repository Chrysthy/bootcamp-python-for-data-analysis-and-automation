# Criação e acesso aos dados

# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. 
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parênteses.

# Tuplas são úteis quando você quer garantir que os dados não sejam modificados — por exemplo, coordenadas, configurações fixas ou constantes.

frutas = ('Laranja', 'pera', 'uva',)

letras = tuple('python')

numeros = tuple([1, 2, 3, 4])

pais = ('Brasil')
# Sem vírgula, isso não é uma tupla, é apenas uma string.
# Para criar uma tupla com um único elemento, você precisa colocar uma vírgula
pais = ('Brasil',)


# Acesso direto 
# A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.
# Tuplas permitem acesso direto, mas não permitem alteração dos valores — são imutáveis.

frutas = ('maça', 'laranja', 'uva', 'pera',)

frutas[0]
frutas[2]


frutas = ('maça', 'laranja', 'uva', 'pera',)

frutas[-1]
frutas[-3]


# Tuplas aninhadas  
# Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. 
# Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0]      # (1, "a", 2)
matriz[0][0]   # 1
matriz[0][-1]  # 2
matriz[-1][-1] # "c"
