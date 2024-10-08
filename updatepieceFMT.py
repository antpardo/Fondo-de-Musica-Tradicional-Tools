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
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import os
import time
import sys
import re
from colorama import Fore, Style, init
import sqlite3


# Inicializar colorama
init(autoreset=True)

# Obtener la fecha y hora actual
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

# Crear el nombre del archivo con la fecha y hora
file_name = f"addpieceFMT_{timestamp}.log"

# Crear y abrir el archivo de registro con la codificación UTF-8
log_file = open(file_name, 'w', encoding='utf-8')
#log_file = open(file_name, 'w',)

# Redirigir la salida estándar al archivo de registro y también a la consola
class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, text):
        # Remover códigos de escape ANSI antes de escribir en el archivo
        #text_without_ansi = ''.join(char for char in text if 0 < ord(char) < 127)
        for f in self.files:
            f.write(text)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

# Redirigir la salida estándar
tee = Tee(sys.stdout, log_file)

# Desactivar colores al escribir en el archivo
sys.stdout = tee
sys.stdout.isatty = lambda: False

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
    print(Fore.GREEN + f'[ok]' + Fore.RESET + f' Conexión con tabla REPERTORIO\n')
except:
    print(Fore.RED + f'[x]' + Fore.RESET + f' FALLO de conexión con la tabla REPEROTRIO')
    sys.exit()
    
try:
    cursor = con.cursor()
except:
    print(Fore.RED + f'[x]' + Fore.RESET + f'FALLO en cursor')

def retrieve_column_tuple(x,y):
    data = cursor.execute('SELECT %s FROM "repertorio"' %x )
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

submission_author = 'Albert López López'

ID = list()
URL_FMT = list()     
ID_pieza = list()
Titulo = list()
Incipit_txt = list()   
Nota_inicial = list()
Incipit_mus = list()  
Tipo_pieza = list()
Genero01 = list()      
Genero02 = list()
Genero03 = list()         
ID_inf01 = list()
Informante01 = list()
ID_inf02 = list()
Informante02 = list()
Comunidad_Autonoma = list() 
Provincia = list()    
Localidad = list()     
Pais = list()
Fuente = list()     
ID_inv01 = list()
Investigador01 = list()
ID_inv02 = list()
Investigador02 = list()
Institucion_colaboradora = list()  
Personas_colaboradoras = list()    
Instrumentos_musicales = list()    
Texto_poesia = list()  
Observaciones = list()
Imagen = list()        
Audio = list()         
Transcripcion_XML = list()
Transcripcion_Kern = list()    
LYincipit = list()    
Idioma = list()        
Audiovisuales = list() 
Video_FMT = list()     
Autor_entrada = list() 

retrieve_column_tuple("ID",ID)  
retrieve_column_tuple("URL_FMT", URL_FMT)       
retrieve_column_tuple("ID_pieza",ID_pieza)  
retrieve_column_tuple("Titulo",Titulo)  
retrieve_column_tuple("Incipit_txt",Incipit_txt)     
retrieve_column_tuple("Nota_inicial",Nota_inicial)  
retrieve_column_tuple("Incipit_mus",Incipit_mus)    
retrieve_column_tuple("Tipo_pieza",Tipo_pieza)  
retrieve_column_tuple("Genero01",Genero01)        
retrieve_column_tuple("Genero02",Genero02)
retrieve_column_tuple("Genero02",Genero03)          
retrieve_column_tuple("ID_inf01",ID_inf01)  
retrieve_column_tuple("Informante01",Informante01)  
retrieve_column_tuple("ID_inf02",ID_inf02)  
retrieve_column_tuple("Informante02",Informante02)  
retrieve_column_tuple("Comunidad_Autonoma",Comunidad_Autonoma)   
retrieve_column_tuple("Provincia",Provincia)      
retrieve_column_tuple("Localidad",Localidad)       
retrieve_column_tuple("Pais",Pais)  
retrieve_column_tuple("Fuente",Fuente)       
retrieve_column_tuple("ID_inv01",ID_inv01)
retrieve_column_tuple("Investigador01",Investigador01)
retrieve_column_tuple("ID_inv02",ID_inv02)
retrieve_column_tuple("Investigador02",Investigador02)
retrieve_column_tuple("Institucion_colaboradora",Institucion_colaboradora)
retrieve_column_tuple("Personas_colaboradoras",Personas_colaboradoras)
retrieve_column_tuple("Instrumentos_musicales",Instrumentos_musicales)
retrieve_column_tuple("Texto_poesia",Texto_poesia)
retrieve_column_tuple("Observaciones",Observaciones)
retrieve_column_tuple("Imagen",Imagen)
retrieve_column_tuple("Audio",Audio)
retrieve_column_tuple("Transcripcion_XML",Transcripcion_XML)
retrieve_column_tuple("Transcripcion_Kern",Transcripcion_Kern)
retrieve_column_tuple("LYincipit",LYincipit)
retrieve_column_tuple("Idioma",Idioma)
retrieve_column_tuple("Audiovisuales",Audiovisuales)
retrieve_column_tuple("Video_FMT",Video_FMT)
retrieve_column_tuple("Autor_entrada",Autor_entrada)

