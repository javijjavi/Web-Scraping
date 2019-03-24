#Importamos librerias
import requests                     #Libreira request una libreria HTTP para Python
from bs4 import BeautifulSoup       #Libreria BeautifulSoup orientada a parsear la información

#Primero descargamos todo el codigo HTML
url = "https://ransomwaretracker.abuse.ch/tracker/"                 #Esta es la URL de la cual vamos a extraer todo el codigo HTML
response = requests.get(url)                                        #Utilizamos nuestra libreria requests para descargar el contenido de la carpeta en formato binario
#Si ejecutamos solo esto la respuesta tendria que ser <Response [200]> esto nos indica que la respuesta ha sido OK


#Si ejecutamos este comando podremos guardar la peticion get pasada formate texto en un archivo txt para comprobar que todo se descarga correctamente
with open('responseHTML.txt', 'w') as file:
    file.write(response.text)


soup = BeautifulSoup(response.text, "html.parser")      #Parseamos el HTML, response.text hace referencia a la peticion pasada a texto 

#Si nos dirigimos al codigo HTML observaremos que toda la informacion que queremos en guardada en tablas en concreto en esta <table class="maintable"> asi que vamos a extraer toda esta información
tablaHTML = soup.find_all("table", "maintable")
print(tablaHTML)