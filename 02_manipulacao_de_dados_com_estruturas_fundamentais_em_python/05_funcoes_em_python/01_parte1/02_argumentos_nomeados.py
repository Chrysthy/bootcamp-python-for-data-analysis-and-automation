# Argumentos Nomeados

# Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.
# São valores que você passa para uma função quando a chama.
# Servem para personalizar o comportamento da função.

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Posicional — segue a ordem dos parâmetros:
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Nomeado — especifica cada parâmetro:
# Isso é ótimo quando há muitos parâmetros ou quando você quer deixar o código mais legível.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Com dicionário — usando ** para “desempacotar”:
# O ** transforma as chaves do dicionário em argumentos nomeados automaticamente.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
