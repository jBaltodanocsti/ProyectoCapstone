from fastapi import FastAPI

import ML
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional,Text


class departamento(BaseModel):
    metros_cuadrados:int
    distrito:int
    antiguedad:int
    desgaste:int
    dormitorios:int
    baños:int
    

app = FastAPI()

origins = ["http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
def read_root():
    return {"welcome":"wellcum to my REST APIcito"}

@app.post("/calcular")
def calcular(request:departamento):
    print(request)
    datos = [request.metros_cuadrados, request.distrito, request.antiguedad, request.desgaste, request.dormitorios, request.baños]
    resultado = ML.procesar_datos(datos)
    return round(float(resultado),2)
     


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)