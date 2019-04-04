import requests                     
from bs4 import BeautifulSoup      
import mysql.connector
import re

q = 0
def funcion_datos():
    url = "https://ransomwaretracker.abuse.ch/tracker/"                 
    response = requests.get(url)                                       
    soup = BeautifulSoup(response.text, "html.parser")     
    table = soup.find('table')
    table_rows = table.find_all('tr')
    h = 0
    for tr in table_rows:
        #print(h)
        h += 1
        td = tr.find_all('td')
        #row = [i.text for i in td]
        j = 0
        malware = []
        ip = []
        host = []
        dominio = []
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
            #elif j == 0 or j == 1:
                #print("")
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
            #else:
                #print(i.text)
            j += 1
    h = h - 1
    print(h)
    return malware, ip, host, dominio

def funcion_datos_paginas(q):
    q = str(q)
    url = "https://ransomwaretracker.abuse.ch/tracker/page/"+q+"/"                 
    response = requests.get(url)                                       
    soup = BeautifulSoup(response.text, "html.parser")     
    table = soup.find('table')
    table_rows = table.find_all('tr')
    h = 0
    for tr in table_rows:
        #print(h)
        h += 1
        td = tr.find_all('td')
        #row = [i.text for i in td]
        j = 0
        malware1 = []
        ip1 = []
        host1 = []
        dominio1 = []
        for i in td:
            if j == 5:
                if len(i.text) < 8:
                    print("(n/a)")
                    ip1.append("(n/a)")
                    print("")
                else:
                    print("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    ip1.append("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    print("")
            #elif j == 0 or j == 1:
                #print("")
            elif j == 2:
                print("Malware-> "+ i.text)
                malware1.append("Malware-> "+ i.text)
            elif j == 3:
                print("Host->"+i.text)
                host1.append("Host->"+i.text)
            elif j == 4:
                if len(i.text) < 4:
                    print("(n/a)")
                    dominio1.append("(n/a)")
                else:
                    print("Dominio-> "+i.text)
                    dominio1.append("Dominio-> "+i.text)
            #else:
                #print(i.text)
            j += 1
    h = h - 1
    #print(h)
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
        print(q)
    elif q == 139:
        print(q)
        break