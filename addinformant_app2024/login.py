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


usr = "SELECT user_name FROM users_data WHERE user_nickname = ?"
nickname_parameter = 'Tony'
try:
    cur.execute(usr, (nickname_parameter,))
    usr_result =cur.fetchone()
    usr_value = usr_result[0]

except sqlite3.Error as e:
    print(f"Error al definir el usuario: {e}")


psw = "SELECT user_password FROM users_data WHERE user_nickname = ?"
try:
    cur.execute(psw, (nickname_parameter,))
    psw_result =cur.fetchone()
    psw_value = psw_result[0]

except sqlite3.Error as e:
    print(f"Error al definir la contraseña: {e}")


#abriendo navegador
print(Fore.WHITE + 'ACCEDIENDO A FONDO DE MÚSICA TRADICIONAL...')       
driver.get('https://musicatradicional.eu')
driver.find_element(By.CSS_SELECTOR, '#edit-name').send_keys(usr_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-pass').send_keys(psw_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-submit').click()