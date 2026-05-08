# .sorted
linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x))   # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True)   # ["python", "csharp", "java", "js", "c"]


# é usada para ordenar listas (ou outras coleções), mas diferente de .sort(), ela não altera a lista original — em vez disso, retorna uma nova lista ordenada.

# key=lambda x: len(x) → define o critério de ordenação: o tamanho das palavras.
# reverse=True → inverte a ordem, mostrando do maior para o menor.
# sorted() → cria uma nova lista ordenada, mantendo a original intacta.