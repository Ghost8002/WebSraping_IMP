from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get('https://sistemas1.sefaz.ma.gov.br/portalsefaz/jsp/principal/principal.jsf')
navegador.find_element(By.XPATH,'//*[@id="mosaic"]/a[2]/div/h3').click()
navegador.find_element(By.XPATH,'//*[@id="servicos"]/ul/li[10]/a/div/h3').click()

time.sleep(60)