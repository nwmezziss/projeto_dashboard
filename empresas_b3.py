import pandas as pd

df = pd.read_excel("AXIA3_evolucao.xlsx")
#Selecionando a coluna "valor" e aplicando funções
df["valor"].max()
df["valor"].min()
df["valor"].mean()
df["valor"].std()
#Selecionar linhas
df[0:1]
#selecionar linhas e colunas
colunas = ["conta", "valor"]
df[23:24][colunas]
#filtrar linhas atraves valor
linhas = df["trimestre"] == '20262T'
colunas = ["conta","valor"]
df[linhas][colunas]
#linha
linhas = df ["conta"] == "lucro"
colunas = ["valor"]
df[linhas][colunas].mean()
#Graficos
import seaborn as sns
import matplotlib.pyplot as plt
#Graficos do lucro
linhas = df["conta"] == "lucro"
colunas = ["trimestre", "valor"]
dados = df[linhas][colunas]
sns.lineplot(dados)
plt.title("Gráfico de lucro")
plt.xticks(rotation=45)