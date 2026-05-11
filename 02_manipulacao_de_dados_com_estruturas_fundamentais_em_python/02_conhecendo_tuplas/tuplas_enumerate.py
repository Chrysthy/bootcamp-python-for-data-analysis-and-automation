# Função enumerate
# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate

carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')


# enumerate(carros) retorna pares (índice, valor) para cada item da tupla.

# A variável indice recebe a posição do elemento.

# A variável carro recebe o valor correspondente.

# O print exibe ambos em cada iteração.

# Isso é muito útil quando você precisa iterar com índices sem ter que usar range(len(...)).