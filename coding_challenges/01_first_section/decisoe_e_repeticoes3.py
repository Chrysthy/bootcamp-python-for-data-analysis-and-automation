# Desafio
# Você faz parte da equipe de transformação digital de uma consultoria que está integrando dados de diferentes sistemas legados. Cada sistema armazena nomes de clientes de formas variadas: alguns usam letras maiúsculas, outros minúsculas, e há casos em que nomes vêm com espaços extras no início ou no fim. Para garantir a padronização e facilitar a análise, sua tarefa é criar um programa que normalize esses nomes, removendo espaços desnecessários e ajustando a capitalização de acordo com o padrão: a primeira letra de cada palavra deve ser maiúscula e as demais, minúsculas.

# Implemente um programa que receba uma string representando o nome de um cliente, possivelmente com letras em qualquer caixa e espaços extras no início ou no fim. O programa deve retornar o nome formatado corretamente, com apenas um espaço entre as palavras e cada palavra iniciando com letra maiúscula.

# Entrada
# Uma única linha contendo uma string representando o nome de um cliente, que pode conter letras maiúsculas ou minúsculas e espaços extras no início ou no fim.

# Saída
# Uma única linha contendo o nome do cliente formatado: cada palavra deve começar com letra maiúscula, as demais letras devem ser minúsculas, e deve haver apenas um espaço entre as palavras, sem espaços extras no início ou no fim.

# Lê a entrada do usuário (nome do cliente)
entrada = input()

# TODO: Remova espaços extras no início/fim e divida a string em palavras
entrada = entrada.strip()
palavras = entrada.split()

# Dica: Use métodos de string para limpar e separar as palavras

# Capitalize cada palavra (primeira letra maiúscula, demais minúsculas)

palavras_formatadas = [palavra.capitalize() for palavra in palavras]

# Junte as palavras com um único espaço entre elas

nome_formatado = ' '.join(palavras_formatadas)

# Exiba o nome formatado
print(nome_formatado)
