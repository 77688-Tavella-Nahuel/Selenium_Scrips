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

#Llenar formulario
nombre = driver.find_element(by=By.NAME, value="your-name")
nombre.send_keys("Nahuel")

correo = driver.find_element(by=By.NAME, value="your-email")
correo.send_keys("soynahuel@gmail.com")

motivo = driver.find_elements(by=By.TAG_NAME, value="Option")
motivo[3].click()

asunto = driver.find_element(by=By.NAME, value="your-subject")
asunto.send_keys("quiero devolver")

msj = driver.find_element(by=By.NAME, value="your-message")
msj.send_keys("No funciona")

time.sleep(2)

#Enviar formulario
click_button_send = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div/div/div/div/div/div[2]/form/p[6]/input")
click_button_send.click()

time.sleep(10)

formulario_completo = "Gracias por tu mensaje. Ha sido enviado."
texto = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div/div/div/div/div/div/div/div[2]/form/div[2]").text
if formulario_completo == texto:
    print("Envío de formulario completo: "+Fore.GREEN+"PASS") 
else:
    print("Envío de formulario completo: "+Fore.RED+"FAIL")
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
    print(Back.GREEN+"Test: Envío del formulario completo en el link 'Contacto': PASS")
else:
    print(Back.RED+"Test: Envío del formulario completo en el link 'Contacto': FAIL")

driver.close()


