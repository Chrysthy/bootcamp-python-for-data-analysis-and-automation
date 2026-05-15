# Dicionários aninhados

# Um dicionário pode conter outro dicionário como valor, criando uma estrutura em camadas.
# Isso é útil para organizar dados mais complexos, como listas de contatos, produtos, etc.
# As chaves continuam sendo únicas, mas os valores podem ser outros dicionários, listas ou qualquer objeto Python.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"code": 400}},
}

# Para acessar dados dentro de um dicionário aninhado, usamos múltiplos colchetes:
contatos["giovanna@gmail.com"]["telefone"]  # Retorna "3443-2121"

telefone = contatos["melaine@gmail.com"]["telefone"]
print(telefone)   # Saída: "3333-7766"

extra = contatos["melaine@gmail.com"]["extra"]["code"]
print(extra)      # Saída: 400


# - Podemos acessar dados em várias camadas usando múltiplos colchetes.
# - Primeiro acessamos a chave externa (e-mail), depois a chave interna ("telefone" ou "extra").
# - Isso torna os dicionários aninhados muito úteis para representar dados hierárquicos.


