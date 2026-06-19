# Parâmetros especiais 

# Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome.
# Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pela qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar 
# para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.


# Somente por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# Os parâmetros antes da barra / (modelo, ano, placa) devem ser passados por posição, nunca por nome. É obrigatório ser por posição

# Os parâmetros depois da barra (marca, motor, combustivel) podem ser passados por nome ou posição.

# Isso ajuda a evitar ambiguidades e torna o código mais legível e eficiente.