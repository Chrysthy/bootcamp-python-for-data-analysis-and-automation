# Escopo local e escopo global

# Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. 
# Portanto, alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. 
# Para usar objetos globais utilizamos a palavra‑chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
# Essa NÃO é uma boa prática e deve ser evitada.

salario = 2000 # variável com escopo global, está fora da função

def salario_bonus(bonus):
    global salario # global para informar que estamos pegando a variável de escopo global

   lista_auxiliar = lista.copy() # quando colocamos um objeto mutável, temos sempre que lembrar de criar uma cópia dele para que ele não altere a refeência externa.
   lista_auxiliar.append(2) 
   print(f"Lista aux = {lista_auxiliar}") 

    salario += bonus
    return salario


lista = [1] 

salario_com_bonus = salario_bonus(500, lista) # 2500
print(salario_com_bonus)
print(lista)