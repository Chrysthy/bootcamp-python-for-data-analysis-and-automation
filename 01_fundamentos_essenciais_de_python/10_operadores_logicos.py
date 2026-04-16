# Operadores lógico

saldo = 1000
saque = 200
limite = 100

# operador de comparação
saldo >= saque # True
saque <= limite # False

# -------------------------------------------------

# operador lógico E - and
# as duas precisam ser verdadeiras para ser True
saldo >= saque and saque <= limite # False

# -------------------------------------------------

# operador lógico OU - or
# para ser falso, os dois precisam ser False
# se apenas um for verdadeiro, temos True
saldo >= saque or saque <= limite # True

# -------------------------------------------------

# operação negação - é o iverso da verdade
# inverte o valor lógico
# se tal coisa for True, vira False
# se tal coisa for False, vira True
# uma sequencia vazia, sem elementos é considerada False
contatos_emergencia = []

not 1000 > 1500 # é False 
# True

not contatos_emergencia # lista vazia é False - é uma sequencia de objetos
# True

not "saque 1500;" # é True porque tem um valor, é uma string com um valor - é uma sequencia de caracteres
# False

not "" # string vazia é Flase
# True

# -------------------------------------------------

# Parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # True

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True

# Outro jeito de fazer, quebrando a expressão grande
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(expressao, expressao_2)
print(conta_normal_com_saldo_suficiente)
print(conta_especial_com_saldo_suficiente)
print(expressao_3)


# Na condição and para ser True tudo tem que ser True
print(True and True)
print(True and True and True)
print(True and False)
print(False and False)

# Na condição or para ser True apenas um tem que ser True
print(True or True)
print(True or False)
print(False or False)
print(False or False or False)
