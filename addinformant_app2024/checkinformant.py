from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import time
import sys
import re
from colorama import Fore, Style, init
import sqlite3
import pyautogui
options = webdriver.FirefoxOptions()
service = Service(executable_path="/snap/bin/geckodriver")
driver = webdriver.Firefox(service=service)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)

con = sqlite3.connect('/home/antonio/Dropbox/CSIC_IMF_FMT/AMRQ_ASFPardo/AMRQ_ASFPardo20240413.sqlite')
cur = con.cursor()

'''
# Navega al formulario web y busca al empleado
driver.get('https://www.tu-pagina-web.com/formulario-busqueda')

input_nombre = driver.find_element_by_name('nombre')  # Asegúrate de usar el nombre correcto del campo
input_nombre.clear()
input_nombre.send_keys(nombre)
input_nombre.send_keys(Keys.RETURN)
'''
try:
    # Comprueba si el empleado ya existe en la base de datos remota
    print(f'Comprobando si el informante {Nombre_FMT[i]} se encuentra ya en el FMT')
    driver.get('https://musicatradicional.eu/informants')
    driver.find_element(By.XPATH, '//*[@id="edit-name"]').clear()
    driver.find_element(By.XPATH, '//*[@id="edit-name"]').send_keys(Nombre_FMT)
    driver.find_element(By.XPATH, '//*[@id="edit-submit-list-of-informants"]').click()
    time.sleep(5)
    driver.find_elements('xpath', '/html/body/div[1]/div[1]/div[1]/div/section/div/div[2]/div/div/div[3]/table/tbody/tr')

except NoSuchElementException:
    # Si el empleado no existe, navega al otro formulario y añádelo
    print(f'El registro {Nombre_FMT[i]} no existe en FMT. Se continúa para añadirlo.')
    driver.get('https://musicatradicional.eu/es/node/add/informant')
    #driver.find_element(By.XPATH, '//*[@id="edit-title"]').send_keys(Nombre_FMT[i])