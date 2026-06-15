contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

# Atualiza o valor da chave existente
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}}

# Adiciona uma nova chave com seus dados
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}



# Primeiro update()

    # A chave "guilherme@gmail.com" já existia.

    # O valor antigo ({"nome": "Guilherme", "telefone": "3333-2221"}) foi substituído por um novo valor ({"nome": "Gui"}).

    # A chave em si não muda.

# Segundo update()

    # A chave "giovanna@gmail.com" não existia.

    # Foi adicionada ao dicionário com o valor informado.



# O método update() serve para atualizar um dicionário com outro conjunto de dados.

# Ele pode:

    # Alterar valores existentes (se a chave já estiver presente).

    # Adicionar novas chaves (se ainda não existirem).