if bool(len(ID) == len(URL_FMT) == len(ID_pieza) == len(Titulo) == len(Incipit_txt) == len(Nota_inicial) == len(Incipit_mus) == len(Tipo_pieza) == len(Genero01) == len(Genero02) == len(Genero03) == len(ID_inf01) == len(Informante01) == len(ID_inf02) == len(Informante02) == len(Comunidad_Autonoma) == len(Provincia) == len(Localidad) == len(Pais) == len(Fuente) == len(ID_inv01) ==  len(Investigador01) == len(ID_inv02) == len(Investigador02) == len(Institucion_colaboradora) == len(Personas_colaboradoras) == len(Instrumentos_musicales) == len(Texto_poesia) == len(Observaciones) == len(Imagen) == len(Audio) == len(Transcripcion_XML) == len(Transcripcion_Kern) == len(LYincipit) == len(Idioma) == len(Audiovisuales) == len(Video_FMT) == len(Autor_entrada)) == True:
    pass
else:
    sys.exit(Fore.RED + 'Revise las variables de tipo lista.\nTodas deben contener el mismo número de elementos')

print(f'Se han obtenido los datos de {len(Titulo)} piezas con éxito.')


while True:
    inp = input('¿Qué le gustaría hacer?\n1. Actualizar en FMT todas las piezas de la DB (escriba "All").\n2. Actualizar sólo una entrada (escriba el nº ABSOLUTO que le asigna la DB).\n3. Actualizar un intervalo de obras (escriba los nos. ABSOLUTOS asignados por la DB que definen el intervalo, separados por un guion (p. ej. 147-230).\n4. Salir ("exit").\n')
    if inp == 'All':
        ex = range(0, len(Titulo))
        break
    elif inp.isnumeric() == True:
        ex = int(inp)
        if ex > len(Titulo):
            print(Fore.RED + 'Parámetros fuera de rango.')
            continue
        else:
            ex = ex -1
            selection.append(ex)
            ex = selection
            break
    elif bool(re.search('^[0-9]+-[0-9]+$', inp)) == True:
        itv = inp.split('-')
        beginning = int(itv[0]) -1
        end = int(itv[1])
        if end > len(Comunidad_Autonoma):
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
    cursor.execute(usr, (nickname_parameter,))
    usr_result =cursor.fetchone()
    usr_value = usr_result[0]

except sqlite3.Error as e:
    print(f"Error al definir el usuario: {e}")


psw = "SELECT user_password FROM users_data WHERE user_nickname = ?"
try:
    cursor.execute(psw, (nickname_parameter,))
    psw_result =cursor.fetchone()
    psw_value = psw_result[0]

except sqlite3.Error as e:
    print(f"Error al definir la contraseña: {e}")        
        
#Abriendo Firefox y login en BHP
        
print(Fore.WHITE + 'Accediendo a FMT...')       
driver.get('https://www.musicatradicional.eu')
driver.find_element("xpath", '//*[@id="edit-name"]').send_keys(usr_value)
driver.implicitly_wait(3)
driver.find_element("xpath", '//*[@id="edit-pass"]').send_keys(psw_value)
driver.implicitly_wait(3)
driver.find_element("xpath", '//*[@id="edit-submit"]').click()
#driver.get('https://musicatradicional.eu/es/node/add/piece')
#print(Fore.GREEN + f'[ok]' + Fore.RESET + f' Añadiendo piezas. Espere...')

