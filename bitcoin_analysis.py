import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurações gráficas
plt.style.use('ggplot')
sns.set_palette("Set2")

# Carregar o conjunto de dados
# https://finance.yahoo.com/quote/BTC-USD/history
df = pd.read_csv("data/bitcoin.csv")
   
# Visualizar primeiras linhas
print("Prévia dos dados:")
print(df.head())

# Converter a coluna de data
df['Date'] = pd.to_datetime(df['Date'])

# Ordenar por data
df = df.sort_values('Date')

# Informações gerais
print("\nInformações gerais:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# ----------------------------------------------
# Visualizações
# ----------------------------------------------

# 1. Evolução do preço de fechamento
plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Close'], label='Preço de Fechamento', color='blue')
plt.title("Evolução do Preço do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Preço em USD")
plt.legend()
plt.show()

# 2. Volume negociado ao longo do tempo
plt.figure(figsize=(12,5))
plt.bar(df['Date'], df['Volume'], color='orange')
plt.title("Volume de Negociação do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Volume")
plt.show()

# 3. Correlação entre variáveis
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Matriz de Correlação")
plt.show()

# ----------------------------------------------
# Análise de Retornos Diários
# ----------------------------------------------
df['Return'] = df['Close'].pct_change()
plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Return'], color='purple', alpha=0.6)
plt.title("Retornos Diários do Bitcoin")
plt.xlabel("Ano")
plt.ylabel("Variação Percentual")
plt.show()

# Estatísticas dos retornos
print("\nEstatísticas dos retornos diários:")
print(df['Return'].describe())

# ----------------------------------------------
# Tendência Móvel (Médias)
# ----------------------------------------------
df['MA_7'] = df['Close'].rolling(window=7).mean()
df['MA_30'] = df['Close'].rolling(window=30).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Preço Fechamento', alpha=0.7)
plt.plot(df['Date'], df['MA_7'], label='Média 7 dias')
plt.plot(df['Date'], df['MA_30'], label='Média 30 dias')
plt.title("Preço do Bitcoin com Médias Móveis")
plt.xlabel("Ano")
plt.ylabel("Preço (USD)")
plt.legend()
plt.show()
