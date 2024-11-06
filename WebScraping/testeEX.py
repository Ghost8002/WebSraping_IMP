# Importa a biblioteca requests, que é usada para fazer requisições HTTP
import requests

# Importa a classe BeautifulSoup da biblioteca bs4 para analisar documentos HTML
from bs4 import BeautifulSoup

# Define a URL do site que será acessado
url = 'https://www.globo.com/'

# Envia uma requisição GET para a URL e armazena a resposta
response = requests.get(url)

# Cria um objeto BeautifulSoup com o conteúdo da resposta, usando o parser 'html.parser'
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra todos os elementos <h2> com a classe 'post__title' no HTML analisado
titulos = soup.find_all('h2', class_='post__title')

# Itera sobre os elementos encontrados
for titulo in titulos:
    # Exibe o texto de cada elemento encontrado
    print(titulo.get_text())

