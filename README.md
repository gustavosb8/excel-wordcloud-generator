# Excel WordCloud Generator

Este projeto gera uma **WordCloud (nuvem de palavras)** a partir de descrições contidas em um arquivo Excel. Ele é útil para análise textual, destacando as palavras mais frequentes após a remoção de stopwords.

---

## 📌 Funcionalidades
- Leitura de dados de um arquivo Excel.
- Limpeza do texto (remoção de caracteres especiais e números).
- Remoção de stopwords em português (incluindo stopwords customizadas).
- Geração e exibição de uma nuvem de palavras.

---

## 🛠️ Pré-requisitos
Antes de executar o código, instale as bibliotecas necessárias:

```bash
pip install pandas wordcloud matplotlib nltk openpyxl

🚀 Como usar

Coloque seu arquivo Excel na pasta do projeto com o nome data.xlsx.

Certifique-se de que ele contém uma coluna chamada Descrição.

Execute o script Python

📂 Estrutura do Projeto
excel-wordcloud-generator/
│
├── main.py          # Código principal
├── data.xlsx        # Arquivo Excel com os dados (não incluído no repositório)
└── README.md        # Documentação do projeto

⚙️ Personalização

Stopwords adicionais: Você pode adicionar novas palavras irrelevantes ao conjunto novas_stopwords no código.
Configuração da WordCloud: Ajuste parâmetros como width, height e background_color para personalizar a visualização.

✅ Exemplo de Saída

<img width="1000" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/f66a04f4-0728-4a1b-b44b-26d076ef010f" />


