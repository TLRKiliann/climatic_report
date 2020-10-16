#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


from bs4 import BeautifulSoup
import requests


url = "https://www.historique-meteo.net/europe/suisse/lausanne/2011/"
tds=[]
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup.text)
divs = soup.findAll("table", {"class": "table"})
with open('ws_avtemp11.txt', '+w') as file:
    for div in divs:
        rows = div.findAll('tr')
        for row in rows:
            tds.append(row.findAll('td'+'b'))
            print(row.td, row.b)
            file.write(str(row.td) + str(row.b) + '\n')

