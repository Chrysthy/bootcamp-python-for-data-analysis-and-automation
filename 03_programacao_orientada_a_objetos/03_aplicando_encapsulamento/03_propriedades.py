# Propriedades

# Para que servem?

# Com o property() do Python, você pode criar atributos gerenciados em suas classes.
# Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

class Foo:

    def __init__(self, x=None):
        # Guarda o valor recebido em um atributo "interno".
        # O underline indica, por convenção, que esse atributo
        # não deve ser manipulado diretamente fora da classe.
        self._x = x

    @property
    def x(self):
        # Permite acessar x como se fosse um atributo:
        #
        # foo.x
        #
        # em vez de:
        #
        # foo.x()
        #
        # Se self._x possuir um valor "falsy", retorna 0.
        # Exemplos de valores falsy: None, 0, False, "".
        return self._x or 0

    @x.setter
    def x(self, value):
        # O setter é executado quando fazemos:
        #
        # foo.x = algum_valor

        # Usa o valor atual de _x.
        # Se _x for None ou outro valor falsy, considera 0.
        _x = self._x or 0

        # Faz o mesmo com o novo valor recebido.
        _value = value or 0

        # Em vez de simplesmente substituir o valor,
        # este setter SOMA o valor novo ao valor atual.
        self._x = _x + _value

    @x.deleter
    def x(self):
        # O deleter é executado quando fazemos:
        #
        # del foo.x
        #
        # Neste exemplo, ele NÃO apaga realmente o atributo.
        # Ele apenas muda o valor de _x para -1.
        self._x = -1


# Cria um objeto com _x = 10.
foo = Foo(10)

# Acessa a propriedade x.
# O @property executa o método x().
#
# Saída: 10
print(foo.x)


# Parece que estamos atribuindo 10 a x,
# mas como existe um @x.setter, ele será executado.
#
# Valor atual: 10
# Novo valor: 10
#
# 10 + 10 = 20
foo.x = 10

# Saída: 20
print(foo.x)


# Chama o método decorado com @x.deleter.
#
# Neste exemplo, _x passa a valer -1.
del foo.x

# Saída: -1
print(foo.x)
