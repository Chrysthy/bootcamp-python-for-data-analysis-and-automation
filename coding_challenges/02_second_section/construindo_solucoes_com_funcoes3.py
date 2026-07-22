# Desafio
# Você foi contratado por uma consultoria em TI para ajudar a organizar o sistema de cadastro de clientes. O time percebeu que o código está ficando difícil de manter, pois várias operações simples, como padronizar nomes e validar e-mails, estão espalhadas e duplicadas em diferentes partes do projeto. Sua missão é criar funções reutilizáveis que centralizem essas operações, facilitando futuras manutenções e evitando erros. Para isso, você deve implementar uma função que receba um nome completo e um e-mail, valide se o e-mail contém exatamente um caractere '@' e pelo menos um ponto '.' após o '@', e retorne o nome formatado (primeira letra de cada palavra em maiúsculo) seguido de ' - OK' se o e-mail for válido, ou ' - ERRO' caso contrário. Essa abordagem ajudará a equipe a manter o código limpo e eficiente, além de garantir que os dados dos clientes estejam sempre padronizados.

# Implemente a função principal que leia uma linha contendo o nome completo e o e-mail separados por uma vírgula e um espaço. Utilize funções auxiliares para validar o e-mail e formatar o nome. Não utilize bibliotecas externas.

# Entrada
# Uma única linha contendo o nome completo e o e-mail, separados por uma vírgula e um espaço. O nome pode conter uma ou mais palavras, e o e-mail pode conter letras, números, pontos e o caractere '@'.

# Saída
# Uma única linha com o nome formatado (primeira letra de cada palavra em maiúsculo), seguido de ' - OK' se o e-mail for válido, ou ' - ERRO' caso contrário.


def formatar_nome(nome):
    # Retorna o nome com a primeira letra de cada palavra em maiúsculo
    return ' '.join(
        palavra.capitalize()
        for palavra in nome.strip().split()
    )


def validar_email(email):
    email = email.strip()

    # O e-mail deve conter exatamente um @
    if email.count('@') != 1:
        return False

    # Separa o conteúdo antes e depois do @
    antes_do_arroba, depois_do_arroba = email.split('@')

    # Deve existir pelo menos um ponto depois do @
    return '.' in depois_do_arroba


def processar_cadastro(entrada):
    # Verifica se existe o separador entre nome e e-mail
    if ', ' not in entrada:
        return 'Entrada inválida - ERRO'

    # Divide a entrada apenas na primeira vírgula seguida de espaço
    nome, email = entrada.split(', ', 1)

    nome_formatado = formatar_nome(nome)

    if validar_email(email):
        return f"{nome_formatado} - OK"
    else:
        return f"{nome_formatado} - ERRO"


# Entrada padrão
entrada = input()
print(processar_cadastro(entrada))