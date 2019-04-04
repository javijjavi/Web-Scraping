import requests                     
from bs4 import BeautifulSoup      
import mysql.connector
import re

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
                ip=(+re.sub(r"([^)]+).*",r"\1)", i.text))
                print(ip)
        j += 1
h = h - 1