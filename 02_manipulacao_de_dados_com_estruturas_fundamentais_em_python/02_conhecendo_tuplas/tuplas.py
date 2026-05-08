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



