# vendas de e-commerce
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

df.head()



# Processamento automático dos dados
total_gorjetas = df["tip"].sum()

print("Total de gorjetas:", total_gorjetas)


gorjetas_por_dia = df.groupby("day")["tip"].sum()

print(gorjetas_por_dia)



# Criando um pipeline automatizado
def pipeline_restaurante():

    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

    df = pd.read_csv(url)

    total_gorjetas = df["tip"].sum()

    relatorio = pd.DataFrame({
        "total_gorjetas":[total_gorjetas]
    })

    relatorio.to_csv("relatorio_gorjetas.csv", index=False)

    print("Pipeline executado com sucesso")
    print("Total de gorjetas:", total_gorjetas)

pipeline_restaurante()