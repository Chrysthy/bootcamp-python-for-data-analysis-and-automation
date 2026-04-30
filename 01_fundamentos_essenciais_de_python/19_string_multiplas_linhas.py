# String múltiplas linhas
# São definidas informando 3 aspas simples ou duplas durante a atribuição.
# Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

nome = "Chrystine"

mensagem = f"""
Olá, meu nome é {nome},
Eu estou aprendendo Python
"""


mensagem = f"""
        Olá, meu nome é {nome},
    Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
"""


# Os espaços e recuos que você colocou dentro da string são preservados. Isso é uma característica das strings de múltiplas linhas: tudo que você digita entre as aspas triplas 
# vai aparecer na saída, inclusive quebras de linha e indentação.

# Se quiser evitar quebras de linha extras no início ou fim, pode usar .strip():


print(mensagem.strip())

# Para docstrings (comentários de documentação em funções), também usamos """ ... """.



print("""
        ************** Menu ****************

        1 - Depositar
        2 - Sacar
        3 - Sair

        *********************************
""")