from colorama import Fore, Style, init
import sqlite3

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