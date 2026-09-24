# Detecção de fraudes em transações

import pandas as pd

url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

df = pd.read_csv(url)

df.head()


# Problema de Classificação Desbalanceada
# Fraudes são raras -> modelo pode ignorar a classe 1

df["Class"].value_counts(normalize=True)


# Feature Engineering
# Criamos variáveis que ajudam o modelo.


import numpy as np

df["Amount_log"] = np.log1p(df['Amount'])


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df["Amount_scaled"] = scaler.fit_transform(df[["Amount"]])


from re import X
from sklearn.model_selection import train_test_split

x = df.drop("Class", axis=1)
y = df["Class"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, stratify=y, test_size=0.3, random_state=42
)



