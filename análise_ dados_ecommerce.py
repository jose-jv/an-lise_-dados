import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv('ecommerce_estatistica.csv')
print(df.head(20).to_string())


#Gráfico de Histograma Distribuição das Notas dos Produtos
plt.figure(figsize=(8,5))
plt.hist(df['Nota'], bins=10, color='blue', alpha=0.7)
plt.title('Histograma - Distribuição das Notas dos Produtos  ')
plt.xlabel('Nota dos Produtos')
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()


# Gráfico de dispersão Relação entre Número de Avaliações e Nota dos Produtos
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['N_Avaliações'],y=df['Nota'],alpha=0.5, color='red')
plt.title('Dispersão - Relação entre Número de Avaliações e Nota dos Produtos ')
plt.xlabel('Número de Avaliações')
plt.ylabel('Nota dos Produtos')
plt.grid(True)
plt.show()


#Mapa de calor - Correlações
plt.figure(figsize=(8,5))
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Mapa de Calor das Correlações")
plt.show()

#Gráfico de barra - Frequência de descontos oferecidos
plt.figure(figsize=(10,6))
df['Desconto'].value_counts().plot(kind='bar',color='green')
plt.title('Frequência de Descontos Oferecidos')
plt.xlabel('Percentual de Desconto')
plt.ylabel('Número de Produtos')
plt.xticks(rotation=45)
plt.show()




# Gráfico de pizza - Distribuição de Produtos por Marca (Top 10)
marca_counts = df["Marca"].value_counts().nlargest(10)
plt.figure(figsize=(10, 8))
plt.pie(marca_counts, labels=marca_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribuição de Produtos por Marca (Top 10)")
plt.show()


#Gráfico de densidade - baseado na coluna de preços
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True,color='red')
plt.title('Gráfico de Densidade dos Preços dos Produtos')
plt.xlabel('Preço')
plt.ylabel("Densidade")
plt.show()

#grafico de regressão -  Regressão entre Preço e Número de Avaliações 
sns.regplot( x='Preço',y='N_Avaliações',  data=df, color='red', scatter_kws={'alpha': 0.5, 'color': 'blue'})
plt.title('Gráfico de Regressão entre Preço e Número de Avaliações')
plt.xlabel('Preço')
plt.ylabel('Numero de Avaliações')
plt.show()