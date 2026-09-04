# Recursos Públicos e Privados

# * Modificadores de acesso *
# Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métodos da classe.
# Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada.


# * Definição *
# Público: Pode ser acessado de fora da classe.
# Privado: Só pode ser acessado pela classe.


# * Público/Privado *
# Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador Python não irá garantir a proteção do recurso, 
# mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos 
# manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.

class Conta:

    def __init__(self, nro_agencia, saldo=0):
        # _saldo indica que este atributo é de uso interno da classe.
        # O underline é uma convenção em Python:
        # ele não impede o acesso, apenas indica que não devemos
        # manipular esse atributo diretamente fora da classe.
        self._saldo = saldo

        # nro_agencia é um atributo público.
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # Altera o saldo através de um método da própria classe.
        self._saldo += valor

    def sacar(self, valor):
        # Diminui o saldo através de um método da própria classe.
        self._saldo -= valor

    def mostrar_saldo(self):
        # Retorna o saldo sem precisar acessá-lo diretamente
        # fora da classe.
        return self._saldo


# Cria uma conta com agência "0001" e saldo inicial de 100.
conta = Conta("0001", 100)

# Deposita mais 100.
conta.depositar(100)

# Como nro_agencia é público, pode ser acessado diretamente.
print(conta.nro_agencia)

# O saldo é consultado através do método da classe.
print(conta.mostrar_saldo())


# Isso FUNCIONA, mas não é recomendado:
# conta._saldo += 100
#
# Como _saldo começa com underline, a convenção indica
# que ele deve ser tratado como um atributo interno.


# Isso também FUNCIONA, mas não é recomendado:
# print(conta._saldo)
#
# O ideal é acessar o saldo através de mostrar_saldo().




# O _saldo não bloqueia o acesso de verdade. O _ é só uma convenção para dizer: “esse atributo é interno, evite mexer nele diretamente fora da classe”.

# A diferença é mais de intenção:

# saldo     público
# _saldo    "interno/protegido" por convenção
# __saldo   usa name mangling

# Mesmo __saldo não fica 100% inacessível; o Python só muda internamente o nome do atributo.


# Isso dá erro:
# print(conta.__saldo)

# Mas ainda é possível acessar assim:
# print(conta._Conta__saldo)

# Então a ideia principal é:

# _saldo → “não mexa diretamente, por favor”
# __saldo → dificulta mais o acesso
# Python não tem private rígido como Java ou C++