class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


class Motocicleta(Veiculo):
    pass

    
class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __int__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")



moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()


carro = Carro("branco", "xde-0098", 4)
print(carro)
carro.ligar_motor()
# carro.esta_carregado() erro, pois o carro não tem esse método


caminhao = Caminhao("roxo", "gfd-8712", 8, False)
print(caminhao)
caminha.ligar_motor()
caminhao.esta_carregado()


print(moto)
print(carro)
print(caminhao)