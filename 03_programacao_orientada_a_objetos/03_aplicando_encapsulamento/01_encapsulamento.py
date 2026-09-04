# Encapsulamento

# O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma 
# unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados.

# Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.



# ------------------------------------------------------------
# PROTEÇÃO DE ACESSO / ENCAPSULAMENTO
# ------------------------------------------------------------
#
# O encapsulamento é usado para controlar o acesso aos
# atributos e métodos de uma classe.
#
# Em diagramas UML:
#
# -  significa privado
# +  significa público
#
# Exemplo:
#
# Conta
# -------------------------
# - saldo: float
# -------------------------
# + depositar(valor: float)
# + sacar(valor: float)
#
# Nesse exemplo:
#
# - saldo é um atributo privado
# + depositar() é um método público
# + sacar() é um método público
#
# A ideia é evitar que o saldo seja alterado diretamente.
# A alteração deve acontecer através dos métodos da classe.
#
# Em Python, não existe um "private" totalmente bloqueado
# como em algumas outras linguagens.
#
# Por convenção:
#
# atributo        -> público
# _atributo       -> protegido (convenção)
# __atributo      -> privado / name mangling
#
# ------------------------------------------------------------