# Estruturas de Repetição
# São estruturas para repetir um trecho de código um determinado número de vezes. Pode ser conhecido previamente ou determinado através de uma expressão lógica

# exemplo sem repetição - exibindo os 2 números seguintes
a = int(input("Informe um número inteiro:"))
print(a)

a += 1
print(a)

a += 1
print(a)


# exemplo com repetição for
# é usado para repetição (loop), ou seja, executar um bloco de código várias vezes de forma controlada. 
# Ele percorre uma sequência de elementos (como listas, strings, intervalos de números) e executa instruções para cada item.
# faz sentido usar quando sabemos o número exato de vezes que deve ser executado ou quando queremos percorrer um objeto iterável

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha



# exemplo com repetição for/else
# não é muito comum no dia a dia
# O else associado ao for é executado quando o loop termina normalmente, ou seja, sem interrupções por um break.
# O else em um for não significa “caso contrário” como no if. Ele é executado sempre que o loop terminar sem break.
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")




# Função Range
# é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). 0 a 5 - 0 incluso mas 5 não, para no 4.
# recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional)
list(range(4)) # [0,1,2,3] - o list transforma em uma lista

for numero in range(0,11):
    print(numero, end="")
# 0 1 2 3 4 5 6 7 8 9 10

# tabuada de 5
for numero in range(0, 51, 5):
    print(numero)
    print(numero, end=" ")

# 0 5 10 15 20 25 30 35 40 45 50



# Comando while
# é usado para repetir um bloco de código várias vezes, mas faz sentido usar while quando não sabemos o número exato de vezes que o bloco de código deve ser executado
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando")

    elif opcao == 2:
        print("Exibindo extrato")

else:
    print("Obrigada por usar nosso sistema bancário, até logo!")







