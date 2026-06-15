# Retornando Valores

# Para retornar um valor, utilizamos a palavra reservada return.
# Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

def calcular_total(numeros: list[int]) -> int:
    """Retorna a soma de todos os números da lista."""
    return sum(numeros)


def retornar_antecessor_e_sucessor(numero: int) -> tuple[int, int]:
    """Retorna o antecessor e o sucessor de um número."""
    return numero - 1, numero + 1


calcular_total([10, 20, 34]) #64
retornar_antecessor_e_sucessor(10) # (9, 11)


def func_3():
    print("Olá, Mundo!")
    return None # pode ou não ser colocado. Vai dar o mesmo resultado quando fizer o print (veja abaixo)


print(func_3()) # none