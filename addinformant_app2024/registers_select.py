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

# Pide al usuario que introduzca el rango de registros que desea subir
rango = input("Introduce el rango de registros que deseas subir (ejemplo: 100-110): ")
inicio, fin = map(int, rango.split('-'))

# Itera sobre cada empleado en el rango especificado en la base de datos local
for row in cur.execute('SELECT Nombre_FMT FROM informantes LIMIT ? OFFSET ?', (fin-inicio+1, inicio-1)):
    nombre = row[0]

