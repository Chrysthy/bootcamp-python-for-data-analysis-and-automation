# Lendo valores com a função input - lê a entrada, converte para string e retorna o valor. Não precisa baixar nada, porque é builtin
name = input("Informe o seu nome: ")
age = input("Informe a sua idade: ")
print(name, idade)

# exibindo valores com a função print
nome = "Chrystine"
sobrenome = "Martins"

# argumento obrigatório do tipo varargs de objetos
print(nome, sobrenome)


# 4 argumentos opcionais (sep, end, file e flush) - parâmetros
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")


# pode usar mais junto
# print(nome, sobrenome, sep="#", end="...\n")