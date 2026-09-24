# 💳 Detecção de Fraudes com Python

Projeto de Machine Learning para identificar possíveis fraudes em transações financeiras.

O principal desafio deste problema é o **desbalanceamento dos dados**, já que existem muito mais transações normais do que fraudulentas. Por isso, além da acurácia, foram analisadas métricas como **Precision, Recall e F1-score**, principalmente para a classe de fraude.

## 🔎 O que foi feito

Durante o projeto foram realizadas etapas de:

* Preparação e transformação dos dados
* Análise do desbalanceamento das classes
* Teste de diferentes modelos de classificação
* Comparação utilizando Precision, Recall e F1-score
* Ajuste do limiar de decisão (*threshold*)
* Análise das variáveis com SHAP

Também foram exploradas técnicas como SMOTE, balanceamento de classes e XGBoost.

## 🤖 Modelos

Foram testados modelos como:

* Logistic Regression
* Random Forest
* XGBoost

O foco da avaliação foi principalmente o **Recall da classe de fraude**, pois nesse tipo de problema é importante reduzir a quantidade de fraudes que não são detectadas.

## 🎯 Threshold

Além do limiar padrão de classificação, foi testado um **threshold de 0.30** para observar o impacto na identificação das fraudes.

A alteração aumentou o Recall, mostrando o trade-off entre **Precision e Recall**.

## 🧠 SHAP

O SHAP foi utilizado para entender quais variáveis tiveram maior influência nas previsões realizadas pelo modelo.

Entre as features com maior impacto apareceram variáveis como **V4 e V14**.

## 🔄 Alterações realizadas

O projeto original foi adaptado para execução em um arquivo Python `.py`, mantendo as principais etapas da análise e organizando o código para publicação no GitHub.

## 🛠️ Tecnologias

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* XGBoost
* SHAP
* Matplotlib

## 📁 Arquivos

```text
deteccao-fraudes-python/
│
├── script.py
└── README.md
```

