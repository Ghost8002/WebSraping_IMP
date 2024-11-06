import streamlit as st
import requests
from bs4 import BeautifulSoup

def obter_titulos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titulos = soup.find_all('h2', class_='post__title')
    return [titulo.get_text() for titulo in titulos]


st.title("teste do Streamlit")

url = st.text_input("Digite a URL:")

if st.button("Extrair Títulos"):
    if url:
        titulos = obter_titulos(url)
        st.write("Títulos das Notícias:")
        for titulo in titulos:
            st.write(titulo)
    else:
        st.write("Por favor, insira uma URL válida.")