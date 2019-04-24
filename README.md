# WEB SCRAPPER

## ¿QUE ES WEB SCRAPING?
Web scraping es una técnica que sirve para extraer información de páginas web de forma automatizada.

## VENTAJAS DE UTILIZAR WEB SCRAPING
Las posibilidades del Web Scrapping son practicamente infinitas, ahora voy a nombrar algunas pero, repito, las posibilidades son infinitas.
***
- Visibilidad en Social Network: Podemos utlizar un web scrapping para sacar informacion de una red social y poder poner comentarios automatizados, en todos los paramaetros que nosotros queramos.
- Comparador: Podemos extrar información de diferentes paginas y comprararlas entre ellas, por ejemplo diferentes paginas de viajes para comprarar que pagina de viaje ofrece el mejor precio, pero tambien podemos extraer esta informacion y luego compararla con la misma pagina un tiempo después para ver como ha cambiado el precio de sus productos.
- Extraer información: Podemos extrar la información que sea de de cualquier pagina web y luego despues procesarla como nosotros queramos, por ejemplo introducirla en una base de dato, en un excel o en un txt.

## HERRAMIENTAS DE WEB SCRAPING
Esta son algunas de las herramientas de web scraping que podemos encontrar en la red:
- [import](https://www.import.io)
- [Google Scraper](https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd)
- [dexi](https://dexi.io)
- [mozenda](https://www.mozenda.com)
- [hunter](https://hunter.io)

## WEB SCRAPPING CON PYTHON
Ahora vamos a crear nuestro propio web scraper diseñado a medida para cumplir nuestra función.     
Nosostros queremos extraer toda la información de la siguiente web: [https://ransomwaretracker.abuse.ch/tracker/](https://ransomwaretracker.abuse.ch/tracker/)        
Esta web esta enfocada a publicar IP, hots, etc con malware asociado a ellas, como podemos ver hay una cantidad de direcciones IP y hots bastante grande haciendo que si una persona por si sola tubiera que extraer toda esta información seria una tarea largisima y muy tediosa.        
Nosotros vamos a simplificar esta tarea para ello vamos a extraer toda la información de esta web luego vamos a procesar esta información en un txt para hacer iptables para un firewall y también procesaremos esta información para un SQL para poder ver esta informacion mas comodamente en un html y saber siempre que ip tables tiene nuestro firewall activas.

## LIBRERIAS QUE VAMOS A UTILIZAR
Para realizar este proyecto en Python3 vamos necesitar dos librerias:
***
- request           (Libreria para descargar el codigo HTML)
- Beautiful Soup    (Libreira para parsear el codigo HTML)
- mysql.connector   (Libreria que utilizaremos para conectarnos con la base de datos)
- re                (Libreria para utilizar para poder utilizar expresiones regulares)

## DESCARGAR EL CODIGO HTML
Para descargar el codigo HTML de una pagina web tendremos que utilizar la libreria request, para esto preimero la tendremos que importar esto es bastante sencillo solo tendremos que poner el siguiente codigo `import requests`.    
Ahora toca descargar el codigo HTML para eso utilizaremos el codigo `response = requests.get(url)`. Y ya tendremos nuestro codigo HTML descargado.

## PARSEAR EL CODIGO HTML
Para parsear el codigo HTML de un codigo HTML utilizaremos la libreia BeautifulSoup para importala introduciremos el siguiente codigo `from bs4 import BeautifulSoup`.      
Esta libreria nos premite parsear codigo HTML, ahora vamos a indicarle que queremos parsear el codigo que acabamos de descargar, para ello ejecutamos este comando `soup = BeautifulSoup(response.text, "html.parser")`.        
Ahora tenmos que empezar a pensar que procedimiento vamos a utilizar, lo primero que obsevamos es que toda la informacion que queremos extrar esta dentro de la misma tabla, pero obviamente no queremos extrar toda esta informacion solo algunos campos.     
Para ello vamos a ir ejecutando parseos poco a poco hasta quedarnos con el resultado:              
1. Buscamos el elemento table dentro de nuestro HTML `table = soup.find('table')`.                        
2. Le decimos que dentro de este nos busque todos los tr `table_rows = table.find_all('tr')`.                           
3. Creamos un bucle que nos analize todos los tr y dentro de estos todos los td        
```python                         
for tr in table_rows:             
        h += 1              
        td = tr.find_all('td')        
        j = 0
```                      

4. Por ultimo vamos a utilizar expresiones regulares y los bucles para extraer solo la informacion que nos interesa.       
```python                      
for i in td:                                             
            if j == 5:                                
                if len(i.text) < 8:                           
                    print("(n/a)")                     
                    ip.append("(n/a)")                      
                    print("")                        
                else:                                
                    print("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))                    
                    ip.append("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))                           
                    print("")                             
            elif j == 2:                           
                print("Malware-> "+ i.text)                 
                malware.append("Malware-> "+ i.text)                      
            elif j == 3:                            
                print("Host->"+i.text)                                      
                host.append("Host->"+i.text)                             
            elif j == 4:                       
                if len(i.text) < 4:                      
                    print("(n/a)")                         
                    dominio.append("(n/a)")                   
                else:                          
                    print("Dominio-> "+i.text)                      
                    dominio.append("Dominio-> "+i.text)                         
            j += 1
```                      

5. Con esto ya tendriamos toda la informacion que queremos.

## PROCESAR LOS RESULTADOS
Una vez extraida toda la informacion que queremos tenemos diferentes formas de procesarla, estos son solo unos ejemplos:
- Mostrarla por la terminal.
- Metero dentro de un documenteto de texto (.txt)
- Meterlo dentro de una base de datos.
- Meterlos en un ISP o crear reglas con IP-Tables.
- Meterlos en un excel.

## PROCESANDO LOS RESULTADO
Ahora vamos a analizar cada uno de los archivos y cual es su función.
- **webscrapper.py** La funcion de este archivo es la de recoger solo la informacion de la pagina https://ransomwaretracker.abuse.ch/tracker/ y mostrarla por pantalla, se mostrará IP, pais, malware, host y dominio.
- **webscrapper-funcion.py** La funcion de este archivo es mostrar en pantalla la IP, pais, malware, host y dominio de la pagina https://ransomwaretracker.abuse.ch/tracker/ y de sus 138 paginas.
- **webscrapper-txt.py** La funcion de este archivo es recoger los mismos que el archivo de arriba, pero esta vez no lo mostrará por pantalla, si no que creará un txt y los dejará alamacenados ahi.
- **webscrapper-iptables.py** La funcion de este archivo es recoger solo las IP de la paginiga https://ransomwaretracker.abuse.ch/tracker/ y de sus 138 paginas extras, y volcarlo todo en un archivo en formato texto plano, con el nombre iptables.rules, a este archivo se le aplica unas reglas de iptables para denegar cualquier conexion con la IP.
