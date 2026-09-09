# Criando Classes Abstratas com o módulo ABC

# ABC

# Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. 
# O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. 
# Um método se torna abstrato quando decorado com `@abstractmethod`.


from abc import ABC, abstractmethod


# Classe abstrata.
# Ela funciona como um "contrato" para os controles remotos.
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        # Toda classe que herdar de ControleRemoto
        # será obrigada a implementar o método ligar().
        pass

    @abstractmethod
    def desligar(self):
        # Toda classe filha também será obrigada
        # a implementar o método desligar().
        pass

    @property
    @abstractmethod
    def marca(self):
        # Propriedade abstrata.
        #
        # Isso obriga todas as classes filhas
        # a terem uma propriedade chamada marca.
        #
        # Como usamos @property, a marca será acessada
        # como um atributo:
        #
        # controle.marca
        #
        # e não:
        #
        # controle.marca()
        pass


# ControleTV herda de ControleRemoto.
class ControleTV(ControleRemoto):

    def ligar(self):
        # Implementação do método ligar para a TV.
        print("Ligando a TV...")
        print("Ligando!")

    def desligar(self):
        # Implementação do método desligar para a TV.
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        # Implementação da propriedade marca
        # exigida pela classe abstrata.
        return "Philco"


# ControleArCondicionado também herda de ControleRemoto.
class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        # Implementação do método ligar
        # específica para o ar-condicionado.
        print("Ligando o Ar...")
        print("Ligando!")

    def desligar(self):
        # Implementação do método desligar
        # específica para o ar-condicionado.
        print("Desligando o Ar...")
        print("Desligado!")

    @property
    def marca(self):
        # Implementação da propriedade marca.
        return "LG"


# Criando um objeto da classe ControleTV.
controle = ControleTV()

# Chamando os métodos da TV.
controle.ligar()
controle.desligar()

# Como marca é uma @property,
# acessamos sem parênteses.
print(controle.marca)


# Agora a variável controle passa a apontar
# para um objeto ControleArCondicionado.
controle = ControleArCondicionado()

# Chamando os métodos do ar-condicionado.
controle.ligar()
controle.desligar()

# Mostrando a marca do ar-condicionado.
print(controle.marca)



# @abstractmethod
# → obriga a classe filha a implementar um método

# @property
# → permite acessar um método como se fosse um atributo

# @property + @abstractmethod
# → obriga a classe filha a implementar uma propriedade