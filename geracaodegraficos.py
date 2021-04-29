#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
Análise de Dados com Python
Desafio:
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1w3TmCcQPoc7ew1CXmwwEUpWeHJzJQqGZ?usp=sharing
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset
"""

import pandas as pd
import plotly.express as px

df = pd.read_csv("telecom_users.csv") #variavel df recebe tabela
df = df.drop(["Unnamed: 0"], axis =1) #exclui a coluna; axis = 1 (colunas)
display(df) #mostra df

df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce") #converte para float a coluna que estava como object
df = df.dropna(how="all", axis=1) #remove coluna vazia
df = df.dropna() #remove todas as linhas vazias, valor padrão: how = any; axis = 0 (linhas)
print(df.info()) #visualizar tipo de dado na tabela

display(df["Churn"].value_counts()) #conta quantas vezes cada elemento da coluna aparece ("sim" e "não")
display(df["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #normalize = True transforma os números em valor percentual; .map define casas decimais

for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()
        display(df.pivot_table(index="Churn", columns=coluna, aggfunc="count")["IDCliente"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