for i in ex:
    url_ref = ''
    #time.sleep(3)
    driver.get(URL_FMT[i])
    driver.implicitly_wait(3)
    driver.find_element("xpath", '/html/body/div[1]/div[1]/div[1]/div/section/div[2]/ul/li[2]/a').click()


    print(Fore.YELLOW + f'============Preparando la ACTUALIZACIÓN de la PIEZA en FMT (registro {i + 1} de REPERTORIO)============')

##Título (año)
    
    try:
        titulo = driver.find_element("xpath", '//*[@id="edit-title"]')
        titulo.clear()
        titulo.click()
    except:
        print(Fore.RED + '[x]' + f'  TITULO: fallo al actualizar {Titulo[i]} a FMT (regsitro {i + 1} de REPERTORIO')
        
    print(Fore.GREEN + f'[ok]' + Fore.RESET + f' TITULO: actualizando {Titulo[i]} a FMT (regsitro {i + 1} de REPERTORIO')
    
    try:
        titulo.send_keys(Titulo[i])
    except:
        print(Fore.RED + '[x]' + f'  TITULO: fallo al actualizar {Titulo[i]} a FMT (regsitro {i + 1} de REPERTORIO')
        
##Íncipit de texto
           
    try:
        incipit_txt = driver.find_element("xpath", '//*[@id="edit-field-text-incipit-und-0-value"]')
        incipit_txt.clear()
        incipit_txt.click()
        
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  INCIPIT TXT: fallo al actualizarlo en  {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        
    print(Fore.GREEN + '[ok]' + Fore.RESET + f' INCIPIT TXT: actualizado en {Titulo[i]} (registro {i + 1} de REPERTORIO)')
    
    try:
        incipit_txt.send_keys(Incipit_txt[i])
    except:
        print(Fore.RED + '[x]' + f'  INCIPIT_TXT: fallo al actualizarlo en {Titulo[i]} a FMT (regsitro {i + 1} de REPERTORIO')
    

##Íncipit musical

    try:
        incipit_mus = driver.find_element("xpath", '//*[@id="edit-field-melody-und-0-value"]')
        incipit_mus.clear()
        incipit_mus.click()
    except:
        print(Fore.RED + '[x]' + f'  INCIPIT MUSICAL: fallo al añdir {Incipit_mus[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        
    print(Fore.GREEN + '[ok]' + Fore.RESET + f' INCIPIT MUSICAL: actualizando {Incipit_mus[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
    
    try:
        incipit_mus.send_keys(Incipit_mus[i])
    except:
        print(Fore.RED + '[x]' + f'INCIPIT MUSICAL: fallo al actualizar {Incipit_mus[i]} a {Titulo[i]} ({i + 1} de REPERTORIO')  

##Tipo de pieza (vocal o instrumental)
    
    pieza_vocal = driver.find_element("xpath", '//*[@id="edit-field-piece-type-und-vocal"]')
    if pieza_vocal.is_selected():
       pieza_vocal.click() 

    pieza_inst = driver.find_element("xpath", '//*[@id="edit-field-piece-type-und-instrumental"]')
    if pieza_inst.is_selected():
       pieza_inst.click()

    if Tipo_pieza[i] == 'vocal':
        driver.find_element("xpath", '//*[@id="edit-field-piece-type-und-vocal"]').click()
        print(Fore.GREEN + '[ok]' + Fore.RESET + f' TIPO DE PIEZA: actualizando {Tipo_pieza[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass

    elif Tipo_pieza[i] == 'instrumental':
        driver.find_element("xpath", '//*[@id="edit-field-piece-type-und-instrumental"]').click()
        pass
    
    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f'  TIPO DE PIEZA: valor {Tipo_pieza[i]} inesperado para {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass

    
## ID PIEZA
    
    try:
        idpieza = driver.find_element("xpath", '//*[@id="edit-field-piece-id-und-0-value"]')
        idpieza.clear()
        idpieza.click()
    except:
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' ID_PIEZA: Fallo al actualizar {ID_pieza[i]} a {Titulo[i]} (registro {i + 1}) de REPERTORIO')
        
    print(Fore.GREEN + f'[ok]' + Fore.RESET + f' ID_PIEZA: actualizando {ID_pieza[i]} a {Titulo[i]} (registro {i + 1}) de REPERTORIO')
    
    try:
        idpieza.send_keys(ID_pieza[i])
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  Fallo al actualizar ID PIEZA {ID_pieza[i]} en la posición Nº {i + 1}')
  
    '''    
#Nota_inicial
    
    # Esperar hasta que el elemento sea clickable
    wait = WebDriverWait(driver, 10)
    spitch = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="edit-field-starting-pitch-und"]')))

    # Hacer clic en el elemento
    spitch.click()

    # Utilizar la clase Select para interactuar con el menú desplegable
    spitchselector = Select(spitch)

    # Obtener todas las opciones del menú desplegable
    #spitchoptions = [option.text for option in aspitch.options]
    spitchoptions = [option.text for option in spitch.find_elements(By.TAG_NAME, 'option')]

    # Valor de la base de datos
    spitchDB = Nota_inicial[i]  # Reemplaza 'TuValor' con el valor real de la base de datos

    # Verificar si el valor en la base de datos está presente en las opciones
    if spitchDB in spitchoptions:
    # Seleccionar la opción que coincide con el valor en la base de datos
        spitchselector.select_by_visible_text(spitchDB)
        print(Fore.GREEN + '[ok]' + Fore.RESET + f" NOTA_INICIAL: '{spitchDB}' añadida correctamente a '{Titulo[i]} '({i + 1} de REPERTORIO)")
    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f"  NOTA_INICIAL: '{spitchDB}' no existe en el menú o en el campo Nota_inicia de '{Titulo[i]}'({i + 1} de REPERTORIO)")
    '''
    '''
    #Generos01 y 02

    #Remove Género
    #driver.find_element("xpath", '/html/body/div[3]/div[2]/div[2]/div/div/form/div/div[9]/div/div/div[2]/table/tbody/tr/td[2]/a').click()
       
    gen01_low = Genero01[i].lower()
    gen01_upp = Genero01[i].upper()
    gen02_low = Genero02[i].lower()
    gen02_upp = Genero02[i].upper()
    gen03_low = Genero03[i].lower()
    gen03_upp = Genero03[i].upper()
        

    try:    
        driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-selects-0"]/option[contains(translate(., "{gen01_low}","{gen01_upp}"), "{gen01_upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-selects-1"]/option[contains(translate(., "{gen02_low}","{gen02_upp}"), "{gen02_upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-dropbox-add--2"]').click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' GENEROS: actualizando {Genero01[i]} {Genero02[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        time.sleep(3)
    except:
        #driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-selects-0"]/option[contains(translate(., "{gen01_low}","{gen01_upp}"), "{gen01_upp}")]').click()
        #time.sleep(3)
        #driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-selects-1"]/option[contains(translate(., "{gen02_low}","{gen02_upp}"), "{gen02_upp}")]').click()
        #time.sleep(3)
        #driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-selects-2"]/option[contains(translate(., "{gen03_low}","{gen03_upp}"), "{gen03_upp}")]').click()
        #time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-genre-und-hierarchical-select-dropbox-add--3"]').click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' GENEROS: actualizando {Genero01[i]} {Genero02[i]} {Genero03[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        time.sleep(3)
    '''
    
    #Informantes

    try:
        informantei = driver.find_element("xpath", '//*[@id="edit-field-informant-und-0-nid"]')
        informantei.clear()
        informantei.click()
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  INFORMANTE01: Fallo al actualizar {Titulo[i]} (registro {i + 1} de REPERTORIO)')

    print(Fore.GREEN + f'[ok]' + Fore.RESET + f' INFORMANTE01: actualizando "{Informante01[i]}" a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
    
    try:
        informantei.send_keys(Informante01[i])
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f' INFORMANTE01: fallo al actualizar "{Informante01[i]}" a {Titulo[i]} (registro {i + 1} de REPERTORIO)')

    ###Localidad, Provincia y CA

    #Remove Localidad, Provincia y CA
    #driver.find_element("xpath", 'html/body/div[3]/div[2]/div[2]/div/div/form/div/div[11]/div/div/div[2]/table/tbody/tr/td[2]/a').click()
        
    caautonoma_1low = Comunidad_Autonoma[i].lower()
    caautonoma_1upp = Comunidad_Autonoma[i].upper()
    provincia_2low = Provincia[i].lower()
    provincia_2upp = Provincia[i].upper()
    localidad_3low = Localidad[i].lower()
    localidad_3upp = Localidad[i].upper()
    
    try:    
        driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-0"]/option[contains(translate(., "{caautonoma_1low}","{caautonoma_1upp}"), "{caautonoma_1upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-1"]/option[contains(translate(., "{provincia_2low}","{provincia_2upp}"), "{provincia_2upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-2"]/option[contains(translate(., "{localidad_3low}","{localidad_3upp}"), "{localidad_3upp}")]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-dropbox-add--3"]').click()
        time.sleep(5)
        
    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  LOCALIDAD: fallo, al actualizar la localidad de la pieza {Titulo[i]} ({i + 1} de REPERTORIO)')
        #Saliendo de la pieza {Titulo [i]} con posición Nº {i + 1} y continuando''')
        #errors.append(f'{Titulo [i]} con posición Nº {i + 1}')
        #driver.find_element("xpath", '/html/body/div[1]/header/nav/div[1]/ul/li[1]/a').click()
        time.sleep(3)
        #continue
    
    print (Fore.GREEN + '[ok]' + Fore.RESET + f' LOCALIDAD: actualizando {Localidad[i]} a {Titulo[i]} ({i + 1} de REPERTORIO)')   
    
    #except:
        #print(Fore.RED + 'Fallo al actualizar pieza {Titulo[i]} (Nº {i + 1}, ID {ID_pieza[i]})')

####Fuente

    '''
    try:
        fuente = driver.find_element("xpath", '//*[@id="edit-field-source-und"]/option[181]')
        fuente.clear()
        fuente.click()
        time.sleep(5)

    except:
        print(Fore.RED + '[x]' + Fore.RESET + f'  FUENTE: fallo en la pieza {Titulo[i]} ({i + 1} de REPERTORIO)')  
        errors.append(f'{Titulo[i]} con la posición Nº {i + 1}')
    print (Fore.GREEN + '[ok]' + Fore.RESET + f' FUENTE: actualizando AMRQ_ASFPardo a la pieza {Titulo[i]} ({i + 1} de REPERTORIO)')

    		
####Investigador  

    try:
       # Localizar la casilla de búsqueda
       investigadori = driver.find_element("xpath", '//*[@id="edit-field-researcher-und-0-nid"]')
       investigadori.clear()
       # Ingresar el valor para la búsqueda
       nid_value = "Pardo Pardo, Fermín"
       investigadori.send_keys(nid_value)
       # Puedes enviar la tecla "Enter" para activar la búsqueda
       investigadori.send_keys(Keys.ENTER)
    
    except:
        print(Fore.RED + 'Fallo al actualizar investigador en la pieza {Titulo[i]} (#{ID_pieza[i]})')

    print (Fore.GREEN +'[ok]' + Fore.RESET + f' INVESTIGADOR: actualizando Pardo, Fermín' + Fore.RED + ' [preset] ' + Fore.RESET  + f'a {Titulo[i]} ({i + 1} de REPERTORIO)')

####Institución colaboradora = Conservatorio de Música "Maestro Jaime López", Molina de Segura, (Murcia) /html/body/div[3]/div[2]/div[2]/div/div/form/div/div[16]/div/select/option[9
####Institución colaboradora = Universidad de Murcia (UM) /html/body/div[3]/div[2]/div[2]/div/div/form/div/div[16]/div/select/option[31]
    
    # Localiza el elemento select
    mi_select = driver.find_element("id", "edit-field-collaborating-institution-und")

    # Utiliza la clase Select
    select = Select(mi_select)

    # Valores que deseas seleccionar
    valores_a_seleccionar = ["67602", "67601", "63826", "36926"]

    # Utiliza la tecla de control para seleccionar múltiples elementos
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)

    for valor in valores_a_seleccionar:
        select.select_by_value(valor)
        actions.key_down(Keys.CONTROL)

        # Libera la tecla de control después de seleccionar los elementos
        actions.key_up(Keys.CONTROL).perform()

    print (Fore.GREEN + '[ok]' + Fore.RESET + f' INST. COLABORADORA: actualizando Conservatorio Molina y UMU' + Fore.RED + f' [preset] ' + Fore.RESET + f'a {Titulo[i]} ({i + 1} de REPERTORIO)')    


####Personas colaboradoras= López López, Albert /html/body/div[3]/div[2]/div[2]/div/div/form/div/div[17]/div/select/option[57]
####Personas colaboradoras= Pardo-Cayuela, Antonio /html/body/div[3]/div[2]/div[2]/div/div/form/div/div[17]/div/select/option[78]
    
    # Localiza el elemento select
    mi_select = driver.find_element("id", "edit-field-collaborating-people-und")

    # Utiliza la clase Select
    select = Select(mi_select)

    # Valores que deseas seleccionar
    valores_a_seleccionar = ["63823", "67603", "36928"]

    # Utiliza la tecla de control para seleccionar múltiples elementos
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)

    for valor in valores_a_seleccionar:
        select.select_by_value(valor)
        actions.key_down(Keys.CONTROL)

        # Libera la tecla de control después de seleccionar los elementos
        actions.key_up(Keys.CONTROL).perform()

    print (Fore.GREEN + '[ok]' + Fore.RESET + f' PERSONAS COLABORADORAS: actualizando López López, Albert y Pardo-Cayuela, Antonio' + Fore.RED + f' [preset] ' + Fore.RESET + f'a {Titulo[i]} ({i + 1} de REPERTORIO)')

    ###Text
    ##TO DO

    ###Observaciones
    ##TO DO

    ##Imagen
    ##TO DO

    ##PDF IMAGE
    ##TO DO

    ###AUDIO (MP3)

    try:
        # Esperar a que el elemento sea visible y pueda ser clickeable
        delete_audio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "edit-field-audio-und-0-remove-button")))
        # Una vez que el elemento sea clickeable, hacer clic en él
        delete_audio.click()
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f" Archivo de audio eliminado")
    
    except NoSuchElementException:
        print(Fore.RED + f'[x]' + Fore.RESET + f"  Archivo de audio no encontrado para eliminar")



    generic_mp3_path = "/home/antonio/ASFPardo_audios/AMRQ_ASFP_001ABmp3/"
    mp3file = Audio[i]
    full_path_to_file = os.path.join(generic_mp3_path, mp3file)

    # Localizar el elemento de entrada de tipo archivo
    inputarchivo = driver.find_element("xpath", '//*[@id="edit-field-audio-und-0-upload"]')

    # Esperar a que el elemento esté presente en el DOM
    wait = WebDriverWait(driver, 10)
    inputarchivo = wait.until(EC.presence_of_element_located(("xpath", '//*[@id="edit-field-audio-und-0-upload"]')))

    # Hacer el campo de entrada visible mediante el cambio de estilo
    driver.execute_script('arguments[0].style = "";', inputarchivo)

    # Limpiar el campo de entrada
    inputarchivo.clear()

    # Enviar la ruta del archivo al campo de entrada
    inputarchivo.send_keys(full_path_to_file)

    # Esperar a que el archivo se cargue completamente antes de realizar más acciones
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="loader"]')))

    print (Fore.GREEN + '[ok]' + Fore.RESET + f' AUDIO FILE: subiendo {Audio[i]} a {Titulo[i]} ({i + 1} de REPERTORIO)')
    
    '''
    
    ###Idioma
#Desactivar idioma español (configurado así por defecto en FMT)
    driver.find_element("xpath", '//*[@id="edit-field-language-und-3566"]').click()

    ##Añadir idioma Español/Spanish o Català/Mallorquí/Valencià

    if Idioma[i] == 'Español/Spanish':
        driver.find_element("xpath", '//*[@id="edit-field-language-und-3566"]').click()
        print(Fore.GREEN + '[ok]' + Fore.RESET + f' IDIOMA: actualizando {Idioma[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass

    elif Idioma[i] == 'Català/Mallorquí/Valencià':
        driver.find_element("xpath", '//*[@id="edit-field-language-und-3567"]').click()
        print(Fore.GREEN + '[ok]' + Fore.RESET + f' IDIOMA: actualizando {Idioma[i]} a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass
    
    elif Idioma[i] == '':
        #driver.find_element("xpath", '//*[@id="edit-field-language-und-3567"]').click()
        print(Fore.GREEN + '[ok]' + Fore.RESET + f' IDIOMA: pieza sin idioma a {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass
    
    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f' IDIOMA: valor {Idioma[i]} inesperado para {Titulo[i]} (registro {i + 1} de REPERTORIO)')
        pass


    #Autor de la entrada

    #Desactivar casilla "Albert López López"
    driver.find_element("xpath", '//*[@id="edit-field-editors-und-8651"]').click()

    if submission_author:='Albert López López':
        try:                 
            driver.find_element("xpath", '//*[@id="edit-field-editors-und-8651"]').click()
        except:             
            pass
    else:
        print(Fore.RED + 'Fallo grave.' + Fore.RED + f'''Fallo al actualizar el autor de la entrada.\n
        Saliendo de pieza {Titulo[i]} ({i + 1}). Continuando...''')
        errors.append(f).click()
        driver.find_element("xpath", '/html/body/div[1]/header/nav/div[1]/ul/li[1]/a').click()
        time.sleep(3)
    print(Fore.GREEN + '[ok]' + Fore.RESET + f' AUTOR ENTRADA: actualizando López López, Albert' + Fore.RED + ' [preset] ' + Fore.RESET + f'a {Titulo[i]} ({i + 1} de REPERTORIO)')
    #continue
        
##Guardar entrada 
#guardar = driver.find_element("xpath", '//*[@id="edit-submit"]')       
#guardar.click()
#time.sleep(3)
#url_fmt = driver.current_url
#cur.execute(f'UPDATE repertorio SET URL_FMT=? WHERE ID_pieza =?', (url_fmt, int(ID_pieza[i])))
#con.commit()
#time.sleep(5)

#url_fmt = driver.current_url
#cur.execute("UPDATE repertorio SET URL_FMT=? WHERE ID_pieza =?", (url_fmt, ID_pieza[i]))
#con.commit()
#time.sleep(5)


    try:
       wait.until(EC.element_to_be_clickable(("xpath", '//*[@id="edit-submit"]'))).click()
       time.sleep(5)
       url_ref = driver.current_url
       #cur.execute(f'UPDATE informantes SET URL_FMT=? WHERE ID =?', (url_ref, int(id_sql[i])))
       cursor.execute(f'UPDATE repertorio SET URL_FMT=? WHERE ID_pieza=?', (url_ref, ID_pieza[i]))
       #con.commit()
       #time.sleep(2)
       print(Fore.GREEN + f'[ok]' + Fore.RESET + f'Guardando ACTUALIZACIÓN pieza {Titulo[i]} (nº {i + 1} de REPERTORIO)')
    except:
        print(Fore.RED + f'[x]' + f'FALLO GRAVE: error al guardar la entrada.\n'
                    f'Saliendo pieza {Titulo[i]} ({i + 1} ).\n'
                  f'Continuando con pieza {Titulo[i]} ({i + 1})')

    
    #driver.get('https://musicatradicional.eu/es/node/add/piece')    

con.close()
driver.quit()

###Mensajes finales        
    

print(Fore.GREEN + f'==========Actualización de registros completada==========')
        
if len(errors) == 0:
    print(Fore.RESET + f'NO SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN.')
    pass
else:
    print(Fore.RED + f'SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN\nREVISE EN FMT Y/O EN LA TABLA REPERTORIO EL CONTENIDO DE LOS REGISTROS.\n')
    for i in errors:
        print(Fore.RED + '[x]' + Fore.RED + f'Fallo en  {i}. Si desea repetir la actualización del registro erróneo, revise los datos del mismo')
