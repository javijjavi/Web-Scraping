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
Para descargar el codigo HTML de una pagina web tendremos que utilizar la libreria request.  
`import requests`
Con este codigo descargaremos la librería.  
Ahora toca descargar el codigo HTML para eso utilizaremos el codigo `response = requests.get(url)`.
Y ya tendremos nuestro codigo HTML descargado.

