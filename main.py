import ML
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from pydantic import BaseModel
import pdb


app = FastAPI(debug=True)
#templates = Jinja2Templates(directory="templates")


origins = ["http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inmueble(BaseModel):
    metros_cuadrados: int
    distrito: int
    antiguedad: int
    desgaste: int
    dormitorios: int
    baños: int
"""
# Crear la ruta POST para procesar los datos y devolver la respuesta
#import pdb; pdb.set_trace()
@app.post("/calcular")
async def calcular(request: Inmueble):
    # Obtener los datos JSON de la solicitud
    inmueble_data = await request.json()
    # Crear una instancia de la clase Inmueble con los datos recibidos
    inmueble = Inmueble(**inmueble_data["Inmueble"])
    # Procesar los datos del inmueble utilizando su función existente
    resultado = Untitled.procesar_datos(inmueble.metros_cuadrados, inmueble.distrito, inmueble.antiguedad, inmueble.desgaste, inmueble.dormitorios, inmueble.baños)
    # Devolver el resultado como respuesta en formato JSON
    return {"resultado": resultado}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
"""
@app.post("/calcular")

async def calcular(request: Inmueble):
    pdb.set_trace()
    # Obtener los datos JSON de la solicitud

    inmueble = Inmueble(**request.Inmueble)

    # Procesar los datos del inmueble utilizando su función existente
    resultado = ML.procesar_datos(inmueble.metros_cuadrados, inmueble.distrito, inmueble.antiguedad, inmueble.desgaste, inmueble.dormitorios, inmueble.baños)
    # Devolver el resultado como respuesta en formato JSON
    return {"resultado": resultado}

async def calcular(request: Inmueble):
    # Crear una instancia de la clase Inmueble con los datos recibidos, realizando conversiones de datos según sea necesario
    inmueble = Inmueble(metros_cuadrados=float(request.metros_cuadrados), 
                        distrito=float(request.distrito), 
                        antiguedad=float(request.antiguedad), 
                        desgaste=float(request.desgaste), 
                        dormitorios=float(request.dormitorios), 
                        baños=float(request.baños))
    # Procesar los datos del inmueble utilizando su función existente
    resultado = ML.procesar_datos(inmueble.metros_cuadrados, inmueble.distrito, inmueble.antiguedad, inmueble.desgaste, inmueble.dormitorios, inmueble.baños)
    # Devolver el resultado como respuesta en formato JSON
    return {"resultado": resultado}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)