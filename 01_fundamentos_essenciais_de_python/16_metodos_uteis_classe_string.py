# Conhecendo métodos úteis da classe string
# Os principais métodos para manipular objetivos do tipo string e interpolar valores de variáveis e entender como funciona o fatiamento

# Maiúscula, minúscula e título
curso = "pYtHon"

print(curso.upper())   # Converte todo o texto da variável 'curso' para letras maiúsculas

print(curso.lower())   # Converte todo o texto da variável 'curso' para letras minúsculas

print(curso.title())   # Converte o texto para "Title Case", ou seja, cada palavra começa com letra maiúscula


# Eliminando espaços em branco
palavra = "   Python  "

print(palavra.strip())   # Remove espaços em branco do início e do fim da string

print(palavra.lstrip())  # Remove espaços em branco apenas do lado esquerdo (início) da string

print(palavra.rstrip())  # Remove espaços em branco apenas do lado direito (final) da string


# Junções e centralização
palavra2 = "Python"

print(palavra2.center(10, "#")) # Centraliza a string 'Python' em um espaço de largura 10, preenchendo os espaços restantes com o caractere '#'. O segundo caractere é opcional
# Resultado: "##Python##"

print(".".join(palavra2)) # Insere o caractere '.' entre cada letra da string 'Python'.
# Resultado: "P.y.t.h.o.n"


