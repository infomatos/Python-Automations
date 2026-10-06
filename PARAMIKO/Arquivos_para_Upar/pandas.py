# Primeiro, instale: pip install pandas
import pandas as pd

# Leitura de um arquivo CSV
df = pd.read_csv('dados.csv') # 'df' é um DataFrame

# Visualizar as primeiras linhas
print(df.head())

# Informações sobre o DataFrame (colunas, tipos de dados, etc.)
print(df.info())

# Acessar uma coluna específica
print(df['Nome'])

# Filtrar dados (ex: pessoas com mais de 25 anos)
df_filtrado = df[df['Idade'] > 25]
print(df_filtrado)

# Salvar o DataFrame modificado em um novo CSV
df_filtrado.to_csv('dados_filtrados.csv', index=False) # index=False para não salvar o índice