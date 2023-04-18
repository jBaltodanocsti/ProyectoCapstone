import requests
from bs4 import BeautifulSoup
import csv

import os
import ctypes
import requests_html
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
     # Código para recopilar los datos de la página web y guardarlos en un archivo CSV
    session = requests_html.HTMLSession()
    session.cookies.clear()

    url = 'https://www.adondevivir.com/inmuebles-en-venta-en-lima-provincia.html'
    response = session.get(url, cookies={'cookie1': 'value1', 'cookie2': 'value2'}, verify=False)
    response.html.render()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    containers = soup.find_all('div', {'class': 'posting-container'})
    
    data_list = []
    print(soup)
    for container in containers:
        
        link = container['data-to-posting']
        response = requests.get(url, verify=True)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('div', class_='price-items').get_text().strip()
        print('Price:', price)
        # Aquí puedes agregar el código para extraer los datos que necesitas y agregarlos a la lista data_list
    
    with open('datos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['metros', 'distrito', 'antiguedad', 'desgaste', 'dormitorios', 'banos', 'valor'])
        writer.writerows(data_list)

else:
    print("Este script debe ser ejecutado como administrador")
    exit()