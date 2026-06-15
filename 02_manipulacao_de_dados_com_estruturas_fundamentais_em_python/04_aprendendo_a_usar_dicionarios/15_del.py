contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
# Remove apenas o campo "telefone" dentro da chave "guilherme@gmail.com"

del contatos["chappie@gmail.com"]
# Remove completamente a chave "chappie@gmail.com" e seu conteúdo

contatos
# {'guilherme@gmail.com': {'nome': 'Guilherme'},
#  'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
#  'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}


# Primeiro del → remove apenas o campo "telefone" dentro do dicionário associado à chave "guilherme@gmail.com".

# Segundo del → apaga completamente a chave "chappie@gmail.com" e seu valor.

# O restante do dicionário permanece intacto.

# ⚠️ Cuidados:
# Se você tentar remover uma chave que não existe, o Python gera um erro KeyError.



# É usado para excluir algo do dicionário.
# Ele pode remover:

# Uma chave específica dentro de um dicionário aninhado.

# Um par chave-valor completo do dicionário principal.


# Em resumo:

    # del dicionario[chave] → apaga o par chave-valor.

    # del dicionario[chave][subchave] → apaga apenas um campo dentro do valor.

    # se colocar del contatos, ele apaga o dicionário inteiro.
