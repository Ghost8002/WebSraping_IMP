import requests  # Importa a biblioteca requests, que é usada para fazer requisições HTTP
from bs4 import BeautifulSoup  # Importa a classe BeautifulSoup da biblioteca bs4 para analisar documentos HTML
import pandas as pd  # Importa a biblioteca pandas, que será usada para manipulação de dados e criação do arquivo Excel

def obter_titulos(url):  # Função para extrair os títulos das notícias
    response = requests.get(url)  # Envia uma requisição GET para a URL e armazena a resposta
    soup = BeautifulSoup(response.content, 'html.parser')  # Cria um objeto BeautifulSoup com o conteúdo da resposta, usando o parser 'html.parser'
    titulos = soup.find_all('h2', class_='post__title')  # Encontra todos os elementos <h2> com a classe 'post__title' no HTML analisado
    return [titulo.get_text() for titulo in titulos]  # Retorna uma lista com o texto de cada título encontrado

st.title("Extrator de Títulos de Notícias")  # Título da aplicação Streamlit

url = st.text_input("Digite a URL do site de notícias")  # Entrada de texto para a URL

if st.button("Extrair Títulos"):  # Botão para iniciar a extração
    if url:  # Verifica se a URL não está vazia
        titulos = obter_titulos(url)  # Chama a função para obter os títulos das notícias
        st.write("Títulos das Notícias:")  # Exibe a mensagem de cabeçalho
        for titulo in titulos:  # Itera sobre os títulos e exibe cada um deles
            st.write(titulo)  # Exibe o título da notícia
        if st.button("Exportar para Excel"):  # Adiciona a opção de exportar para Excel
            df = pd.DataFrame(titulos, columns=['Títulos'])  # Cria um DataFrame pandas com os títulos
            df.to_excel('titulos_noticias.xlsx', index=False)  # Exporta o DataFrame para um arquivo Excel
            st.write("Arquivo Excel exportado com sucesso!")  # Exibe uma mensagem de sucesso
    else:
        st.write("Por favor, insira uma URL válida.")  # Exibe uma mensagem de erro se a URL estiver vazia
