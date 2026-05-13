# Iterar conjuntos
# A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)


# O loop vai imprimir cada elemento do conjunto.
# Mas atenção: como os sets não têm ordem fixa, a saída pode variar — às vezes começa pelo "gol", outras pelo "palio". O importante é que todos os elementos aparecem uma vez.