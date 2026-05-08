# .sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"] - Ordena em ordem alfabética crescente.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] - Ordena em ordem alfabética inversa.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"] - Ordena pelo tamanho das palavras (do menor para o maior).

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"] - Ordena pelo tamanho das palavras, mas do maior para o menor.


# é usado para ordenar listas de forma flexível e poderosa. Ele modifica a lista original (não cria uma nova) e pode ordenar tanto alfabeticamente quanto por 
# critérios personalizados.

# Se você quiser ordenar sem alterar a lista original, use sorted():

nova_lista = sorted(linguagens)

# O parâmetro key do .sort() (ou sorted()) permite definir uma função de transformação que será aplicada a cada elemento da lista antes da comparação.
# Em vez de comparar diretamente os elementos, o Python compara o resultado da função aplicada a eles.

# lambda cria uma função anônima (sem nome).
# x representa cada elemento da lista.

# len(x) retorna o tamanho (número de caracteres) da string x.
# Ordene a lista usando o comprimento das palavras como critério.