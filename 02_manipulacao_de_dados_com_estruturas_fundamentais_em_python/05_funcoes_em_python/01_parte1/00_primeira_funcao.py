# O que são funções?

# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros; esses parâmetros podem ou não ter valores padrões. 
# Usar funções torna o código mais legível e possibilita o reaproveitamento de código. 
# Programar baseado em funções é o mesmo que dizer que estamos programando de maneira estruturada.

# Exemplo

# Sem parâmetro
def exibir_mensagem():
    print("Olá Mundo!")


# Com parâmetro
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


# Com parâmetro e valor padrão
def exibir_mensagem_3(nome="Chrystine"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Noob")
# exibir_mensagem_2("Noob") → podemos passar o valor direto 
exibir_mensagem_3()
exibir_mensagem_3(nome="Collin")


# Saídas esperadas:

# exibir_mensagem() → imprime Olá Mundo!
# exibir_mensagem_2(nome="Noob") → imprime Seja bem vindo Noob!
# exibir_mensagem_3() → como não foi passado argumento, usa o valor padrão → Seja bem vindo Chrystine!
# exibir_mensagem_3(nome="Collin") → substitui o valor padrão → Seja bem vindo Collin!



# Termo	        Onde aparece	            Função
# Parâmetro	    Na definição da função	    Representa uma variável que receberá um valor
# Argumento	    Na chamada da função	    É o valor real passado ao parâmetro


# Conceitos importantes:
    # Função sem parâmetro: não recebe valores externos, executa sempre o mesmo bloco.

    # Função com parâmetro: recebe valores externos e usa dentro do código.

    # Parâmetro com valor padrão: se não for passado argumento, usa o valor definido na função.

    # Isso te dá flexibilidade: pode chamar a função com ou sem argumentos, dependendo da situação.