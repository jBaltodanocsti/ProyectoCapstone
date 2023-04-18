import requests
from bs4 import BeautifulSoup
def buscar(direcciones_ip):
    url = 'https://www.sslproxies.org/'

    # Hacemos la petición a la web
    req = requests.get(url)

    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = req.status_code
    if status_code == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los elementos de la tabla "tr" con clase "postings-container"
        elementos = html.find_all('tr')[1:-1]

        # Creamos una lista vacía para almacenar las direcciones IP
        
        i=0
        # Recorremos todos los elementos para extraer las ip y el puerto
        for el in elementos:
            if i == 100:
                break
            i += 1
            # Buscamos todos los elementos "td" en la fila actual
            td = el.find_all('td')
            # Comprobamos si hay suficientes elementos "td" en la fila actual
            if len(td) >= 2:
                # Extraemos la IP y el puerto
                ip = td[0].text
                puerto = td[1].text
                # Agregamos la dirección IP a la lista con el formato deseado
                direccion_ip = f"http://{ip}:{puerto}"
                direcciones_ip.append(direccion_ip)
        return direcciones_ip
    else:
        print("Error al obtener la información")
