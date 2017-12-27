#!/usr/bin/env python
import urllib2
import hashlib
import requests
import time
from datetime import datetime
from os.path import exists
from core.utils import utils

#url = 'https://media.readthedocs.org/pdf/requests/latest/requests.pdf'
#url = 'http://docs.python.org.ar/tutorial/pdfs/TutorialPython2.pdf'
url = 'https://www.gestiondocumental.gob.ec/bodega/tmp/'
banner = utils()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def menu():
    global valIni
    global valFin
    
    banner.banner()
    #print(banner.color['purple'] + "hey")
    valIni = input('Ingrese el valor inicial de descarga   :')
    valFin = input('Ingrese el valor final de la descarga  :')
    
    #banner.color['purple']
    banner.colorTexto('info', '\n[i] URL cargada correctamente.')
    directorio = 'quipux2'
    banner.colorTexto("info", '[i] Directorio creado: [' + directorio + ']')
    print('')
    print('              Iniciando la descarga de archivos......')
    print('................................................................')

    crear_fichero_log()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def crear_fichero_log():
    global fichero_registro
    fecha = datetime.now
    fichero_registro = 'quiPWN_' + format(fecha().strftime('%d-%m-%Y_%H-%M-%S')) + '.txt'
    # descomentar la siguiente linea
    #registro_log('Registros de archivos descargados de Quipux, solo guarda documentos encontrados\n\n')

def registro_log(log):
    log_quipux = open (fichero_registro, 'a')
    log_quipux.write(log + '\n')
    log_quipux.close()
    return 0

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def descarga(url_descarga, item):
    
    #respuesta = requests.head(url_descarga,allow_redirects=False)
    try:
        respuesta = requests.request('GET', url_descarga)
    except respuesta.exceptions.ConnectionError:
        respuesta.status_code = 'Conexion rechazada por el servidor'
        #print( respuesta.status_code + 'Esperando 2 segundos....')
        time.sleep(2)
    #continue
    #r = respuesta.headers['content-type']
    if (respuesta.status_code == 200):
    #if 'pdf' in r: 
        try:
            bufer = bytes()
            archivo_remoto = urllib2.urlopen(url_descarga)
            tam_max_arch=100*1024*1024
            hash = hashlib.md5()
            
            lectura_total = 0
            while True:
                data = archivo_remoto.read(4096)
                lectura_total += 4096
                bufer += data
                
                if not data: #or lectura_total > tam_max_arch:
                    break

                hash.update(data)
            md5 = hash.hexdigest()
            
            fichero_local = md5 + '.pdf'
        
            if not exists(fichero_local):
                fichero_local = open(md5 +'.pdf', 'w')
                fichero_local.write(bufer)
                fichero_local.close()
                log_grabar = str(item) + ': ' + md5 + '.pdf'
                print('[\033[1;32m+\033[1;m] {' + md5 + '} descargado correctamente [' + str(lectura_total) + ' bytes] ' + str(item))
                registro_log(log_grabar)
            else:
                print('[\033[1;33m>\033[1;m] Ya existe el archivo ' + fichero_local + ' :' + str(item))
        except requests.exceptions.Timeout:
            fchero_local.status_code = 'tiempo de espera agotado'
            print ('error de descarga...')
         #   continue
    else:
       print('[\033[1;31m-\033[1;m] No hay datos, buscando....' + str(item) )

    return 0
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def quipwn(valIni, valFin):
    for i in range(valIni, valFin+1):
        archivo_quipux = str(i) + '.pdf'
        url_quipux = url + archivo_quipux
        descarga(url_quipux, i)


menu()
quipwn(valIni,valFin)
#descarga(url)

