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
Audiovisuales_i = list()
Audiovisuales_ii = list()
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
retrieve_column_tuple("Audiovisuales_i",Audiovisuales_i)
retrieve_column_tuple("Audiovisuales_ii",Audiovisuales_ii)
retrieve_column_tuple("Video",Video)
retrieve_column_tuple("Autor_entrada",Autor_entrada)


if bool(len(ID) == len(Nombre_FMT) == len(Fecha_grabacion) == len(Ano) == len(Edad) == len(Profesion) == len(Lugar_residencia) == len(Lugar_nacimiento) == len(Observaciones) == len(Misiones_Concursos) == len(Comentarios) == len(Ficha_original) == len(Localidad) == len(Provincia) == len(Comunidad_Autonoma) == len(Sexo) == len(Audiovisuales_i) == len(Audiovisuales_ii) == len(Video) == len(Autor_entrada)) == True:
    pass
else:
    sys.exit(Fore.RED + 'Revise las variables de tipo lista.\nTodas deben contener el mismo número de elementos')

print(f'Se han obtenido los datos de {len(Nombre_FMT)} informantes con éxito.')

while True:
    inp = input('¿Qué le gustaría hacer?\nSi desea subir a FMT todos los informantes que se encuentran en su base de datos escriba "All\nSi desea volver a subir una entrada que ha fallado, escriba su número de identificación por su posición dentro de la lista: p.e., 2.\nSi la conexión se ha interrumpido y desea subir un intervalo de obras, p.e., desde la 1 hasta la 9, introduzca 1-7. Si desea salir, escriba exit:\n')
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
driver.get('https://musicatradicional.eu/node/add/informant')
print(Fore.GREEN + f'[ok]' + Fore.RESET + f' Preparando informantes. Espere...')

#Nombre_FMT

