from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


os.system("cls")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver=webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver.exe", options=options)
driver.maximize_window()

#Abrir sitio web
driver.get("https://centroestant.com.ar/")
title = driver.title
assert "INICIO - CENTRO ESTANT" == title, "No coinciden las páginas"

#Abrir link "Contacto"
click_button = driver.find_element(by=By.LINK_TEXT, value="Contacto")
click_button.click()

contacto = "Déjanos tu mensaje y te responderemos con la mayor brevedad posible."
h3 = driver.find_element(by=By.XPATH,value="//*[@id='col-1546266161']/div/h3/span").text
assert contacto == h3, "No se ingreso a la seccion 'Nosotros'"

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
click_button_send = driver.find_element(by=By.XPATH, value="//*[@id='wpcf7-f11-p648-o1']/form/p[6]/input")
click_button_send.click()

time.sleep(8)

formulario_completo = "Gracias por tu mensaje. Ha sido enviado."
texto = driver.find_element(by=By.XPATH,value="//*[@id='wpcf7-f11-p648-o1']/form/div[2]").text
assert formulario_completo == texto, "No se envio el formulario correctamente"

time.sleep(2)

#Volver a la home
volver_home = driver.find_element(by=By.XPATH, value="//*[@id='logo']/a/img[1]")
volver_home.click()

time.sleep(2)
driver.close()

print("Test: Envío del formulario en el link 'Contacto': Pass")
