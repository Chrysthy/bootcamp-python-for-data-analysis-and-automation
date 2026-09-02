# Herança em POO

# **O que é herança**?
# Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).


# **Benefícios da herança**

# * Representa bem os relacionamentos do mundo real.
# * Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
# * É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.


# Sintaxe da herança
class A:
    pass 

class B(A):
    pass



# Herança é quando uma classe pode aproveitar características e comportamentos de outra classe.

# Pensa assim:

# existe uma classe mais geral: Animal
# existe uma classe mais específica: Cachorro
# todo cachorro é um animal
# então Cachorro pode herdar coisas de Animal