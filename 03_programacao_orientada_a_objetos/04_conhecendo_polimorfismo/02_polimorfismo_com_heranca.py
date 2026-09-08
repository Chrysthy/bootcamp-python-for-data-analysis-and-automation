# Polimorfismo com Herança

# Mesmo método com comportamento diferente

# Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada da classe pai. 
# Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

class Passaro:
    def voar(self):
        pass 


class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")


class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não voa")


def plano_de_voo(passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())





# herança + sobrescrita + polimorfismo

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# Fix me: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())


# Pardal(Passaro) → herança
# redefinir voar() → sobrescrita
# super().voar() → chamar o método da classe pai
# obj.voar() funcionando com Pardal e Avestruz → polimorfismo