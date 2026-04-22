# Indentação e blocos
# É uma forma de manter o código fonte mais legível e manutenível.
# Através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

# Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. 
# Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrogada por ser nosso cliente! Tenha um ótimo dia!")



def depositar(valor):
    saldo = 500
    saldo += valor



sacar(100)