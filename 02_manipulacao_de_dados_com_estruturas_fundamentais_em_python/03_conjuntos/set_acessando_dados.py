# Acessando os dados  
# Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

numeros = {1, 2, 3, 2}
print(numeros)

numeros = list(numeros)
print(numeros)


# A ordem dos elementos pode mudar quando você converte de set para lista, porque o set não garante ordem.

# Se você precisa ordem e unicidade ao mesmo tempo, pode usar list(set(...)) e depois aplicar sorted():

# Assim você garante que os elementos fiquem únicos e ordenados.

numeros = sorted(list({1, 2, 3, 2}))
print(numeros)  # [1, 2, 3]
