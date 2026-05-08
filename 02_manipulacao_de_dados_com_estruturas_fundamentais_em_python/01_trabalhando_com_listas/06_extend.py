# .extend
linguagens = ['python', 'js', 'c']   # lista inicial com 3 linguagens

print(linguagens)                    # imprime a lista original -> ['python', 'js', 'c']

linguagens.extend(['java', 'csharp']) # adiciona 'java' e 'csharp' separadamente ao final da lista

print(linguagens)                    # imprime a lista atualizada -> ['python', 'js', 'c', 'java', 'csharp']


# Diferente de .append(), que adiciona um único item (mesmo que seja uma lista inteira), o .extend() desempacota os elementos e coloca cada um separadamente.
# Não remove valores duplicados
# Ele pega a lista original e coloca tudo que passar entre ([]) no final da lista linguagens
# Sintaxe:
# lista.extend([elemento1, elemento2, ...])