
import requests                     
from bs4 import BeautifulSoup      
import mysql.connector
import re

q = 0
p = open("Webscrapper-txt.txt", "w", encoding="utf-8")
def funcion_datos():
    url = "https://ransomwaretracker.abuse.ch/tracker/"                 
    response = requests.get(url)                                       
    soup = BeautifulSoup(response.text, "html.parser")     
    table = soup.find('table')
    table_rows = table.find_all('tr')
    h = 0
    for tr in table_rows:
        h += 1
        td = tr.find_all('td')
        j = 0  
        for i in td:
            if j == 5:
                if len(i.text) < 8:
                    p.write(str("(n/a)")+'\n')
                    p.write('\n')
                else:                  
                    ip=("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text)+'\n')
                    p.write(str(ip)+'\n')
                    p.write('\n')
            elif j == 2:
                p.write(str("Malware-> "+ i.text)+'\n')
            elif j == 3:
                p.write(str("Host-> "+ i.text)+'\n')
            elif j == 4:
                if len(i.text) < 4:
                    p.write(str("(n/a)")+'\n')
                else:
                    p.write(str("Dominio-> "+ i.text)+'\n')
            j += 1
    h = h - 1
    return
def funcion_datos_paginas(q):
    q = str(q)
    url = "https://ransomwaretracker.abuse.ch/tracker/page/"+q+"/"                 
    response = requests.get(url)                                       
    soup = BeautifulSoup(response.text, "html.parser")     
    table = soup.find('table')
    table_rows = table.find_all('tr')
    h = 0
    for tr in table_rows:
        h += 1
        td = tr.find_all('td')
        j = 0
        for i in td:
            if j == 5:
                if len(i.text) < 8:
                    p.write(str("(n/a)")+'\n')
                    p.write('\n')
                else:
                    ip=("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    p.write(str(ip)+'\n')
                    p.write('\n')
            elif j == 2:
                p.write(str("Malware-> "+ i.text)+'\n')
            elif j == 3:
                p.write(str("Host-> "+ i.text)+'\n')
            elif j == 4:
                if len(i.text) < 4:
                    p.write(str("(n/a)")+'\n')
                else:
                    p.write(str("Dominio-> "+ i.text)+'\n')
            j += 1
    h = h - 1
    q = int(q)
    print(url)
    return q


for q in range(138+1):
    if q == 0:
        funcion_datos()
        q += 1
    elif q > 0:
        funcion_datos_paginas(q)
        q += 1
    elif q == 139:
        break