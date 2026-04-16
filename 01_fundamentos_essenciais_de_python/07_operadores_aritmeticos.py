# Operadores aritméticos

produto_1 = 20
produto_2 = 10

# soma
print(1 + 1)
print(produto_1 + produto_2)

# subtração
print(10 - 2)
print(produto_1 - produto_2)

# multiplicação
print(4 * 3)
print(produto_1 * produto_2)

# divisão (normal que retorna float com casa decimais)
print(12 / 3)
print(produto_1 / produto_2)

# divisão inteira
print(12 // 2)
print(produto_1 // produto_2)

# módulo - resto da divisão
print(10 % 3) # 1
print(produto_1 % produto_2)

# exponenciação
print(2 ** 3) # 8
print(produto_1 ** produto_2)


# Precedência dos operadores
# regra que indica quais operações devem ser executadas primeiro
# veja tabela no notion

print(10 - 5 * 2) # 0

print((10 - 5) * 2) # 10

print(10 ** 2 * 2) # 200

print(10 ** (2 * 2)) # 10000

print(10 / 2 * 4) # 20.0