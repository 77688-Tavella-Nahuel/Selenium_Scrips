from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.mouse import Button, Controller
import os
import time
from colorama import Fore, init, Back

init(autoreset=True)
os.system("cls")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver=webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver.exe",options=options)
driver.maximize_window()

contar_error = 0

#Abrir sitio web
driver.get("https://centroestant.com.ar/")
title = driver.title
if "INICIO - CENTRO ESTANT" == title:
    print("Ingreso a página principal: "+Fore.GREEN+"PASS") 
else:
    print("Ingreso a página principal: "+Fore.RED+"FAIL")
    contar_error += 1

#Abrir link "Nosotros"
click_button = driver.find_element(by=By.LINK_TEXT, value="Nosotros")
click_button.click()

nosotros = "Somos una empresa argentina, dedicada a la producción de muebles."
h3 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div/div[1]/div[1]/div[2]/div[2]/div/div/h3/strong").text
if nosotros == h3:
    print("Ingreso a la sección 'Nosotros': "+Fore.GREEN+"PASS") 
else:
    print("Ingreso a la sección 'Nosotros': "+Fore.RED+"FAIL")
    contar_error += 1

time.sleep(4)

#Reproducir video
try:
    reproducir_video = True
    mouse=Controller()
    driver.execute_script("window.scrollTo(0,600)")
    mouse.position = (800,700)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(5)
    print("Reproducción del video: "+Fore.GREEN+"PASS") 
except:
    print("Reproducción del video: "+Fore.RED+"FAIL") 
    reproducir_video = False
    

#Existencia de imagen
imag = "https://s.lamason.us/centroestant.com.ar/media/2022/02/18172951/1_CME120P_FondoBlanco_1000x1000-1024x1024.jpg"
imag2 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div/div[9]/div[2]/div/div[2]/div/img").text

#Volver a la home
volver_home = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[2]/div[1]/div[1]/a/img[1]")
volver_home.click()

title = driver.title
if "INICIO - CENTRO ESTANT" == title:
    print("Regreso a la página principal: "+Fore.GREEN+"PASS") 
else:
    print("Regreso a la página principal: "+Fore.RED+"FAIL")
    contar_error += 1

time.sleep(2)

if contar_error == 0 and reproducir_video == True:
    print(Back.GREEN+"Test: Funcionamiento del video en el link 'Nosotros': PASS")
else:
    print(Back.RED+"Test: Funcionamiento del video en el link 'Nosotros': FAIL")

driver.close()


