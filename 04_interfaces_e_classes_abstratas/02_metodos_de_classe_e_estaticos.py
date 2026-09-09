# Métodos de classe e Métodos estático

# Métodos de classe
# Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância 
# do objeto.


# Métodos estáticos
# Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. 
# Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.



# Métodos de classe x métodos estáticos
# * Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
# * Um método de classe pode acessar ou modificar o estado da classe, enquanto um método estático não pode acessá-lo ou modificá-lo.


# Quanto utilizar método de classe ou estático

# Geralmente usamos o método de classe para criar métodos de fábrica.
# Geralmente usamos métodos estáticos para criar funções utilitárias.]


class Pessoa:

    def __init__(self, nome=None, idade=None):
        # O __init__ é executado quando criamos um objeto Pessoa.
        # self representa o próprio objeto criado.
        self.nome = nome
        self.idade = idade


    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # @classmethod transforma esse método em um método de classe.
        #
        # Em vez de receber "self", ele recebe "cls".
        # cls representa a própria classe Pessoa.

        print(cls)
        # Vai mostrar algo parecido com:
        # <class '__main__.Pessoa'>

        idade = 2026 - ano
        # Calcula a idade usando o ano de nascimento.
        # Aqui mês e dia ainda não estão sendo utilizados.

        return cls(nome, idade)
        # É como fazer:
        # return Pessoa(nome, idade)
        #
        # Mas usamos cls porque esse método está ligado à classe.


    @staticmethod
    def e_maior_idade(idade):
        # @staticmethod cria um método estático.
        #
        # Ele não recebe self nem cls.
        # Ele apenas recebe os dados necessários para fazer sua tarefa.

        return idade >= 18
        # Retorna True se a idade for 18 ou mais.
        # Retorna False caso contrário.


# Criando uma Pessoa normalmente,
# através do __init__
p = Pessoa("Chrystine", 34)

print(p.nome, p.idade)
# Chrystine 34


# Criando uma Pessoa usando o método de classe
p2 = Pessoa.criar_de_data_nascimento(
    1994, 3, 21, "Chrystine"
)

print(p2.nome, p2.idade)
# Chrystine 32


# Chamando o método estático
print(Pessoa.e_maior_idade(18))
# True

print(Pessoa.e_maior_idade(8))
# False


# A parte mais importante desse exemplo é perceber a diferença entre os três tipos:
# 
# def __init__(self, ...)#  
# self → trabalha com um objeto específico.
# 
# @classmethod
# def criar_de_data_nascimento(cls, ...)# 
# cls → trabalha com a classe.# 

# @staticmethod
# def e_maior_idade(idade)# 
# Não recebe self nem cls → é praticamente uma função utilitária que faz sentido ficar dentro da classe.


# self → objeto
# cls → classe
# staticmethod → não precisa nem do objeto nem da classe.