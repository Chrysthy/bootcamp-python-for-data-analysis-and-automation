# copy

contatos = {
    "chrystine@gmail.com": {"nome": "Chrystine", "telefone": "3333-2221"},
}

copia = contatos.copy()
copia['chrystine@gmail.com'] = {"nome": "Chrys"}

contatos["chrystine@gmail.com"]
# {"nome": "Chrystine", "telefone": "3333-2221"}

copia['chrystine@gmail.com']
# {"nome": "Chrys"}


# cria uma cópia rasa (shallow copy) do dicionário.

# Isso significa que o novo dicionário é independente do original, mas se houver objetos mutáveis dentro (como listas ou outros dicionários), eles ainda são 
# referenciados e não duplicados profundamente.



contatos = {
    "chrystine@gmail.com": {"nome": "Chrystine", "telefones": ["3333-2221", "9999-8888"]},
}

copia = contatos.copy()

# Alterando a lista dentro da cópia
copia["chrystine@gmail.com"]["telefones"].append("1111-2222")

contatos["chrystine@gmail.com"]["telefones"]
# ["3333-2221", "9999-8888", "1111-2222"]

copia["chrystine@gmail.com"]["telefones"]
# ["3333-2221", "9999-8888", "1111-2222"]


# Perceba que tanto o original quanto a cópia foram modificados.
# Isso acontece porque .copy() só copia o primeiro nível do dicionário. Os objetos internos (listas, outros dicionários) continuam sendo referências compartilhadas.