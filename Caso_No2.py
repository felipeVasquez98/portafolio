#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Caso de Negocio No. 2:

# Librería para comando de sistema
import os
# Librería para manejo de datos
import pandas as pd
# Librerías para graficar
# El uso de plotly permite analizar los gráficos pasando el mouse sobre ellas
# También se puede redimensionar el gráfico a conveniencia
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


pd.__version__


# In[3]:


# Cargar los datos en csv
df = pd.read_csv("vehicles.csv", error_bad_lines=False, engine='python')
df


# # 1) Se omite el .0 de la columna "year":

# In[4]:


df2 = df
df2['year'] = df2['year'].astype(str).str.split('.', expand = True)[0]
df2


# # 2) Se cuenta cuántas veces se repiten las regiones y se ordenan de mayor a menor

# In[5]:


#Se implementa set_option() para observar todas las filas
pd.set_option("display.max_rows", 404)

#Se hace el conteo por cada una de las regiones y se ordena de mayor a menor
tabla = df['region'].value_counts().reset_index().rename({'index':'region', 'region':'total'})
tabla


# # 3) Ahora se elimina todos los valores nulos (NaN) de la tabla anterior:

# In[6]:


df_new = df2.dropna()
print(df_new)
df_new.reset_index().to_csv('new_file.csv', header=True, index=False)
df2.isna().sum()/len(df2)


# # 4) Registros con 'Price' >= 15000 and ('Condition' == Good or 'Condition' == Excellent)

# In[7]:


df3 = df2
#df3.dtypes

#Se realiza el primer filtro por precio >= 15000 
filtro1 = df3['price'] >= 15000
filtrado1 = df3[filtro1]

#Se filtra el filtro creado anteriormente por condición 'good' o condición 'excellent'
filtro2 = filtrado1['condition'].str.contains('good') | filtrado1['condition'].str.contains('excellent')
filtrado2 = filtrado1[filtro2]

filtrado2


# # 5) Conteo autos azules manufacturados por Chevrolet

# In[8]:


df4 = filtrado2

#Se realiza el filtro en 'manufacturer' para todas las columnas que no son nulas.
filtro3 = df4['manufacturer'].notnull()
filtrado3 = df4[filtro3]

#Se realiza el filtro en 'paint_color' para todas las columnas que no son nulas
filtro4 = filtrado3['paint_color'].notnull()
filtrado4 = filtrado3[filtro4]

#Se realiza el filtro en 'paint_color' para todos los registros que tienen color azúl
filtro5 = filtrado4['paint_color'].str.contains('blue')
filtrado5 = filtrado4[filtro5]
filtrado5


# In[9]:


#Se realiza el conteo de los diferentes 'manufacturer' con color azúl
tabla2 = df['manufacturer'].value_counts().reset_index()
tabla2


# Como se pudo apreciar anteriormente, el número total de carros fabricados por Chevrolet que son de color azúl es de **55064**

# # 6) Visualización de registros por región en un mapa

# In[10]:


df5 = pd.read_csv("vehicles.csv", error_bad_lines=False, engine='python')[['region']]


# In[11]:


tabla3 = df5.value_counts().reset_index()
tabla3


# In[12]:


df5.value_counts().reset_index().to_csv('new_mapa.csv', header=True, index=False)


# In[13]:


us_region = pd.read_csv("new_mapa_2.csv", encoding='unicode_escape')
us_region['lon'] = us_region['lon'].astype(float)

fig = px.scatter_mapbox(us_region, lat="lat", lon="lon", hover_name="region", hover_data=["total"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[14]:


us_region.dtypes


# In[ ]:




