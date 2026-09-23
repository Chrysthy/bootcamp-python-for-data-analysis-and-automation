fig, ax = plt.subplots(2,2, figsize=(12,8))

sns.histplot(df["total_bill"], ax=ax[0,0])
ax[0,0].set_title("Distribuição das contas")

sns.boxplot(data=df, x="day", y="tip", ax=ax[0,1])
ax[0,1].set_title("Gorjetas por dia")

sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax[1,0])
ax[1,0].set_title("Conta vs Gorjeta")

sns.countplot(data=df, x="day", ax=ax[1,1])
ax[1,1].set_title("Quantidade de clientes por dia")

plt.tight_layout()

plt.show()





import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    animation_frame="year",
    title="Evolução de PIB e Expectativa de Vida"
)

fig.show()







fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale="Viridis",
    title="Expectativa de vida no mundo"
)

fig.show()







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
    facet_col="time",
    title="Análise de gorjetas no restaurante"
)

fig.show()








px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="sex",
    size="size",
    animation_frame="day"
)