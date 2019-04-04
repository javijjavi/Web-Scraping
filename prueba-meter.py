
import requests                     
from bs4 import BeautifulSoup      
import mysql.connector
import re

q = 0
malware = ""
ip = ""
host = ""
dominio = ""
def funcion_datos(malware, ip, host, dominio):
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
       
        for i in td:
            if j == 5:
                if len(i.text) < 8:
                    print("(n/a)")
                    ip=("(n/a)")
                    print("")
                else:
                    print("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    ip=("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    print("")
            #elif j == 0 or j == 1:
                #print("")
            elif j == 2:
                print("Malware-> "+ i.text)
                malware=("Malware-> "+ i.text)
            elif j == 3:
                print("Host->"+i.text)
                host=("Host->"+i.text)
            elif j == 4:
                if len(i.text) < 4:
                    print("(n/a)")
                    dominio=("(n/a)")
                else:
                    print("Dominio-> "+i.text)
                    dominio=("Dominio-> "+i.text)
            #else:
                #print(i.text)
            j += 1
    h = h - 1
    print(h)
    return malware, ip, host, dominio




malware1 = ""
ip1 = ""
host1 = ""
dominio1 = ""

def funcion_datos_paginas(q, malware1, ip1, host1, dominio1):
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
        
        for i in td:
            if j == 5:
                if len(i.text) < 8:
                    print("(n/a)")
                    ip1=("(n/a)")
                    print("")
                else:
                    print("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    ip1=("IP(Pais)-> "+re.sub(r"([^)]+).*",r"\1)", i.text))
                    print("")
            #elif j == 0 or j == 1:
                #print("")
            elif j == 2:
                print("Malware-> "+ i.text)
                malware1=("Malware-> "+ i.text)
            elif j == 3:
                print("Host->"+i.text)
                host1=("Host->"+i.text)
            elif j == 4:
                if len(i.text) < 4:
                    print("(n/a)")
                    dominio1=("(n/a)")
                else:
                    print("Dominio-> "+i.text)
                    dominio1=("Dominio-> "+i.text)
            #else:
                #print(i.text)
            j += 1
    h = h - 1
    #print(h)
    q = int(q)
    print(url)
    return q, malware1, ip1, host1, dominio1
p = open("final.txt", "w", encoding="utf-8")
for q in range(138+1):
    if q == 0:
        p.write(str(funcion_datos(malware, ip, host, dominio))+'\n')
        p.write('\n')
        q += 1
    elif q > 0:
        p.write(str(funcion_datos_paginas(q, malware1, ip1, host1, dominio1))+'\n')
        p.write('\n')
        q += 1
        print(q)
    elif q == 139:
        p.close()
        print(q)
        break