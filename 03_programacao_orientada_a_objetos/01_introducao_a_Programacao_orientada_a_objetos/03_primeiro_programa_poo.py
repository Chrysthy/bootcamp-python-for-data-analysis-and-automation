"""
Nosso primeiro programa POO

João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.

Uma bicicleta pode: buzinar, parar e correr.

Adicione esses comportamentos!

"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18)  # self referência para o objeto, referência explícita 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro


    # métodos são funções que estão dentro de uma classe. Sempre precisa passar um argumento, que é o self
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")

    def trocar_marcha(nro_marcha): # um erro muito comum, pode até funcionar em algumas situações, porque o Python não exige que esse primeiro parâmetro se chame self. Ele só precisa existir. Mas o problema é que nro_marcha vai receber o objeto, e não o número da marcha.
        print(nro_marcha)
        print("Marcha trocada...")

    def get_cor(self): # não é uma prática muito comum, pois os atributos são acessíveis publicamente
        return self.cor

    def __str__(self): # representação legível para ver os valores dentro do objeto
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}" # forma manual

    def __str__(self):  # deixando mais automatizado, dinamicamente ter os valores e se for adicionado mais itens, não precisamos preocupar
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  # acessando a classe pelos atributos

bike_1 = Bicicleta("roxa", "caloi", 2022, 600)

bike_1.buzinar()
bike_1.parar()
bike_1.correr()

# Podemos acessar os atributos da classe
print(bike_1.cor, bike_1.modelo, bike_1.ano, bike_1.valor)


bike_2 = Bicicleta("verde", "monark", 2000, 189)

Bicicleta.buzinar(bike_2) # ou bike_2.buzinar()
print(bike_2.get_cor())

# ver valores dentro do objeto
print(bike_2)


# class Bicicleta:
#     def trocar_marcha(self, nro_marcha):
#         print(nro_marcha)
#         print("Marcha trocada...")

# bike.trocar_marcha(3)

"""
self nos métodos de uma classe

O primeiro parâmetro de um método representa o próprio objeto.
Por convenção, ele é chamado de self.
O Python não se importa com o nome self; poderia ser qualquer nome.
Porém, usar outro nome pode causar confusão.
Quando chamamos objeto.metodo(), o Python passa o próprio objeto automaticamente como primeiro argumento.
Se o método precisar receber outro valor, ele vem depois do self.

self → representa a bicicleta
nro_marcha → representa a marcha escolhida 23:15

"""