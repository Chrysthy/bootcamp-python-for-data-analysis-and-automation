contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values()
# dict_values([
#   {'nome': 'Guilherme', 'telefone': '3333-2221'},
#   {'nome': 'Giovanna', 'telefone': '3443-2121'},
#   {'nome': 'Chappie', 'telefone': '3344-9871'},
#   {'nome': 'Melaine', 'telefone': '3333-7766'}
# ])



# O método não retorna uma lista diretamente, mas um objeto dict_values, que é uma visão dinâmica dos valores. Retorna os valores e não as chaves.

# Se o dicionário for alterado, essa visão também muda automaticamente.

# Para transformar em lista, basta usar:

    # list(contatos.values())


# Retorna uma visualização dos valores contidos no dicionário, ou seja, tudo o que está do lado direito das chaves.

# Essa visualização é do tipo dict_values, que pode ser percorrida com for ou convertida em uma lista.


