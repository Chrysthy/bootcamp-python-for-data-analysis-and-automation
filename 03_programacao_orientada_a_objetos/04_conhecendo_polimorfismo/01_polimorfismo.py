# Polimorfismo

# Muitas formas!

# A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.


len("python")
len([10, 20, 30])


texto = "Python"
lista = [1, 2, 3, 4]
dicionario = {"nome": "Ana", "idade": 25}

print(len(texto))        # 6
print(len(lista))        # 4
print(len(dicionario))   # 2


# funciona com tipos diferentes de dados:

# str → conta os caracteres
# list → conta os elementos
# dict → conta as chaves

# Isso é polimorfismo: a mesma operação sendo usada em objetos de tipos diferentes.