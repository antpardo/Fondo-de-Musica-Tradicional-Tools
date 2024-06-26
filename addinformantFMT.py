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
    con = sqlite3.connect('/home/antonio/Dropbox/CSIC_IMF_FMT/AMRQ_ASFPardo/AMRQ_ASFPardo20240406.sqlite')
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
URL_FMT = list()
Fecha_grabacion = list()
Ano = list()
Edad = list()
Profesion = list()
Lugar_residencia = list()
Lugar_nacimiento = list()
Observaciones = list()
Misiones_Concursos = list()
Comentarios = list()
Ficha_original = list()
Localidad = list()
Provincia = list()
Comunidad_Autonoma = list()
Sexo = list()
Audiovisuales = list()
Video = list()
Autor_entrada = list()

retrieve_column_tuple("ID",ID)
retrieve_column_tuple("Nombre_FMT",Nombre_FMT)
retrieve_column_tuple("Fecha_grabacion",Fecha_grabacion)
retrieve_column_tuple("Ano",Ano)
retrieve_column_tuple("Edad",Edad)
retrieve_column_tuple("Profesion",Profesion)
retrieve_column_tuple("Lugar_residencia",Lugar_residencia)
retrieve_column_tuple("Lugar_nacimiento",Lugar_nacimiento)
retrieve_column_tuple("Observaciones",Observaciones)
retrieve_column_tuple("Misiones_Concursos",Misiones_Concursos)
retrieve_column_tuple("Comentarios",Comentarios)
retrieve_column_tuple("Ficha_original",Ficha_original)
retrieve_column_tuple("Localidad",Localidad)
retrieve_column_tuple("Provincia",Provincia)
retrieve_column_tuple("Comunidad_Autonoma",Comunidad_Autonoma)
retrieve_column_tuple("Sexo",Sexo)
retrieve_column_tuple("Audiovisuales",Audiovisuales)
retrieve_column_tuple("Video",Video)
retrieve_column_tuple("Autor_entrada",Autor_entrada)


if bool(len(ID) == len(Nombre_FMT) == len(Fecha_grabacion) == len(Ano) == len(Edad) == len(Profesion) == len(Lugar_residencia) == len(Lugar_nacimiento) == len(Observaciones) == len(Misiones_Concursos) == len(Comentarios) == len(Ficha_original) == len(Localidad) == len(Provincia) == len(Comunidad_Autonoma) == len(Sexo) == len(Audiovisuales) == len(Video) == len(Autor_entrada)) == True:
    pass
else:
    sys.exit(Fore.RED + 'Revise las variables de tipo lista.\nTodas deben contener el mismo número de elementos')

print(f'Se han obtenido los datos de {len(nombre)} informantes con éxito.')

while True:
    inp = input('¿Qué le gustaría hacer?\nSi desea subir a FMT todos los informantes que se encuentran en su base de datos escriba "All\nSi desea volver a subir una entrada que ha fallado, escriba su número de identificación por su posición dentro de la lista: p.e., 2.\nSi la conexión se ha interrumpido y desea subir un intervalo de obras, p.e., desde la 1 hasta la 9, introduzca 1-7. Si desea salir, escriba exit:\n')
    if inp == 'All':
        ex = range(0, len(nombre))
        break
    elif inp.isnumeric() == True:
        ex = int(inp)
        if ex > len(nombre):
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
        if end > len(nombre):
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




submission_author = 'Antonio Pardo-Cayuela'
#submission_author = 'Emilio Ros-Fábregas'
#submission_author = 'Andrea Puentes-Blanco'        
        
#abriendo navegador
        
