import dbconnect

import login

import registers_select

#import checkinformant

try:
    driver.get('https://musicatradicional.eu/es/node/add/informant')
    driver.find_element("xpath", '//*[@id="edit-title"]').send_keys(Nombre_FMT[i])
except:
    print(Fore.RED + f'Fallo al añadir el Nombre_FMT del informante {Nombre_FMT[i]} en la posición Nº {i + 1}')

#Fecha de grabación

#Ano

#Edad

#Profesion

    #Lugar_residencia
try:
    driver.find_element("xpath", '//*[@id="edit-field-place-of-residence-und-0-value"]').send_keys(Lugar_residencia[i])
    print(Fore.GREEN + '[ok]' + Fore.RESET + f'LUGAR de RESIDENCIA: localidad de residencia del informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')
except:
     print(Fore.RED + '[x]' + Fore.RESET + f'LUGAR de RESIDENCIA: fallo al añadir la localidad de residencia del informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')

    #Lugar de nacimiento
try:
    driver.find_element("xpath", '//*[@id="edit-field-place-of-birth-und-0-value"]').send_keys(Lugar_nacimiento[i])
        
except:
     print(Fore.RED + '[x]' + Fore.RESET + f'LUGAR de NACIMIENTO: fallo al añadir en el informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')

print(Fore.GREEN + '[ok]' + Fore.RESET + f'LUGAR NACIMIENTO: localidad de nacimiento del informante {Nombre_FMT[i]} ({i + 1} de INFORMANTES)')     


#Comentarios

try:
    driver.find_element("xpath", '//*[@id="edit-field-remarks-informant-und-0-value"]').send_keys(Comentarios[i])
except:
    print(Fore.RED + '[x]' + Fore.RESET + f'  COMENTARIOS: fallo al añadirlas a {Nombre_FMT[i]} registro {i + 1} de INFORMANTES)')
        
print(Fore.GREEN + f'[ok]' + Fore.RESET + f' COMENTARIOS: añadiendo {Comentarios[i]} a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')


#Ficha original



#Misiones / Concursos Activar para los informantes extraidos de los cuadernos de Fermín Pardo
    
'''
try:
    driver.find_element("xpath", '//*[@id="edit-field-source-und"]/option[181]').click()
    time.sleep(5)

except:
    print(Fore.RED + '[x]' + Fore.RESET + f'  FUENTE: fallo en la pieza {Titulo[i]} ({i + 1} de REPERTORIO)')  
    errors.append(f'{Titulo[i]} con la posición Nº {i + 1}')
print (Fore.GREEN + '[ok]' + Fore.RESET + f' FUENTE: añadiendo AMRQ_ASFPardo a la pieza {Titulo[i]} ({i + 1} de REPERTORIO)')

'''

        
#Localidad, provincia, CA    
loc_1low = Comunidad_Autonoma[i].lower()
loc_1upp = Comunidad_Autonoma[i].upper()
loc_2low = Provincia[i].lower()
loc_2upp = Provincia[i].upper()
loc_3low = Localidad[i].lower()
loc_3upp = Localidad[i].upper()
    
    
try:    
    driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-0"]/option[contains(translate(., "{loc_1low}","{loc_1upp}"), "{loc_1upp}")]').click()
    time.sleep(3)
    driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-1"]/option[contains(translate(., "{loc_2low}","{loc_2upp}"), "{loc_2upp}")]').click()
    time.sleep(3)
    driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-selects-2"]/option[contains(translate(., "{loc_3low}","{loc_3upp}"), "{loc_3upp}")]').click()
    time.sleep(3)
    driver.find_element("xpath", '//*[@id="edit-field-location-official-und-hierarchical-select-dropbox-add--3"]').click()
    time.sleep(5)
        
except:
    print(Fore.RED + '[x]' + Fore.RESET + f' LOCALIDAD: No es possible añadirla a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')
    
    time.sleep(3)
    #continue

    
#Sexo
    
if {Sexo[i]} == 'hombre':
    driver.find_element("xpath", '//*[@id="edit-field-man-female-und-7234"]').click()
elif {Sexo[i]} == 'mujer':
    driver.find_element("xpath", '//*[@id="edit-field-man-female-und-7235"]').click()
elif {Sexo[i]} == 'na':       
    driver.find_element("xpath", '//*[@id="edit-field-man-female-und-none"]"]').click()
else:

    pass    

#Audiovisuales selección "Audio" y "Cinta"
           
    if {Audiovisuales[i]} == 'cinta':
        driver.find_element('xpath', '//*[@id="edit-field-audiovisual-und-hierarchical-select-selects-0--2"]').click()
        driver.find_element('xpath', '//*[@id="edit-field-audiovisual-und-hierarchical-select-selects-1"]').click()
        driver.find_element('xpath', '//*[@id="edit-field-audiovisual-und-hierarchical-select-dropbox-add--2"]')
        print(Fore.GREEN + f'[ok]' + Fore.RESET + f' AUDIO: añadiendo Audio/Cinta a {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

    else:
        print(Fore.RED + f'[x]' + Fore.RESET + f'  AUDIO: campo vacío para {Nombre_FMT[i]} (registro {i + 1} de INFORMANTES)')

        pass               

#Autor de la entrada

    driver.find_element("xpath", '//*[@id="edit-field-editors-und-8651"]').click()
    driver.find_element("xpath", '//*[@id="edit-field-editors-und-5133"]').click()
             
        
 #Guardar entrada 

guardar = driver.find_element("xpath", '//*[@id="edit-submit"]')       
guardar.click()
time.sleep(3)
        
#Guardar URL en URL_FMT        
url_fmt = driver.current_url
cur.execute("UPDATE informantes SET URL_FMT=? WHERE ID =?", (url_fmt, int(ID[i])))
con.commit()
time.sleep(5)
    #except:
        #print(Fore.RED + f'Fallo grave.' + Fore.GREEN + f'No se pudo guardar la entrada.\n'
        #+ Fore.RESET + f'Saliendo de informante {Nombre_FMT[i]} con posición Nº {i + 1} y continuando')
        #errors.append(f'{Nombre_FMT[i]} con la posición Nº {i + 1}')
        #continue
        
        
    
con.close()
print(Fore.RED + 'La ejecución ha terminado. Revise los resultados a continuación en busca de posibles errores.\n')
        
if len(errors) == 0:
    print(Fore.GREEN + 'NO SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN.')
    pass
else:
    print(Fore.RED + 'SE HAN PRODUCIDO ERRORES GRAVES DURANTE LA EJECUCIÓN\nDEBE VOLVER A SUBIR LOS SIGUIENTES INFORMANTES.\n')
    for i in errors:
        print(Fore.RED + 'Fallo en' + f' {i}. ' + 'Si desea repetir la subida del informante que ha dado problemas, revise los datos, vuelva a ejecutar el código e introduzca el número ordinario que representa dicho informante en las filas de la base de datos')

#driver.close()