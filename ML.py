#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt
import openpyxl
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


# In[2]:

# Cargar datos de Excel
data = pd.read_csv('datos_inmuebles.csv', delimiter=';')
print(data.columns)
# Separa las características y la variable objetivo
X = data[['metros', 'distrito', 'antiguedad', 'desgaste', 'dormitorios', 'banos']].values
y = data['valor'].values

# In[196]:
# Normaliza los datos de entrada
variances = np.var(X, axis=0)

# Encuentra las columnas con una varianza muy baja (por ejemplo, menor que 0.001)
low_variance_columns = np.where(variances < 0.001)[0]

# Calcula la media y la desviación estándar de las columnas restantes
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

# Normaliza los datos
X = (X - mean) / std



# In[197]:

# Divide los datos en conjuntos de entrenamiento y validación
val_size = 0.2
val_samples = int(len(X) * val_size)
train_X, train_y = X[:-val_samples], y[:-val_samples]
val_X, val_y = X[-val_samples:], y[-val_samples:]


# In[198]:

# Crea el modelo de red neuronal
model = Sequential()
model.add(Dense(32, input_shape=(6,), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))


# In[199]:


# Compila el modelo
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])


# In[205]:

# Entrena el modelo
history = model.fit(train_X, train_y, epochs=100, batch_size=16, validation_data=(val_X, val_y))


# In[206]:

# Realiza una predicción para un nuevo inmueble
# numpy float32
nuevo_inmueble = np.array([[150, 40, 20, 2, 3, 2]]) # valores de las características del nuevo inmueble
nuevo_inmueble = (nuevo_inmueble - mean) / std
prediccion = model.predict(nuevo_inmueble)

print("El valor estimado del inmueble es: ", prediccion[0][0])


# In[ ]:

def procesar_datos(datos):
    # convertir la lista a un array numpy
    nuevo_inmueble = np.array([datos], dtype=np.float32)

    #normalizar los datos
    nuevo_inmueble = (nuevo_inmueble - mean) / std

    # hacer la predicción
    prediccion = model.predict(nuevo_inmueble)

    resultado = prediccion[0][0]
    return resultado




# In[ ]:




