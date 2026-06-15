contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos
# True  -> a chave existe no dicionário principal
print(resultado)

resultado = "megui@gmail.com" in contatos
# False -> essa chave não existe
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]
# False -> dentro do dicionário dessa chave, não há "idade"
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]
# True  -> dentro do dicionário dessa chave, existe "telefone"
print(resultado)


# Quando usado diretamente em um dicionário, in verifica chaves.

# Quando usado dentro de um valor que também é um dicionário, ele verifica as chaves internas desse valor.

# Ele não procura valores, apenas nomes de chaves.


# O operador in verifica a existência de uma chave dentro de um dicionário.

# Ele não busca valores, apenas chaves — a menos que você o use dentro de um valor que também seja um dicionário.