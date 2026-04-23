# Estruturas condicionais
# Permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.



#if / if-else / elif
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = float(input("Informe o valor do saque: "))
cheque_especial = 450

#if
# O comando if é usado para verificar uma condição. Se ela for verdadeira, o bloco de código associado será executado.
if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")


