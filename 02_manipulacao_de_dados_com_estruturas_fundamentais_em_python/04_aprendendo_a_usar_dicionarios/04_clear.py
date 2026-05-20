# clear

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"code": 400}},
}

contatos.clear()
contatos # {}


# remove todos os itens de um dicionário.
# Após a execução, o dicionário fica vazio, mas continua existindo (não é apagado da memória).