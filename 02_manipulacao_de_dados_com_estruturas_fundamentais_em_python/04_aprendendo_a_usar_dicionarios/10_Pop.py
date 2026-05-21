# pop

contatos = {
    "chrystine@gmail.com": {"nome": "Chrystine", "telefone": "3333-2221"}
}

contatos.pop("chrystine@gmail.com")
# {"nome": "Chrystine", "telefone": "3333-2221"}

contatos.pop("chrystine@gmail.com", {})
# {}


# remove um item do dicionário com base na chave informada e retorna o valor associado a essa chave.
# Se a chave não existir, pode-se passar um valor padrão para evitar erro.

# pop(chave) → remove e retorna o valor da chave.
# pop(chave, valor_padrao) → retorna valor_padrao se a chave não existir, evitando erro.