from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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


##################
#Las siguientes líneas no deben editarse.
"""
serv = Service(r'/usr/bin/geckodriver', log_path='/dev/null')
options = FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options, service=serv)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)
errors = list()
ex = ''
date = datetime.datetime.now()
log = open(f'add_piece_{date}.log', 'w')
"""

options = webdriver.FirefoxOptions()
service = Service(executable_path="/snap/bin/geckodriver")
driver = webdriver.Firefox(service=service)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)
errors = list()
ex = ''
selection = list()
conv = lambda i : i or ''

try:
    con = sqlite3.connect('/home/antonio/Dropbox/CSIC_IMF_FMT/AMRQ_ASFPardo/AMRQ_ASFPardo20240413.sqlite')
    print(Fore.GREEN + 'CONEXIÓN A LA BASES DE DATOS OK\n')
except:
    print(Fore.RED + 'ERROR al conectar con la base de datos.')
    sys.exit()
    
try:
    cur = con.cursor()
except:
    print(Fore.RED + 'Error al crear el cursor de la base de datos.')

def retrieve_column_tuple(x,y):
    data = cur.execute('SELECT %s FROM "informantes"' %x )
    col_data = data.fetchall()
    comprehension = [item for t in col_data for item in t]
    t = [conv(i) for i in comprehension]
    for i in t:
        i = str(i)
        if bool(re.search('\n', i)) == True:
            e = re.sub('\n','',i)
            y.append(e)
        else:
            y.append(i)


ID = list()
Nombre_FMT = list()

retrieve_column_tuple("ID",ID)
retrieve_column_tuple("Nombre_FMT",Nombre_FMT)


if bool(len(ID) == len(Nombre_FMT)) == True:
    pass
else:
    sys.exit(Fore.RED + f'Revise las variables de tipo lista.\nTodas deben contener el mismo número de elementos')

print(f'Se han obtenido los datos de {len(Nombre_FMT)} informantes con éxito.')

while True:
    inp = input('Escriba el rango de informantes de la tabla INFORMANTES  que desea comprobar\n')
    if inp == 'All':
        ex = range(0, len(Nombre_FMT))
        break
    elif inp.isnumeric() == True:
        ex = int(inp)
        if ex > len(Nombre_FMT):
            print(Fore.RED + 'Parámetros fuera de rango.')
            continue
        else:
            ex = ex -1
            selection.append(ex)
            ex = selection
            break
    elif bool(re.search('^[0-9]+-[0-9]+$', inp)) == True:
        itv = inp.split('-')
        beginning = int(itv[0]) - 1
        end = int(itv[1])
        if end > len(Nombre_FMT):
            print(Fore.RED + 'Parámetros fuera de rango.')
            continue
        else:
            ex = range(beginning, end)
            break
    elif bool(re.search('^exit$', inp)) == True:
        quit()
    
    else:
        print(Fore.RED + 'Error: ' + 'Parámetros erróneos.')


#Recuperación de datos de usuarios de la tabla users_data

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


#submission_author = 'Albert López López'
#submission_author = 'Antonio Pardo-Cayuela'
        
#abriendo navegador
print(Fore.WHITE + 'ACCEDIENDO A FONDO DE MÚSICA TRADICIONAL...')       
driver.get('https://musicatradicional.eu')
driver.find_element(By.CSS_SELECTOR, '#edit-name').send_keys(usr_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-pass').send_keys(psw_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-submit').click()
driver.get('https://musicatradicional.eu/es/informants')
print(Fore.GREEN + f'[ok]' + Fore.RESET + f' Consultando informantes. Espere...')


for i in ex:
    url_ref = ''
    time.sleep(3)

    try:
        # Comprueba si el empleado ya existe en la base de datos remota
        print(Fore.YELLOW + f'[...]' + Fore.RESET +f'Comprobando si el informante {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES) se encuentra ya en el FMT')
        driver.get('https://musicatradicional.eu/informants')
        driver.find_element('xpath', '//*[@id="edit-name"]').clear()
        driver.find_element('xpath', '//*[@id="edit-name"]').send_keys(Nombre_FMT[i])
        driver.find_element('xpath', '//*[@id="edit-submit-list-of-informants"]').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(('xpath', '/html/body/div[1]/div[1]/div[1]/div/section/div/div[2]/div/div/div[3]/table/tbody/tr/td[1]/a'))).click()
        #Guardar URL en URL_FMT
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' El informante {Nombre_FMT[i]}  (registro {i + 1} de INFORMANTES) se encuentra ya en el FMT.\n Se adjunta su URL al campo URL_FMT.')        
        url_fmt = driver.current_url
        cur.execute("UPDATE informantes SET URL_FMT=? WHERE ID =?", (url_fmt, int(ID[i])))
        con.commit()
        time.sleep(3)
    
    except:
        
        print(Fore.RED + f'[x]' + Fore.RESET + f'  El registro {Nombre_FMT[i]}  (registro {i + 1} de INFORMANTES) no existe en FMT.\n El campo URL_FMT de este registro permanece NULL\n No olvide añadir este informante a FMT.')

con.close()

print(Fore.GREEN + 'LA COMPROBACIÓN DE INFORMANTES EN FMT HA TERMINADO.\n COMPRUEBE QUE LOS DATOS SON CORRECTOS.')

driver.close()        