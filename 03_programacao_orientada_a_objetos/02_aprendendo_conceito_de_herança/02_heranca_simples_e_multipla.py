# Herança simples & Herança múltipla

# Herança simples
# Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.

class A:
    pass 

class B(A):
    pass


# Herança múltipla
# Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.

class A:
    pass 

class B:
    pass

class C(A, B):
    pass

# só a classe C que extende da class A e também da B. Class C é filha de A e B