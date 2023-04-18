#importamos el modulo
from bs4 import BeautifulSoup
#importamos el modulo requests
import requests
import random
import coneccion

# Lista de proxies
proxies = ['http://190.119.167.11:5678',
'http://181.176.211.168:8080',
'http://190.116.56.74:999',
'http://200.60.71.10:46934',
'http://181.65.193.242:999',
'http://190.43.92.248:5678',
'http://181.65.139.237:999',
'http://131.255.138.161:80',
'http://200.123.15.252:999',
'http://181.65.128.139:999',
'http://200.123.15.250:999',
'http://190.12.95.170:47029',
'http://200.37.107.106:8888',
'http://181.65.242.86:10101',
'http://200.123.15.194:999',
'http://179.43.94.238:999',
'http://200.123.29.37:3128',
'http://200.123.29.36:3128',
'http://200.123.29.45:3128',
'http://200.123.29.41:3128',
'http://181.65.128.140:999',
'http://161.132.113.180:999',
'http://200.123.29.40:3128',
'http://190.187.201.26:8080',
'http://181.176.175.247:999',
'http://200.123.15.251:999',
'http://181.176.166.17:80',
'http://200.123.29.35:3128',
'http://190.238.231.118:1994',
'http://200.123.29.39:3128',]
#coneccion.buscar(proxies)
# Función para hacer una petición HTTP utilizando un proxy aleatorio
def make_request(url):
    proxy = random.choice(proxies)
    response = requests.get(url, proxies={'http': proxy, 'https': proxy})
    return response

# Ejemplo de uso


#Guardamos en una variable la url
url = "https://www.adondevivir.com/inmuebles-en-venta-en-lima-provincia-soles.html"
#Realizamos una peticion de la web

#Comprobamos que la peticion es correcta
for i in range(100):
    page = make_request(url)
    if page.status_code == 200:
        print (i)
        #pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        soup = BeautifulSoup(page.content, "html.parser")
        #Obtenemos todos los elementos div con clase postings-container
        postings_containers = soup.find_all('div', class_= 'postings-container')
        #Iteramos sobre los elementos encontrados
        for postings_container in postings_containers:
            #Obtenemos el link de la propiedad
            link_propiedad = postings_container.find('div', {'data-to-posting': True}).get('data-to-posting')
            #concatenamos el link de la pagina con el link de la propiedad
            url_propiedad = "https://www.adondevivir.com/" + link_propiedad
            #Realizamos una peticion de la web
            page_propiedad = requests.get(url_propiedad)
            #Comprobamos que la peticion es correcta
            if page_propiedad.status_code == 200:
                #pasamos el contenido HTML de la web a un objeto BeautifulSoup()
                soup_propiedad = BeautifulSoup(page_propiedad.content, "html.parser")
                #Obtenemos el precio
                price_item = soup_propiedad.find('div', class_= 'block-price block-row').find('div', class_= 'block-price-containerd').find('div', id= 'pc-container').find('div', id= 'detailTitle').find('div', class_= 'price-items')
                #imprimimos el precio
                print(price_item.text.strip())
    #En caso de que no se realice la peticion
    else:
        print("Error al obtener la pagina")