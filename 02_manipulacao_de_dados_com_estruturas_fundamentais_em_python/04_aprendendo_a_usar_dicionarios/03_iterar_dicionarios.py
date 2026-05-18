# Iterar dicionários
# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"code": 400}},
}


# Iterando apenas pelas chaves:
for chave in  contatos:
    print(chave, contatos[chave])


# Saída:
# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
# melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766', 'extra': {'code': 400}}



# Iterando pelas chaves e valores ao mesmo tempo:
for chave, valor in contatos.items():
    print(chave, valor)


# Saída:
# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
# melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766', 'extra': {'code': 400}}




# - "for chave in dicionario" percorre apenas as chaves.
# - "for chave, valor in dicionario.items()" percorre chaves e valores juntos.
# - Corrija o erro de digitação para evitar NameError.