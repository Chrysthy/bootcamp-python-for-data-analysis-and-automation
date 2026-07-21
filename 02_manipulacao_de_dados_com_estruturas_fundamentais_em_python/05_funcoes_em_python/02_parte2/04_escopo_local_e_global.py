# Escopo local e escopo global

# Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. 
# Portanto, alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. 
# Para usar objetos globais utilizamos a palavra‑chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
# Essa NÃO é uma boa prática e deve ser evitada.

salario = 2000 # variável com escopo global, está fora da função

def salario_bonus(bonus):
    global salario # global para informar que estamos pegando a variável de escopo global
    salario += bonus
    return salario

salario_bonus(500) # 2500