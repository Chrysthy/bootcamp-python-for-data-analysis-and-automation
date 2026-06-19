# parâmetros apenas por palavra‑chave (keyword only) em Python — ou seja, todos os argumentos devem ser passados explicitamente pelo nome.

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# Explicação:

# O * na definição da função indica que todos os parâmetros seguintes devem ser passados por nome.

# Isso torna o código mais legível e evita confusões com a ordem dos argumentos.

# A primeira chamada é válida, pois usa nomes explícitos.

# A segunda é inválida, porque tenta usar argumentos posicionais antes dos nomeados.