import random
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

proxies = [
    "http://proxy.glamourify.shop:824", 
]

def create_driver_with_proxy(proxy):
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')  
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

driver = None

def start_api():
    global driver
    try:
        proxy = random.choice(proxies)
        driver = create_driver_with_proxy(proxy)
        driver.get("https://login.live.com/oauth20_authorize.srf?client_id=10fa57ef-4895-4ab2-872c-8c3613d4f7fb&scope=openid+profile+offline_access&redirect_uri=https%3a%2f%2fwww.microsoft.com%2fcascadeauth%2faccount%2fsignin-oidc&response_type=code&state=CfDJ8NW1sga3NmRPn1ZL4DdSvA78ZnbBYVgZhGVEr3svfTqiqwSWP7W1baWJb6TDCKk0VNLoXRX3sO8u_E4PR5OnBgElPJywqLiAzMmO74qF6B0O-MSgtg7LxFXiz1cecp-QvU8636f2zDJaysZp3wsypX_5uqmf8On1Tx8MNYItpdBvURnL0NjAOhasBrWzqlw7mXg2g8ARwdTjlAahihNqHasYHyfwYt8Tg5PadK7JPjXJy6Q1X7aVhlfRZmVgMsESBFPyIGx3lOZumKjiRGs4Ky2AiMFynfE1o3XvFJznhqSm7EmummrMWFvsa2XJrm8oiTv963c9b1fjc4h5MRqa_oDE-rPP0vYamV87WN5Q4gcD2GKdAFa0An1YP_D-UUXwiXoWBc48XowqH6clFtdauO3OpTAVwx_VtlkffR5HyU-pFCxgLrfF_kNOl_DCKfYTtV0kaw3jVCxZafUXG1WSN8k&response_mode=form_post&nonce=639065645462874385.MTgwZTk5ZjgtNzc4OS00YzIzLTkzY2UtNmIwMGQ3N2Q1NDg2MWQwNjI0ODUtMjg0ZS00MTc3LTkxNmEtZGYyMDA2NDJiZDE5&code_challenge=TNwyzaSLhySjzVjI-KrHfxlAMez-9mCQ5O9b9365ZJk&code_challenge_method=S256&x-client-SKU=ID_NET6_0&x-client-Ver=8.11.0.0&uaid=853b9ee52dd2482eb4983c8c3f700e10&msproxy=1&issuer=mso&tenant=consumers&ui_locales=pt-BR&client_info=1&epctrc=VyTLy1AsC%2bOMrnbRTUQlvgCMa%2btEl%2fet79bF4UmrgCk%3d3%3a1%3aCANARY%3asG0ikWm0YNypZVcdE2EV6pjMxVtg5yKYucEdkO4b01Q%3d&epct=PAQABDgEAAACvnsHKEvvRQb3Bz3Qc7wnaRXZvU3RzQXJ0aWZhY3RzCAAAAAAAl5z74wBkv_JfFuMLmiYTWOddCMwnn3A2LoXWRyhNbsxyxMdNGBumXt5tckvzwz5UF-Gnt07IjkeLV1Omb0M1bVPmP3WfnxS8lQf6TAwyOiICZPCp9pLMvjSRZyWsW1dYa-jnDkFPTsToz1GwPzvbb5ESa0wgYXbwtaihM9xqK7rdp7V8iRkowVr5k0DPXrSiDvF-1RN3kSLRFhRSSSMy2yAA&jshs=0&claims=%7b%22compact%22%3a%7b%22name%22%3a%7b%22essential%22%3atrue%7d%7d%7d#")

        time.sleep(2)

        pyautogui.write('db2a3fae009c7b6554f4')  
        pyautogui.press('tab') 
        pyautogui.write('d09e479878e09ae3')  
        pyautogui.press('enter')

        time.sleep(8)
        
        pyautogui.click(534, 692)

        time.sleep(8)

        pyautogui.write('ucfz15ah2001@hotmail.com')

        pyautogui.click(587, 625)

        time.sleep(3)

        pyautogui.write('ucfz15ah')

        pyautogui.click(531, 690)

        time.sleep(3)

        pyautogui.click(375, 587)

        time.sleep(2)

        pyautogui.click(416, 608)

        time.sleep(2)

        pyautogui.click(446, 613)

        time.sleep(2)

        pyautogui.press('tab')

        pyautogui.press('2')

        time.sleep(2)  

        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.press('tab')

        time.sleep(2)   

        pyautogui.press('j')

        time.sleep(2)

        pyautogui.press('tab')

        pyautogui.write('1998')

        time.sleep(2)  

        pyautogui.press('tab')

        pyautogui.press('tab')

        time.sleep(2)

        pyautogui.press('enter')

        time.sleep(2)   

        pyautogui.write('Pedro')

        pyautogui.press('tab')

        pyautogui.write('Pascal')

        pyautogui.press('tab') 
        pyautogui.press('tab')
        pyautogui.press('tab') 
        pyautogui.press('tab') 
        pyautogui.press('enter') 

        time.sleep(10)

        pyautogui.click(368, 744)
        time.sleep(1)
        pyautogui.click(368, 744)
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.click(495, 752)


        

       
      
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


        pyautogui.moveTo(878, 173, duration=10) 
        pyautogui.click()


def stop_api():
    global driver
    if driver:
        driver.quit()
        messagebox.showinfo("Informação", "Navegador fechado e API desligada.")
    else:
        messagebox.showerror("Erro", "API não foi iniciada ainda.")


root = tk.Tk()
root.title("API Executor")

root.geometry("400x250")


start_button = tk.Button(root, text="Iniciar API", command=start_api, height=2, width=20, bg="green", fg="white")
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Desligar API", command=stop_api, height=2, width=20, bg="red", fg="white")
stop_button.pack(pady=20)

root.mainloop()
