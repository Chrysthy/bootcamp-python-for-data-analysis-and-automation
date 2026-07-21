# Objetos de primeira classe

# Em Python tudo é objeto, dessa forma funções também são objetos, o que as tornam objetos de primeira classe.
# Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc.) e 
# usá-las como valor de retorno para uma função (closures).

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def test(a, b):
    return a * 2 + b *3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 + 10 = 0
exibir_resultado(10, 10, test) # O resultado da operação 10 + 10 = 50  
# (porque 10 × 2 + 10  × 3 = 20 + 30 = 50)


# Atribuindo a função somar à variável operacao (apontamento)
# não está executando a função. Está guardando uma referência da função somar na variável operacao. 
operacao = somar
print(operacao(1,23))


# Por isso, depois, pode chamá-la normalmente:

operacao(1, 23)

# É o mesmo que fazer:

somar(1, 23)