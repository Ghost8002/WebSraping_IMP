import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Função para ler os NCMs do arquivo Excel
def ler_arquivo_excel(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    return df['NCM'].tolist()

# Caminho do arquivo Excel
caminho_arquivo = 'teestesNCM.xlsx'

# Ler os NCMs do arquivo Excel
ncms = ler_arquivo_excel(caminho_arquivo)

# Configurar o WebDriver (ajuste o caminho para o seu WebDriver)
driver = webdriver.Chrome() #executable_path='/path/to/chromedriver'

# Navegar para o site da Econet
driver.get('https://www.econeteditora.com.br')

# Exemplos de passos para encontrar a aba Federal e depois PIS/COFINS podem variar, então adaptaremos
# Navegar até a aba Federal (assumindo que isso é feito através de um link ou botão)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/ul[1]/li[13]/a').click()

# Aguardar a página carregar
time.sleep(2)

# # Navegar até a aba PIS/COFINS
# driver.find_element(By.LINK_TEXT, "PIS/COFINS").click()

# # Aguardar a página carregar
# time.sleep(2)

for ncm in ncms:
    # Encontre o campo de entrada onde o NCM deve ser colado
    campo_ncm = driver.find_element(By.ID, 'id_do_campo_ncm')  # Ajuste 'id_do_campo_ncm' conforme necessário
    campo_ncm.clear()
    campo_ncm.send_keys(ncm)
    campo_ncm.send_keys(Keys.RETURN)

    # Aguardar a página carregar os resultados
    time.sleep(2)

    # Verificar se o NCM é monofásico ou não (ajuste os seletores conforme necessário)
    resultado = driver.find_element(By.ID, 'id_do_resultado').text
    print(f"NCM {ncm} é monofásico: {resultado}")

# Fechar o navegador
driver.quit()