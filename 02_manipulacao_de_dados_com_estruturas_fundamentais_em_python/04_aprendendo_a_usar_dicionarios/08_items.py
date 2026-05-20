# items

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
# A primeira parte da tupla é a chave ("guilherme@gmail.com").
# A segunda parte é o valor (outro dicionário com nome e telefone).



# Retorna uma visão dos itens do dicionário.
# Cada item é um par (chave, valor) dentro de uma estrutura chamada dict_items.
# É muito usado em loops para percorrer chaves e valores ao mesmo tempo.



for chave, valor in contatos.items():
    print(chave, "=>", valor)

# guilherme@gmail.com => {'nome': 'Guilherme', 'telefone': '3333-2221'}
# Assim você consegue percorrer o dicionário pegando chave e valor juntos.


# .items() → retorna todos os pares (chave, valor).
# Útil para percorrer o dicionário em loops.
# Resultado é um objeto dict_items, que se comporta como uma lista de tuplas.