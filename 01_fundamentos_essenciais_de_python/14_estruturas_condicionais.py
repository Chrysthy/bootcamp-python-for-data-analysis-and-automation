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


# if-else
# O if-else permite tratar duas situações: quando a condição é verdadeira e quando é falsa.
if saldo >= saque:
    print("Realizando saque")
else:
    print("Saldo insuficiente!")


# elif
# O elif (abreviação de else if) é usado quando existem múltiplas condições possíveis. Ele evita o uso de vários if independentes.
opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantidade para o saque:"))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção inválida.")



