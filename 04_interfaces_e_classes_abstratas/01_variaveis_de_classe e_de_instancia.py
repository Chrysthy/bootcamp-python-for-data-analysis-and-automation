# Variáveis de classe e Variáveis de instância


# Atributos do objeto

# Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), 
# já os atributos de classe são compartilhados entre os objetos.


class Estudante:
    # Atributo de classe
    # É compartilhado por todos os objetos criados a partir da classe Estudante
    escola = "DIO"

    def __init__(self, nome, numero):
        # Atributos de instância
        # Cada objeto terá seu próprio nome e seu próprio numero
        self.nome = nome
        self.numero = numero

    def __str__(self):
        # Define como o objeto será mostrado quando usamos print()
        return f"{self.nome} ({self.numero}) - {self.escola}"


# Criando uma instância/objeto da classe Estudante
chrys = Estudante("Chrystine", 56451)

# Criando outro objeto da mesma classe
be = Estudante("Noob", 17323)



# Uma forma simples de lembrar:

# Classe:
# escola = "DIO"
# → informação que pode ser comum a todos.

# Instância:
# self.nome
# self.numero
# → informação específica de cada estudante.