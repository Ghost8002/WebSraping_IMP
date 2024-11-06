import requests
from bs4 import BeautifulSoup
url = 'https://www.globo.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titulos = soup.find_all('h2', class_='post__title')
for titulo in titulos:
    print(titulo.get_text())