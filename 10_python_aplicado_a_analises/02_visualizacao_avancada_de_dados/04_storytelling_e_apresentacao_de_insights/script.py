sns.boxplot(data=df, x="day", y="tip")

plt.title("Gorjetas ao longo da semana")

plt.show()




sns.boxplot(data=df, x="day", y="tip")

plt.title("Gorjetas ao longo da semana")

plt.show()




import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

fig = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    hover_data=["sex","time"],
    title="Relação entre Conta e Gorjeta"
)

fig.show()





import seaborn as sns
import matplotlib.pyplot as plt

correlacao = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))

sns.heatmap(
    correlacao,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlação entre variáveis")

plt.show()