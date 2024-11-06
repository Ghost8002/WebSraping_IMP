import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para extrair os títulos das notícias
def obter_titulos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titulos = soup.find_all('h2', class_='post__title')
    return [titulo.get_text() for titulo in titulos]

# Título da aplicação
st.title("Extrator de Títulos de Notícias")

# Entrada de texto para a URL
url = st.text_input("Digite a URL do site de notícias")

# Botão para iniciar a extração
if st.button("Extrair Títulos"):
    if url:
        titulos = obter_titulos(url)
        st.write("Títulos das Notícias:")
        for titulo in titulos:
            st.write(titulo)

        # Adiciona a opção de exportar para Excel
        if st.button("Exportar para Excel"):
            df = pd.DataFrame(titulos, columns=['Títulos'])
            df.to_excel('titulos_noticias.xlsx', index=False)
            st.write("Arquivo Excel exportado com sucesso!")
    else:
        st.write("Por favor, insira uma URL válida.")