import pyautogui
import time

# Espera um tempo para dar tempo de você abrir a janela correta
time.sleep(5)

# Tira um screenshot da tela inteira e salva como 'screenshot.png'
screenshot = pyautogui.screenshot('screenshot.png')

# Localiza a posição da imagem do botão na tela
button_location = pyautogui.locateOnScreen('botao.png')

if button_location:
    # Se a imagem for encontrada, obtém o centro do botão e clica nele
    button_point = pyautogui.center(button_location)
    pyautogui.click(button_point)
else:
    print("Botão não encontrado na tela.")