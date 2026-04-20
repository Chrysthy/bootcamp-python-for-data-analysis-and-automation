# Operadores de identidade 
# compara se os dois objetos ocupam a mesma posição na memória - É quando duas variáveis apontam pro MESMO objeto

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # True

curso is not nome_curso # False

saldo is limite # True


