class Animal:
    # Construtor da classe Animal
    # Recebe o número de patas
    def __init__(self, nro_patas, **kw):
        self.nro_patas = nro_patas

        # Continua a cadeia de herança.
        # Aqui, normalmente chegará no object.
        super().__init__(**kw)

    # Define como o objeto será exibido quando usamos print()
    def __str__(self):
        # self.__class__.__name__ pega o nome da classe do objeto
        # self.__dict__ pega os atributos do objeto em formato de dicionário
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()]
        )}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        # Mamifero "consome" apenas o argumento que pertence a ele
        self.cor_pelo = cor_pelo

        # Passa os argumentos restantes para a próxima classe
        # da cadeia de herança
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        # Ave "consome" o argumento que pertence a ela
        self.cor_bico = cor_bico

        # Passa os argumentos restantes adiante
        super().__init__(**kw)

    
    def __str__(self):
        return 'ave 42'


class Gato(Mamifero):
    pass


# Ornitorrinco herda de Mamifero e Ave
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)
        
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


# Como estamos usando **kw, passamos os argumentos de forma nomeada
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)


ornitorrinco = Ornitorrinco(
    nro_patas=2,
    cor_pelo="Vermelho",
    cor_bico="Laranja"
)

print(ornitorrinco)

# 18:07