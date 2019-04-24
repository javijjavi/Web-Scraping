import requests
import re
import time
from bs4 import BeautifulSoup
import os

def introducir_url():
    url = str(input("Introduzca aqui la URL: "))
    time.sleep(2)
    comprobacion_url(url)
    return url

def comprobacion_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Hemos analizado la URL y todo se ecuentra en correcto estado.")
        time.sleep(2)
        eleccion_datos(response)

    elif response.status_code == 404:
        print("Lo sentimos mucho pero la URL introducida no se encuentra.")
        eleccion = str(input("Desea volver a introducir la URL (si/no): "))
        if eleccion == "si" or eleccion == "s":
            introducir_url()
        elif eleccion == "no" or eleccion == "n":
            print("Gracias por utilizar este programa. Adios")
            exit()
        else:
            print("Lo sentimos pero no hemos entendido su repuesta. La proxima escriba si o no.")
            time.sleep(2)
            comprobacion_url(url)
    else:
        print("Lo sentimos mucho pero hay algun fallo con la URL")
        eleccion = str(input("Desea volver a introducir la URL (si/no): "))
        if eleccion == "si" or eleccion == "s":
            introducir_url()
        elif eleccion == "no" or eleccion == "n":
            print("Gracias por utilizar este programa. Adios")
            exit()
        else:
            print("Lo sentimos pero no hemos entendido su repuesta. La proxima escriba si o no.")
            time.sleep(2)
            comprobacion_url(url)
    return response

def eleccion_datos(response):
    print("Esta es la informacion que puede extraer de la pagina:")
    time.sleep(2)
    print("+-------------------+")
    print("| HTML------------1 |")
    print("| FORMS-----------2 |")
    print("| MEDIA-----------3 |")
    print("| GRAPHICS--------4 |")
    print("+-------------------+")

    var_introducido = int(input("Por favor seleccione una opcion: "))
    
    if var_introducido == 1:
        time.sleep(1)
        datos_html()    
    elif var_introducido == 2:
        time.sleep(1)
        datos_forms(response)
    elif var_introducido == 3:
        time.sleep(1)
        datos_media(response)
    elif var_introducido == 4:
        time.sleep(1)
        datos_grapihcs(response)
    else:
        print("Lo sentimos mucho pero el codigo introducido no corresponde con ninguno de la tabla.")
        time.sleep(1)
        print("Por favor intentelo de nuevo.")
        time.sleep(1)
        eleccion_datos(response)

def datos_html():
    print("+--------------------+")
    print("| BASIC----------- 1 |")
    print("| ELEMENTS-------- 2 |")
    print("| ATTRIBUTES------ 3 |")
    print("| HEADINGS-------- 4 |")
    print("| PARAGRAPHS------ 5 |")
    print("| STYLES---------- 6 |") 
    print("| FORMATTING------ 7 |")
    print("| QUOTATIONS------ 8 |")
    print("| COMMENTS-------- 9 |")
    print("| COLORS----------10 |")
    print("| CSS-------------11 |")
    print("| LINKS-----------12 |")
    print("| IMAGES----------13 |")
    print("| TABLES----------14 |")
    print("| LISTS-----------15 |")
    print("| BLOCKS----------16 |")
    print("| CLASSES---------17 |")
    print("| ID--------------18 |")
    print("| IFRAMES---------19 |")
    print("| JAVASCRIPT------20 |")
    print("| BACK------------99 |")
    print("+--------------------+")

