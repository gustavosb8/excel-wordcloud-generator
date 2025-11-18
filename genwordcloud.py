#Use este comando para instalar as bibliotecas necessárias
#pip install pandas wordcloud matplotlib nltk openpyxl

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re

# Baixar stopwords (apenas uma vez)
nltk.download('stopwords')

# Definindo stopwords em português
stopwords_pt = set(stopwords.words('portuguese'))

#adicionar novas palavras ao stopwords
novas_stopwords = {"evidenciado", "inspeção", "atividade", "identificado", "durante", "realizando", "atividades","uso", "devido"}

# Adicionar ao conjunto existente
stopwords_pt.update(novas_stopwords)

# Caminho do arquivo Excel
arquivo_excel = "data.xlsx"  # Nome do arquivo Excel

# Lendo o arquivo Excel
df = pd.read_excel(arquivo_excel)

# Verificando se a coluna 'Descrição' existe
if 'Descrição' not in df.columns:
    raise ValueError("A coluna 'Descrição' não foi encontrada no arquivo Excel.")

# Concatenando todas as descrições em uma única string
texto = " ".join(df['Descrição'].dropna().astype(str))

# Limpeza do texto: remover caracteres especiais e números
texto_limpo = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', texto.lower())

# Remover stopwords
palavras_filtradas = [palavra for palavra in texto_limpo.split() if palavra not in stopwords_pt]
texto_final = " ".join(palavras_filtradas)

# Gerando a WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_final)

# Exibindo a WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()