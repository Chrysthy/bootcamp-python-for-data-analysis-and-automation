# get

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#Acesso direto
contatos["chave"]    # KeyError


# Usando .get() sem valor padrão
contatos.get("chave")    # None


# Se a chave não existe, retorna o valor que você passou (nesse caso {}).
contatos.get("chave", {})    # {}
contatos.get("guilherme@gmail.com", {})    # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


contatos.get("chave", "não encontrado")
# "não encontrado"

contatos.get("chave", 0)
# 0

contatos.get("chave", ["sem dados"])
# ["sem dados"]

contatos.get("chave", {"status": "inexistente"})
# {"status": "inexistente"}


# Serve para acessar valores de uma chave no dicionário. Um jeito seguro de acessar valores em um dicionário.

# Diferente do acesso direto (contatos["chave"]), ele não gera erro se a chave não existir.

# Se a chave não for encontrada, retorna None ou um valor padrão que você pode definir.