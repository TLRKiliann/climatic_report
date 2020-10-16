#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


from bs4 import BeautifulSoup
import requests


url = "https://www.historique-meteo.net/europe/suisse/lausanne/2020/08/"
tds=[]
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup.text)
divs = soup.findAll("table", {"class": "table table-striped"})
with open('myscrap.txt', '+w') as file:
    for div in divs:
        rows = div.findAll('td')
        for row in rows:
            if row.b != None:
                tds.append(row.findAll('b'))
                print(row.b)
                file.write(str(row.b) + '\n')
