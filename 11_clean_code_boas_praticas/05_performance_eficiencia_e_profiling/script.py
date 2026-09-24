import time

inicio = time.time()

for i in range(1000000):
    pass

fim = time.time()

print("Tempo:", fim - inicio)



# exemplo com lista
numeros = list(range(1000000))

# forma rápida
soma = sum(numeros)

print(soma)



# Projeto final
def calcular_total_vendas(vendas):
    return sum(vendas)


dados = [100, 200, 300, 400]

resultado = calcular_total_vendas(dados)

print("Total:", resultado)