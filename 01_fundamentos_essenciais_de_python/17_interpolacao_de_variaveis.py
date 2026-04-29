# Interpolação de variáveis

# Em Python temos 3 formas de interpolar variáveis em strings:

    # Usando o sinal %
    # Utilizando o método format
    # Utilizando f-strings

# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro.
# Por esse motivo, iremos focar nas duas últimas.


# ===========================================================================

# Usando o operador %
python
nome = "Chrystine"
idade = 25

print("Meu nome é %s e tenho %d anos." % (nome, idade))
# Resultado: Meu nome é Chrystine e tenho 25 anos.


nome = "Chrystine"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." 
      % (nome, idade, profissao, linguagem))


# %s → indica que ali será inserida uma string (texto).

# %d → indica que ali será inserido um inteiro (número).

# Depois da string, vem o operador % seguido de uma tupla com as variáveis (nome, idade, profissao, linguagem).
# Cada variável substitui o marcador correspondente na ordem.




# ===========================================================================
# Usando o método format()

# Forma 1
python
nome = "Chrystine"
idade = 25

print("Meu nome é {} e tenho {} anos.".format(nome, idade))
# Resultado: Meu nome é Chrystine e tenho 25 anos.


# Forma 2
nome = "Chrystine"
idade = 28
profissao = "Progamador"
linguagem = "Python"

# Com números (ordem definida manualmente)
print("Olá, me chamo {3}. Eu tenho {1} anos, trabalho como {2} e estou matriculado no curso de {0}."
      .format(linguagem, idade, profissao, nome))


# {} → substitui na ordem em que os argumentos aparecem.

# {0}, {1}, {2}, {3} → você escolhe qual argumento usar, pela posição (começa em 0).

# Isso é útil quando você quer reutilizar ou reordenar variáveis sem precisar mudar a lista no .format().


# Forma 3
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Aqui, cada chave {nome}, {idade}, {profissao}, {linguagem} é associada ao argumento passado no .format().
# Isso deixa claro qual variável está sendo usada em cada parte da frase.



# Forma 4
# Outra forma é usar um dicionário e o operador ** para "desempacotar" os valores
pessoa = {
    "nome": "Guilherme",
    "idade": 28,
    "profissao": "Programador",
    "linguagem": "Python"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}."
      .format(**pessoa))


# O **pessoa faz com que o Python associe automaticamente cada chave do dicionário ao marcador correspondente na string.
# Isso é muito útil quando você já tem os dados organizados em um dicionário e não quer escrever cada variável manualmente.




# ===========================================================================


# Usando f-strings (Python 3.6+)
nome = "Chrystine"
idade = 25

print(f"Meu nome é {nome} e tenho {idade} anos.")
# Resultado: Meu nome é Chrystine e tenho 25 anos.