print(Fore.WHITE + 'ACCEDIENDO A FONDO DE MÚSICA TRADICIONAL...')       
driver.get('https://musicatradicional.eu')
driver.find_element(By.CSS_SELECTOR, '#edit-name').send_keys(usr_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-pass').send_keys(psw_value)
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#edit-submit').click()
print(Fore.WHITE + 'Creando entradas de tipo Add Informant. Espere unos minutos.')

for i in ex:
    url_ref = ''
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, '//*[@id="block-system-navigation"]/div/ul/li[4]/a').click()
    except:
        print(f'Fallo justo antes de añadir el informante {nombre[i]} en la posición Nº {i}')
        
    print(f'AÑADIENDO A FMT EL INFORMANTE {nombre[i]} (Nº {i + 1})')
    
    try:
        driver.find_element(By.XPATH, '//*[@id="edit-title"]').send_keys(nombre[i])
    except:
        print(Fore.RED + 'Fallo al añadir el nombre del informante {nombre[i]} en la posición Nº {i + 1}')

    try:
        driver.find_element(By.XPATH, '//*[@id="edit-field-place-of-birth-und-0-value"]').send_keys(birthplace[i])
    except:
        print(Fore.RED + 'Fallo al añadir la localidad de nacimiento del informante {nombre[i]} en la posición Nº {i + 1}')
        
    loc_1low = region[i].lower()
    loc_1upp = region[i].upper()
    loc_2low = provincia[i].lower()
    loc_2upp = provincia[i].upper()
    loc_3low = localidad[i].lower()
    loc_3upp = localidad[i].upper()
    
    try:    
        driver.find_element(By.XPATH, f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-0"]/option[contains(translate(., "{loc_1low}","{loc_1upp}"), "{loc_1upp}")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-1"]/option[contains(translate(., "{loc_2low}","{loc_2upp}"), "{loc_2upp}")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-2"]/option[contains(translate(., "{loc_3low}","{loc_3upp}"), "{loc_3upp}")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="edit-field-location-official-und-hierarchical-select-dropbox-add--3"]').click()
        time.sleep(5)
        
    except:
        print(Fore.RED + 'FALLO GRAVE:' + Fore.GREEN + f'''Los parámetros de location están vacíos o mal escritos. Debe revisarlos.\n
        Saliendo de informante {nombre[i]} con posición Nº {i + 1} y continuando''')
        errors.append(f'{nombre[i]} con posición Nº {i + 1}')
        driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div[1]/ul/li[1]/a').click()
        time.sleep(3)
        continue

    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/section/div/div/div/form/div/div[16]/div/div/div[1]/div/select[1]/option[2]').click()
    except:
        print(Fore.RED + 'Pestaña de Audiovisuales/Audio ha fallado en la pieza {title[i]} con la ID  {ids[i]}')
        errors.append(f'{title[i]} con la posición Nº {I + 1}')
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/section/div/div/div/form/div/div[16]/div/div/div[1]/div/select[2]/option[13]').click()
        driver.find_element(By.XPATH, '//*[@id="edit-field-audiovisual-und-hierarchical-select-dropbox-add--2"]').click()
    except:
        print(f'Pestaña de Audiovisuales/Wikimedia ha fallado en la pieza {title[i]} con la ID  {ids[i]}')
        errors.append(f'{title[i]} con la posición Nº {I + 1}')
        continue

    if submission_author != '':
        
        #Antonio
        try:                
            driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div/section/div/div/div/form/div/div[17]/div/div/div[41]/label[contains(text(), "{submission_author}")]').click()
          
        #Emilio
        #try:                
        #    driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div/section/div/div/div/form/div/div[17]/div/div/div[1]/label[contains(text(), "{submission_author}")]').click()
        #except:             
        #    pass

        #Andrea
        
        #try:                
         #   driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div/section/div/div/div/form/div/#div[17]/div/div/div[46]/label[contains(text(), "{submission_author}")]').click()
        except:             
            pass

    else:
        print(Fore.RED + 'Fallo grave.' + Fore.RED + f'''Los parámetros de submission author están mal escritos. Debe revisarlos.\n
        Saliendo de informante {nombre[i]} con posición Nº {i + 1} y continuando''')
        errors.append(f).click()
        driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div[1]/ul/li[1]/a').click()
        time.sleep(3)
        continue
    
    #time.sleep(5)
    #driver.find_element(By.XPATH, '//*[@id="edit-submit"]').click()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-submit"]'))).click()
        time.sleep(5)
        url_ref = driver.current_url
        cur.execute(f'UPDATE informantes SET URL_FMT=? WHERE ID =?', (url_ref, int(id_sql[i])))
        con.commit()
        time.sleep(5)
    except:
        print(Fore.RED + 'Fallo grave.' + Fore.GREEN + f'''No se pudo guardar la entrada.\n
        Saliendo de informante {nombre[i]} con posición Nº {i + 1} y continuando''')
        errors.append(f'{title[i]} con la posición Nº {I + 1}')
        continue
        
        
    
con.close()
print(Fore.RED + 'La ejecución ha terminado. Revise los resultados a continuación en busca de posibles errores.\n')
        
if len(errors) == 0:
    print(Fore.GREEN + 'NO SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN.')
    pass
else:
    print(Fore.RED + 'SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN\nDEBE VOLVER A SUBIR LOS SIGUIENTES INFORMANTES.\n')
    for i in errors:
        print(Fore.RED + 'Fallo en' + f' {i}. ' + 'Si desea repetir la subida del informante que ha dado problemas, revise los datos, vuelva a ejecutar el código e introduzca el número ordinario que representa dicho informante en las filas de la base de datos')

driver.close()