def datos_forms(response):
    print("+-------------------+")
    print("| ALL-------------1 |")
    print("| ELEMENTS--------2 |")
    print("| TYPES-----------3 |")
    print("| BACK-----------90 |")
    print("| EXIT-----------99 |")
    print("+-------------------+")
    
    insertar_opcion = int(input("Porfavor introduce un codigo: "))
    soup = BeautifulSoup(response.text, "html.parser")

    if insertar_opcion == 1:
        print("Has seleccionado ALL, te vamos a mostrar todos los form que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('form')
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 2:
        print("Has seleccionado ELEMENTS, este es todo el codigo audio que hemos encontrado.")
        time.sleep(1)
        resultado1 = soup.find_all('input')
        resultado2 = soup.find_all('select')
        resultado3 = soup.find_all('option')
        resultado4 = soup.find_all('textarea')
        resultado5 = soup.find_all('button')
        resultado = resultado1 + resultado2 + resultado3 + resultado4 + resultado5
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 3:
        print("+----------------------+")
        print("| BUTTON-------------1 |")
        print("| CHECKBOX-----------2 |")
        print("| COLOR--------------3 |")
        print("| DATE---------------4 |")
        print("| DATETIME-LOCAL-----5 |")
        print("| EMAIL--------------6 |")
        print("| FILE---------------7 |")
        print("| HIDDEN-------------8 |")
        print("| IMAGE--------------9 |")
        print("| MONTH-------------10 |")
        print("| NUMBER------------11 |")
        print("| PASSWORD----------12 |")
        print("| RADIO-------------13 |")
        print("| RANGE-------------14 |")
        print("| RESET-------------15 |")
        print("| SEARCH------------16 |")
        print("| SUBMIT------------17 |")
        print("| TEL---------------18 |")
        print("| TEXT--------------19 |")
        print("| TIME--------------20 |")
        print("| URL---------------21 |")
        print("| WEEK--------------22 |")
        print("| BACK--------------90 |")
        print("| EXIT--------------99 |")
        print("+----------------------+")

        opcion_insertada = int(input("Porfavor introduzca una opcion: "))

        if opcion_insertada == 1:
            print("Has seccionado BUTTON")
            time.sleep(1)
            resultado = soup.find_all('input' ,type='button')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 2:
            print("Has seccionado CHECKBOX")
            time.sleep(1)
            resultado = soup.find_all('input', type='checkbox')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 3:
            print("Has seccionado COLOR")
            time.sleep(1)
            resultado = soup.find_all('input', type='color')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 4:
            print("Has seccionado DATE")
            time.sleep(1)
            resultado = soup.find_all('input', type='date')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 5:
            print("Has seccionado DATETIME-LOCAL")
            time.sleep(1)
            resultado = soup.find_all('input', type='datetime-local')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 6:
            print("Has seccionado EMAIL")
            time.sleep(1)
            resultado = soup.find_all('input', type='email')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 7:
            print("Has seccionado FILE")
            time.sleep(1)
            resultado = soup.find_all('input', type='file')
            salida(resultado, response)
            return resultado
        
        elif opcion_insertada == 8:
            print("Has seccionado HIDDEN")
            time.sleep(1)
            resultado = soup.find_all('input', type='hidden')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 9:
            print("Has seccionado IMAGE")
            time.sleep(1)
            resultado = soup.find_all('input', type='image')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 10:
            print("Has seccionado MONTH")
            time.sleep(1)
            resultado = soup.find_all('input', type='month')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 11:
            print("Has seccionado NUMBER")
            time.sleep(1)
            resultado = soup.find_all('input', type='number')
            salida(resultado, response)
            return resultado
        
        elif opcion_insertada == 12:
            print("Has seccionado PASSWORD")
            time.sleep(1)
            resultado = soup.find_all('input', type='password')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 13:
            print("Has seccionado RADIO")
            time.sleep(1)
            resultado = soup.find_all('input', type='radio')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 14:
            print("Has seccionado RANGE")
            time.sleep(1)
            resultado = soup.find_all('input', type='range')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 15:
            print("Has seccionado RESET")
            time.sleep(1)
            resultado = soup.find_all('input', type='reset')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 16:
            print("Has seccionado SEARCH")
            time.sleep(1)
            resultado = soup.find_all('input', type='search')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 17:
            print("Has seccionado SUBMIT")
            time.sleep(1)
            resultado = soup.find_all('input', type='submit')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 18:
            print("Has seccionado TEL")
            time.sleep(1)
            resultado = soup.find_all('input', type='tel')
            salida(resultado, response)
            return resultado
        
        elif opcion_insertada == 19:
            print("Has seccionado TEXT")
            time.sleep(1)
            resultado = soup.find_all('input', type='text')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 20:
            print("Has seccionado TIME")
            time.sleep(1)
            resultado = soup.find_all('input', type='time')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 21:
            print("Has seccionado URL")
            time.sleep(1)
            resultado = soup.find_all('input', type='url')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 22:
            print("Has seccionado WEEK")
            time.sleep(1)
            resultado = soup.find_all('input', type='week')
            salida(resultado, response)
            return resultado
        elif opcion_insertada == 90:
            time.sleep(1)
            eleccion_datos(response)
        elif opcion_insertada == 99:
            exit()
        else:
            time.sleep(1)
            print("No hemos entendido el codigo que ha introducido.")
            print("Vuelva a introducirlo porfavor.")
            time.sleep(1)
            datos_forms(response)

    elif insertar_opcion == 90:
        time.sleep(1)
        eleccion_datos(response)
    elif insertar_opcion == 99:
        exit()
    else:
        time.sleep(1)
        print("No hemos entendido el codigo que ha introducido.")
        print("Vuelva a introducirlo porfavor.")
        time.sleep(1)
        datos_forms(response)

def datos_media(response):
    print("+--------------------+")
    print("| VIDEO------------1 |")
    print("| AUDIO------------2 |")
    print("| PLUG-INS---------3 |")
    print("| YOUTUBE----------4 |")
    print("| BACK------------90 |")
    print("| EXIT------------99 |")
    print("+--------------------+")

    insertar_opcion = int(input("Porfavor introduce un codigo: "))
    soup = BeautifulSoup(response.text, "html.parser")

    if insertar_opcion == 1:
        print("Has seleccionado VIDEO, este es todo el codigo video que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('video')
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 2:
        print("Has seleccionado AUDIO, este es todo el codigo audio que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('audio')
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 3:
        print("Has seleccionado PLUG-INS, este es todo el codigo plug-ins que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('object')
        resultado1 = soup.find_all('embed')
        resultado = resultado + resultado1
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 4:
        print("Has seleccionado YOUTUBE, este es todo el codigo youtube que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('iframe')
        
        salida(resultado, response)
        return resultado

    elif insertar_opcion == 90:
        time.sleep(1)
        eleccion_datos(response)
    elif insertar_opcion == 99:
        exit()
    else:
        time.sleep(1)
        print("No hemos entendido el codigo que ha introducido.")
        print("Vuelva a introducirlo porfavor.")
        time.sleep(1)
        datos_media(response)

def datos_grapihcs(response):
    print("+-------------------+")
    print("| CANVAS----------1 |")
    print("| SVG-------------2 |")
    print("| BACK-----------90 |")
    print("| EXIT-----------99 |")
    print("+-------------------+")

    insertar_opcion = int(input("Porfavor introduce un codigo: "))
    soup = BeautifulSoup(response.text, "html.parser")

    if insertar_opcion == 1:
        print("Has seleccionado CANVAS, este es todo el codigo canvas que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('canvas')
        salida(resultado, response)
        return resultado
    elif insertar_opcion == 2:
        print("Has seleccionado SVG, este es todo el codigo svg que hemos encontrado.")
        time.sleep(1)
        resultado = soup.find_all('svg')
        salida(resultado, response)
        return resultado

    elif insertar_opcion == 90:
        time.sleep(1)
        eleccion_datos(response)
    elif insertar_opcion == 99:
        exit()
    else:
        time.sleep(1)
        print("No hemos entendido el codigo que ha introducido.")
        print("Vuelva a introducirlo porfavor.")
        time.sleep(1)
        datos_grapihcs(response)

def salida(resultado, response):
    if len(resultado) < 1:
        print("Lo sentimos mucho pero no hemos encontrado nada.")
        time.sleep(1)
        volver_lanzar = str(input("Quiero volver a buscar otro dato (si/no): "))
        if volver_lanzar == "si" or volver_lanzar == "s":
            eleccion_datos(response)
        elif volver_lanzar == "no" or volver_lanzar == "n":
            print("Adios. Muchas gracias")
            exit()
        else:
            print("No entendemos el digito seleccionado, por favor introduzcalo de nuevo.")
            salida(resultado, response)
    else:
        print("Estos son los formatos de salida disponibles: ")
        print("+------------------+")
        print("|TXT--------------1|")
        print("|TERMINAL---------2|")
        print("|SALIR-----------99|")
        print("+------------------+")
        formato_salida = int(input("Seleccione un formato de salida: "))
        if formato_salida == 1:
            if os.path.exists("salida-web-scraper.txt"):
                os.remove("salida-web-scraper.txt")
            f = open("salida-web-scraper.txt", "w")
            resultado = str(resultado)
            f.write(resultado)
            f.close()
            time.sleep(2)
            print("Muchas gracias. Adios")
            exit()

        elif formato_salida == 2:
            print(resultado)
            time.sleep(2)
            print("Muchas gracias. Adios")
            exit()

        elif formato_salida == 99:
            print("Adios.")
            exit()
        else:
            print("El cogido introducido no se entiende, por favor vuelva a marcalo.")
            salida(resultado, response)   

print("Hola buenas, bienvenido al programa de web scraper, a continuacion debera introducir la URL de la pagina.")
time.sleep(2)
introducir_url()

url = introducir_url()
response = requests.get(url)