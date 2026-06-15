contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("nome", "Giovanna")
# "Guilherme"  -> a chave já existe, então mantém o valor atual

contato
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)
# 28  -> a chave não existia, então é criada com esse valor

contato
# {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}


# Se a chave já existe, o método não altera o valor e apenas o retorna.

# Se a chave não existe, ela é criada com o valor padrão informado.

# setdefault() é ótimo para inicializar valores padrão em dicionários, especialmente em estruturas de dados mais complexas (como contadores ou agrupamentos).

# Ele retorna sempre o valor da chave, seja existente ou recém-criada.

# É uma alternativa elegante ao uso de if chave not in dicionario:.