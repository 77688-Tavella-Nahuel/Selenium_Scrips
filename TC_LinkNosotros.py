from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from pynput.mouse import Button, Controller

import time

driver=webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver.exe")
driver.maximize_window()

#Abrir sitio web
driver.get("https://centroestant.com.ar/")

#Abrir link "Nosotros"
click_button = driver.find_element(by=By.LINK_TEXT, value="Nosotros")
click_button.click()
time.sleep(4)

#Reproducir video
mouse=Controller()
driver.execute_script("window.scrollTo(0,600)")
mouse.position = (800,700)
time.sleep(2)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)

#Volver a la home
volver_home = driver.find_element(by=By.XPATH, value="//*[@id='logo']/a")
volver_home.click()

time.sleep(3)
driver.close()