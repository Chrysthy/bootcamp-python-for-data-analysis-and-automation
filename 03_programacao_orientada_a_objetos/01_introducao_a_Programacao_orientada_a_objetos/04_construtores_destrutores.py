# Métodos __init__ e __del__


# Método construtor

# O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. 
# Para declarar o método construtor da classe, criamos um método com o nome __init__.

# __init__
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acrodado = acordado


# class Cachorro: → cria a classe, ou seja, o molde do objeto.
# __init__ → é o construtor, executado automaticamente quando um objeto é criado.
# self → representa o próprio objeto.
# nome, cor e acordado → são os valores recebidos ao criar o cachorro.
# self.nome = nome → guarda o valor de nome dentro do objeto.
# acordado=True → define True como valor padrão, caso nenhum valor seja informado.

# __init__ inicializa os atributos do objeto. self representa o próprio objeto e permite guardar nele os valores recebidos.


# Método destrutor

# O método destrutor sempre é executado quando uma instância (objeto) é destruída. 
# Destrutores em Python não são tão necessários quanto em C++ porque o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. 
# Para declarar o método destrutor da classe, criamos um método com o nome __del__.

# __del__
class Cachorro:
    def __del__(self):
        print("Destruindo instância")

c = Cachorro()
del c


# __del__ → é o método destrutor.
# Ele pode ser executado quando o objeto é destruído.
# c = Cachorro() → cria um objeto da classe Cachorro.
# del c → remove a referência c.
# Quando o objeto é destruído, aparece: Destruindo instância

# __del__ é chamado quando o objeto é destruído. del remove a referência ao objeto.

# Só um detalhe importante: em Python, não é bom depender de __del__ para coisas críticas, porque o momento exato em que ele será executado pode variar.