# Acesso aos dados
# Para acessar um valor, usamos a chave correspondente entre colchetes [].

dados = {"nome": "Chrystine", "idade": 34, "telefone": "3334-5555"}  

dados["nome"]       # Retorna "Chrystine"
dados["idade"]      # Retorna 34
dados["telefone"]   # Retorna "3334-5555"


# Também podemos atualizar os valores das chaves existentes:
dados["nome"] = "Noob"          # Atualiza o valor da chave "nome"
dados["idade"] = 15             # Atualiza o valor da chave "idade"
dados["telefone"] = "99917-0055" # Atualiza o valor da chave "telefone"


# os valores podem ser acessados e modificados facilmente, mas as chaves continuam únicas dentro do dicionário.