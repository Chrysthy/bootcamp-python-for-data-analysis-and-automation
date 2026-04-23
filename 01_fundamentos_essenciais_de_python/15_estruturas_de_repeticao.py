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



