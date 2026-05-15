# Aprendendo a Utilizar Dicionários em Python

# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário.
# Dicionários são delimitados por chaves {}, e contêm uma lista de pares chave:valor separada por vírgulas.

# As chaves de um dicionário são únicas, ou seja, não podem se repetir.
# Dicionários são mutáveis e permitem alterações, desde que respeitem a regra de chave única.

pessoa = {"nome": "Chrystine", "idade": 34}  
# Aqui criamos um dicionário com duas chaves: "nome" e "idade".

pessoa = dict(nome="Chrystine", idade=34)  
# Outra forma de criar dicionário usando a função dict().

pessoa["telefone"] = "3333-1234"   # {"nome": "Chrystine", "idade": 34, "telefone": "3333-1234"}  
# Adicionamos uma nova chave "telefone" ao dicionário já existente.



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