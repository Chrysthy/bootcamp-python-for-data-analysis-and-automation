import matplotlib.pyplot as plt

plt.scatter(df["total_bill"], df["tip"])

plt.xlabel("Conta total")
plt.ylabel("Gorjeta")

plt.title("Relação entre conta e gorjeta")

plt.show()




import seaborn as sns

sns.scatterplot(data=df, x="total_bill", y="tip")

plt.show()




import plotly.express as px

fig = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="day",
    title="Conta vs Gorjeta"
)

fig.show()