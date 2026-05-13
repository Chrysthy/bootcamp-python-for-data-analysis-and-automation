# Função enumerate
# às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso, podemos usar o enumerate

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')


# É importante lembrar que o índice que aparece não é “a posição real” do elemento dentro do conjunto, já que conjuntos não têm ordem fixa. 
# O enumerate apenas numera os itens conforme eles vão sendo percorridos no loop