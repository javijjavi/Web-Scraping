import requests                     
from bs4 import BeautifulSoup      
import mysql.connector
import re
import subprocess
import base64
import os


q = 0
p = open("iptables.rules.out", "w", encoding="utf-8")
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
                if len(i.text) > 8:
                    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i.text).group()
                    #print(ip)
                    p.write(str("iptables -I OUTPUT -s "+ ip +" -i DROP"+'\n'))
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
                if len(i.text) > 8:
                    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i.text).group()
                    #print(ip)
                    p.write(str("iptables -I OUTPUT -s "+ ip +" -i DROP"+'\n'))
            j += 1
    h = h - 1
    q = int(q)
    #print(url)
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

with open('iptables.rules.out', 'rb') as f:
    data = f.read()
with open('iptables.rules', 'wb') as f:
    f.write(base64.encodebytes(data))

#subprocess.call("./home/iptables.sh", shell=True)
p.close()
f.close()
os.remove("iptables.rules.out")

