# popitem

contatos = {
    "chrystine@gmail.com": {"nome": "Chrystine", "telefone": "3333-2221"}
}

contatos.popitem()
# ("chrystine@gmail.com", {"nome": "Chrystine", "telefone": "3333-2221"})

contatos.popitem()
# KeyError: 'popitem(): dictionary is empty'


# Primeiro popitem:
# Remove o único item do dicionário e retorna uma tupla com a chave e o valor.
# Resultado → ("chrystine@gmail.com", {"nome": "Chrystine", "telefone": "3333-2221"})  
# O dicionário fica vazio.

# Segundo popitem:
# Como o dicionário já está vazio, ocorre um erro KeyError.



# remove e retorna um par chave-valor do dicionário.

# Antes do Python 3.7, o item removido era aleatório.

# A partir do Python 3.7, ele sempre remove o último item inserido (seguindo a ordem de inserção).