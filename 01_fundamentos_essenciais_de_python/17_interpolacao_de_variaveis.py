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