for i in ex:
    url_ref = ''
    time.sleep(3)

    print(Fore.YELLOW + f'============Preparando NUEV0 INFORMANTE para añadir a FMT (registro {i + 1} de INFORMANTES)=============')
   
    try:
        driver.get('https://musicatradicional.eu/node/add/informant')
        nombre = driver.find_element("xpath", '//*[@id="edit-title"]')
        nombre.click()
        nombre.send_keys(Nombre_FMT[i])
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' NOMBRE: añadiendo {Nombre_FMT[i]} a FMT (regsitro {i + 1} de INFORMANTES')
    except:
        print(Fore.RED + '[x]' + f'  NOMBRE: fallo al añadir {Nombre_FMT[i]} a FMT (regsitro {i + 1} de INFORMANTES')
    
    

    '''
    try:
        nombre.send_keys(Nombre_FMT[i])
    except:
        print(Fore.RED + '[x]' + f'  NOMBRE: fallo al añadir {Nombre_FMT[i]} a FMT (regsitro {i + 1} de INFORMANTES')
    '''

    #Fecha de grabación

    #Ano

    #Edad

    #Profesion

    #Lugar_residencia
    try:
        residencia = driver.find_element("xpath", '//*[@id="edit-field-place-of-residence-und-0-value"]')
        residencia.click()
        residencia.send_keys(Lugar_residencia[i])
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' LUGAR de RESIDENCIA: añadiendo {Lugar_residencia[i]} a FMT (regsitro {i + 1} de INFORMANTES')

    except:
        print(Fore.GREEN + '[ok]' + Fore.RESET + f'LUGAR de RESIDENCIA: localidad de residencia del informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')

    
    
    '''
    try:
        residencia.send_keys(Lugar_residencia[i])
    except:
        print(Fore.RED + '[x]' + f'  LUGAR de RESIDENCIA: fallo al añadir {Lugar_residencia[i]} a FMT (regsitro {i + 1} de INFORMANTES')
    '''
    

    #Lugar de nacimiento
    try:
        nacimiento = driver.find_element("xpath", '//*[@id="edit-field-place-of-birth-und-0-value"]')
        nacimiento.click()
        nacimiento.send_keys(Lugar_nacimiento[i])
        print(Fore.GREEN + '[ok]' + Fore.RESET + f'LUGAR NACIMIENTO: localidad de nacimiento del informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)') 
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'LUGAR de NACIMIENTO: fallo al añadir en el informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')

        

    '''
    try:
        nacimiento.send_keys(Lugar_nacimiento[i])
    except:
        print(Fore.RED + '[x]' + f'  LUGAR NACIMIENTO: fallo al añadir {Lugar_nacimiento[i]} a FMT (regsitro {i + 1} de INFORMANTES')
    '''

    #Comentarios

    try:
        comentarios = driver.find_element("xpath", '//*[@id="edit-field-remarks-informant-und-0-value"]')
        comentarios.click()
        comentarios.send_keys(Comentarios[i])
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' COMENTARIOS: añadiendo {Comentarios[i]} a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  COMENTARIOS: fallo al añadirlas a {Nombre_FMT[i]} registro {i + 1} de INFORMANTES)')
        
    

    '''
    try:
        comentarios.send_keys(Comentarios[i])
    except:
        print(Fore.RED + '[x]' + f'  COMENTARIOS: fallo al añadir {Comentarios[i]} a FMT (regsitro {i + 1} de INFORMANTES)')
    '''

    #Ficha original



    #Misiones / Concursos Activar para los informantes extraidos de los cuadernos de Fermín Pardo
    
    
    try:
        driver.find_element("xpath", '/html/body/div[3]/div[2]/div[2]/div/div/form/div/div[9]/div/select/option[182]').click()
        print (Fore.GREEN + '[ok]' + Fore.RESET + f' FUENTE: añadiendo AMRQ_ASFPardo al informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')
        time.sleep(5)

    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  FUENTE: error al añadir AMRQ_ASFPardo al informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')  
        
    
    
        
    #Localidad, provincia, CA    
    loc_1low = Comunidad_Autonoma[i].lower()
    loc_1upp = Comunidad_Autonoma[i].upper()
    loc_2low = Provincia[i].lower()
    loc_2upp = Provincia[i].upper()
    loc_3low = Localidad[i].lower()
    loc_3upp = Localidad[i].upper()
    
    
    try:
        print(Fore.GREEN + '[ok]' + Fore.RESET + f' LOCALIDAD: añadiendo {Localidad[i]} (registro {i + 1} de INFORMANTES)')    
        driver.find_element("xpath", f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-0"]/option[contains(translate(., "{loc_1low}","{loc_1upp}"), "{loc_1upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-1"]/option[contains(translate(., "{loc_2low}","{loc_2upp}"), "{loc_2upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", f'//*[@id="edit-field-location-official-und-hierarchical-select-selects-2"]/option[contains(translate(., "{loc_3low}","{loc_3upp}"), "{loc_3upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-dropbox-add--3"]').click()
        time.sleep(3)
        
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  LOCALIDAD: fallo al añadir {Localidad[i]} (registro {i + 1} de INFORMANTES)')
        time.sleep(3)
    
    #Sexo
    
    if Sexo[i] == 'hombre':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-male-female-und-male"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "hombre" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    elif Sexo[i] == 'mujer':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-male-female-und-female"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "mujer" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    elif Sexo[i] == 'na':       
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-male-female-und-none"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "NA" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f'  SEXO: campo vacío para {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

        pass

    if Sexo[i] == 'hombre':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-man-female-und-7234"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "hombre" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    elif Sexo[i] == 'mujer':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-man-female-und-7235"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "mujer" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    elif Sexo[i] == 'na':       
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="edit-field-man-female-und-none"]'))).click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' SEXO: añadiendo "NA" a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f'  SEXO: campo vacío para {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

        pass        

    #Audiovisuales selección "Audio" y "Cinta"

    audi_1low = Audiovisuales_i[i].lower()
    audi_1upp = Audiovisuales_i[i].upper()
    audii_1low = Audiovisuales_ii[i].lower()
    audii_1upp = Audiovisuales_ii[i].upper()
    
    if Audiovisuales_i[i] == 'Audio' and Audiovisuales_ii[i] == 'cinta':
        driver.find_element('xpath', f'//*[@id="edit-field-audiovisual-und-hierarchical-select-selects-0"]/option[contains(translate(., "{audi_1low}","{audi_1upp}"), "{audi_1upp}")]').click()
        time.sleep(3)
        driver.find_element('xpath', f'//*[@id="edit-field-audiovisual-und-hierarchical-select-selects-1"]/option[contains(translate(., "{audii_1low}","{audii_1upp}"), "{audii_1upp}")]').click()
        time.sleep(3)
        driver.find_element('xpath', '//*[@id="edit-field-audiovisual-und-hierarchical-select-dropbox-add--2"]').click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' AUDIO: añadiendo Audio/Cinta a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f'  AUDIOVISUALES: campos vacíos para {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

        pass               
    
    #Autor de la entrada

    driver.find_element("xpath", '//*[@id="edit-field-editors-und-8651"]').click()
    driver.find_element("xpath", '//*[@id="edit-field-editors-und-5133"]').click()
             
        
    #Guardar entrada 

    guardar = driver.find_element("xpath", '//*[@id="edit-submit"]')       
    guardar.click()
    time.sleep(5)
        
    #Guardar URL en URL_FMT        
    url_fmt = driver.current_url
    cur.execute("UPDATE informantes SET URL_FMT=? WHERE ID =?", (url_fmt, int(ID[i])))
    con.commit()
    time.sleep(8)
    #except:
        #print(Fore.RED + f'Fallo grave.' + Fore.GREEN + f'No se pudo guardar la entrada.\n'
        #+ Fore.RESET + f'Saliendo de informante {Nombre_FMT[i]} con posición Nº {i + 1} y continuando')
        #errors.append(f'{Nombre_FMT[i]} con la posición Nº {i + 1}')
        #continue
        
        
    
con.close()
print(Fore.GREEN + 'LA SUBIDA DE NUEVOS INFORMANTES HA TERMINADO.\n COMPRUEBE QUE LOS DATOS SON CORRECTOS.')
        
if len(errors) == 0:
    print(Fore.GREEN + 'NO SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN.')
    pass
else:
    print(Fore.RED + 'SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN\nDEBE VOLVER A SUBIR LOS SIGUIENTES INFORMANTES.\n')
    for i in errors:
        print(Fore.RED + 'Fallo en' + f' {i}. ' + 'Si desea repetir la subida del informante que ha dado problemas, revise los datos, vuelva a ejecutar el código e introduzca el número ordinario que representa dicho informante en las filas de la base de datos')

driver.close()

