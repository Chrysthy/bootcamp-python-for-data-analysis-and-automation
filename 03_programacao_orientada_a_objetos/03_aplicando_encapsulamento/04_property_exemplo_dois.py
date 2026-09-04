class Pessoa:

    def __init__(self, nome, ano_nascimento):
        # Armazena os valores em atributos internos.
        # O "_" indica, por convenção, que esses atributos
        # não devem ser manipulados diretamente fora da classe.
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        # Permite acessar o nome como se fosse um atributo:
        #
        # pessoa.nome
        #
        # mas, por trás, este método está sendo executado.
        return self._nome

    # Poderíamos criar um setter caso quiséssemos
    # controlar a alteração do nome.
    #
    # @nome.setter
    # def nome(self, value):
    #     # Aqui poderia existir alguma validação
    #     # antes de alterar o nome.
    #     self._nome = value

    @property
    def idade(self):
        # A idade não precisa ser armazenada diretamente.
        # Ela pode ser calculada sempre que for consultada.
        _ano_atual = 2026

        # Calcula a idade usando o ano atual
        # e o ano de nascimento armazenado no objeto.
        return _ano_atual - self._ano_nascimento


# Cria uma pessoa com:
# nome = "Chrystine"
# ano de nascimento = 1992
pessoa = Pessoa("Chrystine", 1992)


# pessoa.nome chama a @property nome.
#
# pessoa.idade chama a @property idade,
# que calcula:
#
# 2026 - 1992 = 34
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")




# Para ter o ano automaticamente

# from datetime import datetime


# class Pessoa:

#     def __init__(self, nome, ano_nascimento):
#         self._nome = nome
#         self._ano_nascimento = ano_nascimento

#     @property
#     def nome(self):
#         return self._nome

#     @property
#     def idade(self):
#         # Pega o ano atual automaticamente do sistema
#         ano_atual = datetime.now().year

#         # Calcula a idade com base no ano atual
#         return ano_atual - self._ano_nascimento


# pessoa = Pessoa("Chrystine", 1992)

# print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")