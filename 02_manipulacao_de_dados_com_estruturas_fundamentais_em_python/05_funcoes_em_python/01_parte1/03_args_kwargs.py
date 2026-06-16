# Args e kwargs

# Podemos combinar parâmetros obrigatórios com args e kwargs.
# Quando esses são definidos (*args (renderiza uma tupla) e **kwargs (vem em um dicionário)), o método recebe os valores como tupla e dicionário, respectivamente.

# Quando não sabemos quantos argumentos uma função vai receber, podemos usar:

# *args → recebe vários argumentos posicionais e os transforma em uma tupla.
# **kwargs → recebe vários argumentos nomeados e os transforma em um dicionário.


# O *args pega todos os argumentos posicionais extras e transforma em uma tupla.
# Exemplo:

# def teste(*args):
#     print(args)

# teste("A", "B", "C")

# Saída:
# ('A', 'B', 'C')

# Ou seja:
# args = ('A', 'B', 'C')


# -----------------------------------------------------------------------------------------------------------------------------

# O **kwargs pega todos os argumentos nomeados extras e transforma em um dicionário.

# Exemplo:

# def teste(**kwargs):
#     print(kwargs)

# teste(nome="Chrystine", idade=30)

# Saída:
# {'nome': 'Chrystine', 'idade': 30}

# Ou seja:
# kwargs = {
#     'nome': 'Chrystine',
#     'idade': 30
# }




def exibir_poema(data_extenso, *args, **kwargs):

    texto = "\n".join(args)
    meta_datos = "\n".join(([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]))
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_datos}"
    print(mensagem)


exibir_poema(    
    "Sexta-feira, 26 de Agosto de 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
