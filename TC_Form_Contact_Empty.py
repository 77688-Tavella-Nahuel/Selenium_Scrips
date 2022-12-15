from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from colorama import Fore, init, Back

init(autoreset=True)
os.system("cls")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver=webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver.exe", options=options)
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

#Abrir link "Contacto"
click_button = driver.find_element(by=By.LINK_TEXT, value="Contacto")
click_button.click()

contacto = "Déjanos tu mensaje y te responderemos con la mayor brevedad posible."
h3 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div/div/div/div/div/div/div/h3/span").text
if contacto == h3:
    print("Ingreso a la sección 'Contacto': "+Fore.GREEN+"PASS") 
else:
    print("Ingreso a la sección 'Contacto': "+Fore.RED+"FAIL")
    contar_error += 1

time.sleep(2)

#Enviar formulario vacio
click_button_send = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div/div/div/div/div/div[2]/form/p[6]/input")
click_button_send.click()

time.sleep(4)

formulario_vacio = "Uno o más campos tienen un error. Por favor, revísalos e inténtalo de nuevo."
texto = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div/div/div/div/div/div/div/div[2]/form/div[2]").text
if formulario_vacio == texto:
    print("Envío de formulario vacío: "+Fore.GREEN+"PASS") 
else:
    print("Envío de formulario vacío: "+Fore.RED+"FAIL")
    contar_error += 1 

time.sleep(2)

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

if contar_error == 0:
    print(Back.GREEN+"Test: Envío del formulario vacío en el link 'Contacto': PASS")
else:
    print(Back.RED+"Test: Envío del formulario vacío en el link 'Contacto': FAIL")

driver.close()


