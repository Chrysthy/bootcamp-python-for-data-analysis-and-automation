# Classe base
class Animal:

    # Método construtor da classe Animal.
    # Recebe o número de patas do animal.
    #
    # **kw representa outros argumentos nomeados que ainda
    # podem existir na cadeia de herança.
    def __init__(self, nro_patas, **kw):
        self.nro_patas = nro_patas

        # Continua seguindo a cadeia de herança definida pelo MRO.
        #
        # Neste exemplo, Animal é a última classe personalizada
        # da cadeia, então depois dele normalmente chegamos em object.
        super().__init__(**kw)

    # Define o que será mostrado quando fizermos:
    #
    # print(objeto)
    #
    # Se uma classe filha não tiver seu próprio __str__,
    # ela poderá usar este.
    def __str__(self):

        # self.__class__.__name__
        # pega o nome real da classe do objeto.
        #
        # Exemplo:
        # Gato
        # Ornitorrinco

        # self.__dict__
        # retorna os atributos do objeto em formato de dicionário.
        #
        # Exemplo:
        # {
        #     "cor_pelo": "Preto",
        #     "nro_patas": 4
        # }

        # A compreensão de lista transforma cada atributo
        # em uma string no formato:
        #
        # chave=valor
        #
        # Depois o ", ".join(...) junta tudo usando vírgula.
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()]
        )}"


# Mamifero herda de Animal.
class Mamifero(Animal):

    def __init__(self, cor_pelo, **kw):

        # Mamifero pega ("consome") somente o argumento
        # que pertence a ele: cor_pelo.
        self.cor_pelo = cor_pelo

        # Os argumentos restantes ficam dentro de **kw
        # e são enviados para a próxima classe da cadeia.
        #
        # IMPORTANTE:
        # super() não significa simplesmente "chamar meu pai".
        #
        # Ele chama a PRÓXIMA classe de acordo com o MRO
        # (Method Resolution Order).
        super().__init__(**kw)

    def __str__(self):
        return "Mamifero"


# Ave também herda de Animal.
class Ave(Animal):

    def __init__(self, cor_bico, **kw):

        # Ave pega somente o argumento que pertence a ela.
        self.cor_bico = cor_bico

        # Passa os argumentos restantes para a próxima
        # classe definida pelo MRO.
        super().__init__(**kw)

    def __str__(self):
        return "ave 42"


# Gato herda somente de Mamifero.
#
# Como não criamos nenhum método aqui,
# ele usará os métodos herdados.
class Gato(Mamifero):
    pass


# Ornitorrinco possui HERANÇA MÚLTIPLA:
#
# Mamifero + Ave
#
# A ordem das classes importa.
class Ornitorrinco(Mamifero, Ave):

    def __init__(self, cor_bico, cor_pelo, nro_patas):

        # Mostra a ordem em que o Python irá procurar
        # os métodos das classes.
        #
        # O resultado será aproximadamente:
        #
        # Ornitorrinco
        # Mamifero
        # Ave
        # Animal
        # object
        print(Ornitorrinco.mro())

        # Como estamos usando herança múltipla,
        # enviamos TODOS os argumentos usando nomes.
        #
        # O super() olha o MRO e chama primeiro:
        #
        # Mamifero.__init__()
        super().__init__(
            cor_pelo=cor_pelo,
            cor_bico=cor_bico,
            nro_patas=nro_patas
        )

    def __str__(self):
        return "Ornitorrinco"


# -------------------------------------------------
# CRIANDO UM GATO
# -------------------------------------------------

# Gato não possui __init__, então o Python procura
# esse método na classe Mamifero.
#
# Mamifero recebe:
#
# cor_pelo="Preto"
#
# E nro_patas=4 fica dentro de **kw.
gato = Gato(
    nro_patas=4,
    cor_pelo="Preto"
)

# Como Gato não possui __str__,
# ele encontra o __str__ de Mamifero.
#
# Resultado:
#
# Mamifero
print(gato)


# -------------------------------------------------
# CRIANDO UM ORNITORRINCO
# -------------------------------------------------

ornitorrinco = Ornitorrinco(
    nro_patas=2,
    cor_pelo="Vermelho",
    cor_bico="Laranja"
)

# Ornitorrinco possui seu próprio __str__,
# então será ele que será executado.
#
# Resultado:
#
# Ornitorrinco
print(ornitorrinco)