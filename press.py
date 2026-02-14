import time
import pyautogui


pyautogui.moveTo(494, 752)

time.sleep(5)

        # Pressiona o botão esquerdo do mouse
pyautogui.mouseDown(button='left')

        # Aguarda o período de tempo desejado
time.sleep(13)  # O mouse ficará pressionado por 2 segundos

        # Libera o botão esquerdo do mouse
pyautogui.mouseUp(button='left') 