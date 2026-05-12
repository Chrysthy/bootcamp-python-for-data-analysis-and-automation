# Conjuntos 
# Entender o funcionamento da estrutura de dados set
# Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)

# Elementos únicos: não permitem duplicatas.
# Não ordenados: não garantem a ordem de inserção (embora no Python moderno geralmente mantenham a ordem, mas isso não deve ser usado como regra).
# Mutáveis: você pode adicionar ou remover elementos.
# Iteráveis: podem ser percorridos em loops.


# Diferença entre {} e set():
    # {} → cria um set diretamente, se você colocar elementos dentro.

    # set([...]) → cria um set a partir de um iterável (lista, tupla, string etc.).

    # O Python vê as chaves e entende que você quer um set literal.

    # Como sets não permitem duplicatas, o "python" repetido é automaticamente eliminado.


# Atenção: Existe uma exceção importante:
    # {} sozinho cria um dicionário vazio, não um set.

    # Para criar um set vazio, você precisa usar set().