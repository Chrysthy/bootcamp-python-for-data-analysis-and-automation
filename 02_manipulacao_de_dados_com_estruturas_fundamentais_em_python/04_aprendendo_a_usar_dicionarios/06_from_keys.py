# fromkey

dict.fromkeys(["nome", "telefone"]) # {'nome': None, 'telefone': None}
# Aqui, o Python criou um dicionário com as chaves "nome" e "telefone", e colocou None como valor para cada uma.

dict.fromkeys(["nome", "telefone"], 'vazio') # {'nome': None, 'telefone': None}
# Agora, além das chaves, você disse que o valor padrão seria "vazio".
# Então todas as chaves receberam esse mesmo valor.



# criar um novo dicionário rapidamente, usando uma lista (ou outro iterável) de chaves.
# Por padrão, os valores dessas chaves serão None.
# Se você quiser, pode passar um valor padrão para todas as chaves.
# É útil para inicializar dicionários com várias chaves de uma vez, sem precisar escrever manualmente.



dict.fromkeys(["telefone", "cidade"], "vazio")
contatos.fromkeys(["telefone", "cidade"], "vazio")


# dict.fromkeys(...) → chamado direto da classe.
# contatos.fromkeys(...) → chamado de uma instância já criada.
# Em ambos os casos, o resultado é um novo dicionário.
# O dicionário original não é modificado.