# função com parâmetros posicionais e keyword only — uma combinação poderosa para controlar como os argumentos são passados em Python.

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


# Explicação:

# Os parâmetros antes da barra / (modelo, ano, placa) são posicionais apenas — não podem ser passados por nome.

# Os parâmetros depois do asterisco * (marca, motor, combustivel) são keyword only — devem ser passados explicitamente pelo nome.

# Isso ajuda a deixar o código mais claro e evita erros de ordem ou ambiguidade.



def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Erro: os três primeiros são posicionais apenas


# Misturando três tipos de parâmetros:

# Posicionais apenas — antes da barra /:
# modelo, ano, placa → devem ser passados somente por posição.

# Parâmetros padrão (posicionais ou nomeados) — entre / e *:
# marca → pode ser passado por posição ou nome.

# Keyword only — depois do *:
# motor, combustivel → devem ser passados explicitamente pelo nome.

# Essa combinação é útil quando você quer garantir que certas informações (como modelo e ano) sempre sejam passadas na ordem correta, 
# enquanto outras (como motor e combustível) tenham nomes explícitos para clareza.